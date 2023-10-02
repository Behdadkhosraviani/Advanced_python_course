#!/usr/bin/env python
# coding: utf-8

# In[72]:


a=[1,1,1,1,1,1,1,1,1,1]
for i in range(0,10):
    a[i]=int(input())


# In[73]:


def tedad(b):
    aval=[]
    for n in range(2,b):
        t0 = 0
        for u in range(2,n):
            if n % u == 0 :
                t0 += 1
        if t0 == 0:
            aval.append(n)
    t1=0
    for i in aval:
        if b % i == 0:
            t1 += 1
    return t1


# In[74]:


b=[1,1,1,1,1,1,1,1,1,1]
for i in range(0,10):
    b[i]= tedad(a[i])


# In[75]:


m1=max(b)
b1=[]
for i in range(0,10):
    if b[i] == m1 :
        b1.append(i)


# In[76]:


a1=[]
for i in b1:
    a1.append(a[i])


# In[77]:


m2=max(a1)


# In[78]:


print(m2 , m1)

