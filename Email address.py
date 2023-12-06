
import re

email=input()
pattern='^[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]'

result = re.search(pattern,email)

if result is not None:
    print("Good")
else:
    print("Bad")    