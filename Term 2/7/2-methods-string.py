a = "Lacus Leo luctus accumsan Leo tortor posuere ac."

a_upper = a.upper()
a_lower = a.lower()
print(a)
# print(a_upper)
# print(a_lower)
# print(a)

a_capitalize = a.capitalize()
a_title = a.title()
# print(a_capitalize)
# print(a_title)
a_center = a.center(50)
# print(a_center)

a_count = a.count('p')
# print(a_count)

a_endswith = a.endswith(' ')
# print(a_endswith)
a_startswith = a.startswith('L')
# print(a_startswith)

a_find = a.find('Leo')
print(a_find)
a_index = a.index('Leo')
print(a_index)

# islower()
# isupper()

# isdigit()	Returns True if all characters in the string are digits
# isdecimal()	Returns True if all characters in the string are decimals
# isnumeric()	Returns True if all characters in the string are numeric
# +-------------+-----------+-------------+----------------------------------+
# | isdecimal() | isdigit() | isnumeric() |          Example                 |
# +-------------+-----------+-------------+----------------------------------+
# |    True     |    True   |    True     | "038", "０３８"                   |
# |  False      |  False    |  False      | "abc", "38.0", "-38"             |
# +-------------+-----------+-------------+----------------------------------+
# isalnum()	Returns True if all characters in the string are alphanumeric

# isalpha()	Returns True if all characters in the string are in the alphabet
# isidentifier()	Returns True if the string is an identifier
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
