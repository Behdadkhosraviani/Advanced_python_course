#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector as mc


# In[30]:


cnx = mc.connect(host='????',
           port='????',
           user='root',
           password='',
           database='database_name',)


# In[31]:


cu = cnx.cursor()


# In[32]:


cu.execute("SELECT * FROM employees;")


# In[33]:


n=[]
h=[]
w=[]
for Height,weight,Name in cn:
    n.append(Name)
    h.append(Height)
    w.append(weight)


# In[45]:


c = [ (x,y,z) for x,y,z in zip(n,h,w)]


# In[ ]:


res = sorted(c , key = lambda x : (x[0],x[1]))


# In[ ]:


for i in range(0,len(res)):
    print(res[0],res[1],res[2])

