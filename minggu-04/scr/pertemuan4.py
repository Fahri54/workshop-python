#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import fibonacci
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# In[ ]:


from fibonacci import *
fib(500)


# In[1]:


import sys
sys.ps1


# In[2]:


sys.ps2


# In[3]:


sys.ps1 = 'C> '
print('Yuck!')


# In[ ]:


import fibonacci, sys
dir(fibo)


# In[5]:


dir(sys)


# In[ ]:


import builtins
dir(builtins)

