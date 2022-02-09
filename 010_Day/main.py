def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version od the name"""
    return (f_name + ' ' + l_name).title()

print(format_name('tomek', 'romek'))