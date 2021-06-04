#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
print("I like ", np.pi)


# In[2]:


from scipy import misc
import matplotlib.pyplot as plt

face = misc.face()
plt.imshow(face)
plt.show()


# In[3]:


import numpy as np
get_ipython().run_line_magic('pinfo', 'np.linspace')


# In[4]:


import numpy as np
get_ipython().run_line_magic('pinfo2', 'np.linspace')


# In[5]:


a = "SciPy is awesome ;)"
get_ipython().run_line_magic('pinfo', 'a')


# In[ ]:




