#!/usr/bin/env python
# coding: utf-8

# In[5]:


from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")        # Terry arrives
queue.append("Graham")       # Graham arrives
queue.popleft()               # The first to arrive now leaves
'Eric'
queue.popleft()              # The second to arrive now leaves
'John'
queue                       # Remaining queue in order of arrival
deque(['Michael','Terry','Graham'])


# In[ ]:




