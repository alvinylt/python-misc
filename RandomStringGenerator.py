import random

count = 0
length = int(input("How many characters do you want?"))
string = str()
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

while count < length:
    string = random.choice(char) + string
    count += 1

print(string)
