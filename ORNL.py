import re
import pyperclip as pc

first_initial = re.compile(r"(\w)(?:\W?\w+)*\s[^,]*")
last_name = re.compile(r"[^,]*\s(?!and)(\w+(?:\W?\w+)*)")


message = pc.paste()
# message = 'Rohit Srivastava, Hannah Nelsen, Peanut Smith'
first = list(first_initial.findall(message))
last = list(last_name.findall(message))

list_names = ""
for f,l in zip(first, last):
    if l == last[-1]:
        list_names += f+". "+l
    else:
        list_names += f+". "+l+", "

pc.copy(list_names)
