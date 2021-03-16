#!/usr/bin/env python
# coding: utf-8

# In[1]:


while True print('Hello world')


# In[2]:


10 * (1/0)


# In[3]:


4 + spam*3


# In[4]:


'2' + 2


# In[5]:


while True:
    try:
        x = int(input("Please enter a number : "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again..... ")


# In[6]:


raise NameError('HiThere')


# In[7]:


try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
    
KeyboardInterrupt


# In[8]:


for line in open("myfile.txt"):
    print(line,end="")


# In[9]:


with open("myfile.text") as f:
    for line in f:
        print(line, end="")


# In[ ]:




