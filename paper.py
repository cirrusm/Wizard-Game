import re

example = "' I AM NOT YELLING', she said. Though we knew it to not be true."


#regex
#re takes three arguemets matches we want, what we want to replace with, and the string
# this removes E and replaces it with A
new = re.sub('E', 'A', example)
print(new)

new = re.sub('[\'a-z]', 'A', example)
print(new)