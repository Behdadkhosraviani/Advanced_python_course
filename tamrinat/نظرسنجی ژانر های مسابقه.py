#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = int(input())
c=[]
values=[]
for i in range(0,num):
    c.append(input())    


# In[197]:


a=list(map(lambda x :x.split(),c))


# In[198]:


for i in range(0,num):
    del a[i][0]


# In[199]:


janr=["Horror", "Romance", "Comedy", "History" , "Adventure" , "Action"]
tedad=[0,0,0,0,0,0]


# In[200]:


for i in range(0,num):
    for j in range(0,3):
        for h,n in zip(janr,range(0,6)):
            if a[i][j]==h:
                tedad[n] += 1


# In[201]:


res1={"Horror" : tedad[0],
    "Romance" : tedad[1],
    "Comedy" : tedad[2],
    "History" : tedad[3] , 
    "Adventure" : tedad[4] ,
    "Action" : tedad[5]}


# In[202]:


res=sorted(res1.items(), key = lambda x: (-x[1],x[0]))


# In[203]:


for i in range(0,6):
    print(res[i][0],":",res[i][1])


# In[ ]:




