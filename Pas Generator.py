import string
import random
# Password Generator
Length =  int(input("Enter the length of the Pasword: "))
Characters = string.ascii_letters + string.digits + string.punctuation
Password = ''.join(random.choices(Characters,k=Length) )
print(Password)
