#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
os.getcwd() 


# In[4]:


os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')


# In[5]:


import glob
glob.glob('*.py')


# In[6]:


import sys
print(sys.argv)


# In[7]:


sys.stderr.write('Warning, log file not found starting a new one\n')


# In[8]:


import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')


# In[9]:


re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')


# In[10]:


import math
math.cos(math.pi / 4)


# In[11]:


math.log(1024, 2)


# In[12]:


from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)



import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org
Beware the Ides of March.
""")
server.quit()


# In[13]:


# dates are easily constructed and formatted
from datetime import date
now = date.today()
now


# In[14]:


now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")


# In[15]:


# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days


# In[16]:


import zlib
s = b'witch which has which witches wrist watch'
len(s)


# In[17]:


t = zlib.compress(s)
len(t)


# In[18]:


zlib.decompress(t)


# In[19]:


zlib.crc32(s)


# In[20]:


from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()


# In[21]:


Timer('a,b = b,a', 'a=1; b=2').timeit()


# In[ ]:




