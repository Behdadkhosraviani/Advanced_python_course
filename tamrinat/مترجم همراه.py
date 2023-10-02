#!/usr/bin/env python
# coding: utf-8

# In[21]:


num=int(input())
c = [input().split(" ") for i in range(0,num)]


# In[23]:


sen = input()


# In[24]:


sen1 = sen.split(" ")
sen2 = []


# In[25]:


for k in sen1:    
    c1 = 0
    for i in range(0,num):
        for j in range(1,4):
            if c[i][j] == k:
                sen2.append(c[i][0])
                c1 += 1
    if c1 == 0:
        sen2.append(k)


# In[26]:


print(" ".join(sen2))


# In[ ]:




