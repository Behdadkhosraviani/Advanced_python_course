#!/usr/bin/env python
# coding: utf-8

# In[51]:


num = int(input())
c=[]
values=[]
for i in range(0,num):
    c.append(input())    


# In[91]:


a=list(map(lambda x :x.split("."),c))


# In[92]:


names=[]
for i in range(0,num):
    a[i][1] = a[i][1].lower()
    names.append(a[i][1][0].upper() + a[i][1][1:])
    a[i][1] = names[i]


# In[93]:


res = sorted(a,key = lambda x : (x[0],x[1]))


# In[94]:


for i in range(0,num):
    print(res[i][0],res[i][1],res[i][2])


# In[ ]:




