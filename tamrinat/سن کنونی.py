#!/usr/bin/env python
# coding: utf-8

# In[2]:


import datetime as dt


# In[44]:


date=input()
date=date.split("/")


# In[45]:


for i in range(0,3):
    date[i]=int(date[i])


# In[47]:


if date[0]<0:
    print("WRONG")
elif date[1] > 12 or date[1]<0:
    print("WRONG")
elif date[2] > 31 or date[2] < 0:
    print("WRONG")
else:
    date1=dt.date(date[0],date[1],date[2])
    date2=dt.date.today()
    a=int(((date2 - date1).days) * 0.002738)
    print(a)


# In[ ]:




