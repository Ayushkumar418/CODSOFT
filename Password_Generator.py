import random
import string
length = int (input("\nEnter the length of password: "))

charValues = string.ascii_letters + string.digits + string.punctuation
password = "".join([random.choice(charValues) for i in range(length)])
print ("Your Random Password is:",password,"\n")
