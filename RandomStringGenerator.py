import random as rd

x = 0
y = input('How many characters do you want?')
y = int(y)
p = str()
r = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*()-_=+\|{[]}:;?/>.<,\'\"'

while x < y:
    p = rd.choice(r) + p
    x = x + 1
print(p)
