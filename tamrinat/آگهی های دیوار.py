#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as rq
import re
from bs4 import BeautifulSoup


# In[92]:


res = rq.get("https://divar.ir/s/tehran")

soup = BeautifulSoup(res.text , "html.parser")

a1=soup.find_all("h2", class_="kt-post-card__title")
a2=soup.find_all("div",class_="kt-post-card__description")


# In[93]:


te1=0
for i in range(0,len(a2)):
    if re.search(r'کیلومتر' , a2[i].text) != None:
        te1 +=1

for i in range(0,len(a2)-te1) :   
    if re.search(r'کیلومتر' , a2[i].text) != None :
        del a2[i]

te2=0
for i in range(0,len(a2)-te1):
    if re.search(r'ودیعه' , a2[i].text) != None:
        te2 +=1
te=te1+te2        
    
for i in range(0,len(a2)-te) :   
    if re.search(r'ودیعه' , a2[i].text) != None and re.search(r'توافقی' , a2[i].text) != None :
        del a2[i+1]
    elif re.search(r'ودیعه' , a2[i].text) != None and re.search(r'توافقی' , a2[i].text) == None :
        del a2[i]


# In[94]:


for i in range(0,len(a2)):
    if re.search(r'توافقی' , a2[i].text) != None:
        print(a1[i].text,":",a2[i].text)


# In[ ]:




