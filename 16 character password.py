#!6 character password
import re               #importing re madule

pwd=input()           #taking input from user
pattern='^[A-Z]{1}[a-z0-9@$#%&]{15}' #validating password pattern

result = re.search(pattern,pwd) #checking if the password  entered from user matches with the pattern

#printing if the password  pattern is correct or not with if-else statement
if result is not None:
    print("Good")
else:
    print("Bad")  