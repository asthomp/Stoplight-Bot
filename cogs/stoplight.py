import discord
from discord import app_commands
from discord.ext import commands

from utils import admin_channel, get_admin_channel, get_admin_message, get_message, get_alert, get_emoji, \
    build_context, default_config


class Stoplight(commands.Cog):
    # Constructor - builds the Cog and registers commands.
    def __init__(self, bot):
        self.context_menu_commands = None
        self.bot = bot
        self.flagged_message = None
        # Register all context-menu commands.
        for command in self.build_context_menu_commands():
            self.bot.tree.add_command(command)

    # Destructor - removes manually-registered context-menu application commands when the cog is unloaded.
    async def cog_unload(self) -> None:
        for command in self.build_context_menu_commands():
            self.bot.tree.remove_command(command.name, type=command.type)

    # == STOPLIGHT FUNCTIONALITY ==
    @staticmethod
    async def stoplight(ctx, color, flagged_message=None):
        emoji = get_emoji(ctx.guild.id, color)
        alert = get_alert(ctx.guild.id, color)
        message = get_message(ctx, color)

        user_message = f"{emoji} {alert} {emoji} {message}"
        if len(user_message) > 0:
            await ctx.channel.send(user_message)

        # If configured, post a stoplight message to the admin channel.
        if admin_channel(ctx.guild.id):
            admin_message = get_admin_message(ctx, color)
            if len(admin_message) > 0:
                await ctx.guild.get_channel(get_admin_channel(ctx.guild.id)).send(admin_message)

        # If the user flags a message and an admin channel has been configured, embed the flagged message
        # in the admin channel.
        if admin_channel(ctx.guild.id) and flagged_message is not None and ctx.guild.id == flagged_message.guild.id:
            embed = discord.Embed(title=f"{emoji} Flagged Message")
            embed.description = flagged_message.content
            embed.set_author(name=flagged_message.author.display_name,
                             icon_url=flagged_message.author.display_avatar.url)
            embed.timestamp = flagged_message.created_at
            url_view = discord.ui.View()
            url_view.add_item(
                discord.ui.Button(label='Go to Message', style=discord.ButtonStyle.url,
                                  url=flagged_message.jump_url))

            await ctx.guild.get_channel(get_admin_channel(ctx.guild.id)).send(embed=embed, view=url_view)

    async def _text(self, ctx, color):
        await self.stoplight(ctx, color)
        await ctx.message.delete()

    async def _slash(self, interaction, color):
        ctx = await build_context(discord, interaction)
        await self.stoplight(ctx, color)
        await ctx.send(f"{default_config[color]['emoji']} A {color} stoplight was sent to <#{interaction.channel.id}>.",
                       ephemeral=True)

    async def _message_context_menu(self, interaction, color, flagged_message):
        ctx = await build_context(discord, interaction)
        await self.stoplight(ctx, color, flagged_message)
        await ctx.send(f"{default_config[color]['emoji']} A {color} stoplight was sent to <#{interaction.channel.id}>.",
                       ephemeral=True)

    # == STOPLIGHT (PREFIXED CHAT-COMMANDS) ==
    # Chat commands are sent directly to a channel using a preconfigured prefix, with the default being "stoplight".
    # Once a chat command has been issued, the command message is deleted to preserve a user's anonymity.
    # Note: While hybrid chat & application commands are available, each command is kept separate. If Discord removes
    # support for them altogether, this simplifies removal.
    @commands.command(pass_context=True)
    @commands.has_permissions(send_messages=True)
    async def green(self, ctx) -> None:
        await self._text(ctx, "green")

    @commands.command(pass_context=True)
    @commands.has_permissions(send_messages=True)
    async def yellow(self, ctx) -> None:
        await self._text(ctx, "yellow")

    @commands.command(pass_context=True)
    @commands.has_permissions(send_messages=True)
    async def red(self, ctx) -> None:
        await self._text(ctx, "red")

    # == STOPLIGHT (/SLASH APPLICATION COMMANDS) ==
    # /Slash application commands are invoked by typing "/" in the message text-box of a given channel.
    @app_commands.command(name='green', description="🟢 Green means you\'re good to continue the conversation.")
    async def _green(self, interaction: discord.Interaction) -> None:
        await self._slash(interaction, "green")

    @app_commands.command(name='yellow', description="🟡 Yellow means the conversation should proceed with caution.")
    async def _yellow(self, interaction: discord.Interaction) -> None:
        await self._slash(interaction, "yellow")

    @app_commands.command(name='red', description="🔴 Red means the conversation should stop.")
    async def _red(self, interaction: discord.Interaction) -> None:
        await self._slash(interaction, "red")

    # == STOPLIGHT (CONTEXT-MENU APPLICATION COMMANDS) ==
    # Context-Menu Application Commands do not work with decorators; this function defines them.
    # The commands are registered in the Cog constructor.
    def build_context_menu_commands(self):
        return [
            app_commands.ContextMenu(
                name='🟢 Green Stoplight',
                callback=self.__green),
            app_commands.ContextMenu(
                name='🟡 Yellow Stoplight',
                callback=self.__yellow),
            app_commands.ContextMenu(
                name='🔴 Red Stoplight',
                callback=self.__red)
        ]

    # Context-menu application commands can be invoked by right-clicking on a given message.
    async def __green(self, interaction: discord.Interaction, message: discord.Message) -> None:
        await self._message_context_menu(interaction, "green", message)

    async def __yellow(self, interaction: discord.Interaction, message: discord.Message) -> None:
        await self._message_context_menu(interaction, "yellow", message)

    async def __red(self, interaction: discord.Interaction, message: discord.Message) -> None:
        await self._message_context_menu(interaction, "red", message)
