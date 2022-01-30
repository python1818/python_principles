import random

letters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

myList= random.sample(letters,10)

print (myList)
print("". join(myList))
 