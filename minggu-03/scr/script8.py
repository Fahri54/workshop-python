#!/usr/bin/env python
# coding: utf-8

# In[17]:


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
{'orange','banana','pear','apple'}
'orange' in basket                 # fast membership testing
True
'crabgrass' in basket
False

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
{'a','r','b','c','d'}
a - b                              # letters in a but not in b
{'r','d','b'}
a | b                              # letters in a or b or both
{'a','c','r','d','b','m','z','1'}
a & b                              # letters in both a and b
{'a','c'}
a ^ b                              # letters in a or b but not both


# In[ ]:




