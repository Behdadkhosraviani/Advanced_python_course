#!/usr/bin/env python
# coding: utf-8

# In[83]:


a1 = input()


# In[101]:


a="".join((x for x in a1 if not x.isdigit()) )


# In[102]:


a="".join((x for x in a1 if not x.isdigit()) )

a=a.replace(",","")

li=a.split()


# In[103]:


for i in range(0,len(li)-1):
    if li[i][-1] == "." :
        li[i+1] = li[i+1].lower()
        li[i]=li[i].replace(".","")
li[-1]=li[-1].replace(".","")


# In[104]:


p=0
for i in range(1,len(li)):  
    if li[i][0].isupper() :
        b=str(i+1)
        p += 1
        print(b + ":" + li[i])
if p==0 :
        print("None")

