# Abbreviate a Two Word Name
def abbrev_name(name):
    first, second = name.title().split()
    return f"{first[0]}.{second[0]}"
abbrev_name("sarah Smith")