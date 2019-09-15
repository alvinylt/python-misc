#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as rd


# In[2]:


x = 0
y = input('How many characters do you want?')
y = int(y)
p = str()
r = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*()-_=+\|{[]}:;?/>.<,\'\"'


# In[4]:


while x < y:
    p = rd.choice(r) + p
    x = x + 1
print(p)

