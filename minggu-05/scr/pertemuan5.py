#!/usr/bin/env python
# coding: utf-8

# In[1]:


s = 'Heloo, world'
str(s)


# In[2]:


repr(s)


# In[3]:


str(1/7)


# In[4]:


x = 10 * 3.25
y = 200 * 200
s = 'The value of x is' + repr(x) + ', and y is' + repr(y) + '...'
print(s)


# In[5]:


hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)


# In[6]:


repr((x, y, ('spam', 'eggs')))


# In[7]:


print('We are the {} who say "{}!"'.format('knights', 'Ni'))


# In[8]:


for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    #Note use of 'end' on precious line
    print(repr(x*x*x).rjust(4))


# In[9]:


import math
print('This value of is approximately %5.3f.' %math.pi)


# In[12]:


f = open('workfile', 'w')


# In[13]:


import json
json.dumps([1, 'simple', 'list'])


# In[15]:


import math
print(f'The value of pi is approximately {math.pi:.3f}.')


# In[ ]:




