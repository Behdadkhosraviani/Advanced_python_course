#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[13]:


email = input()


# In[14]:


res = re.search(r'^.*@[^\d\n]+\.[^\d\n]+',email)


# In[15]:


if res == None:
    print("WRONG")
else:
    print("OK")

