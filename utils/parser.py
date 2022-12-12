# Description: Based on the total count, converts q unit to its plural form.
def pluralizer(total_count, unit, plural_suffix):
    if total_count == 1:
        return f"{total_count} {unit}"
    else:
        return f"{total_count} {unit}{plural_suffix}"
