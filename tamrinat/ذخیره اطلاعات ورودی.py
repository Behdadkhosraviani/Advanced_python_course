#!/usr/bin/env python
# coding: utf-8

# In[4]:


import mysql.connector as mc
import re


# In[75]:


db_host="localhost"
db_port=3306
db_user="root"
db_password="Kordestansna1401"
db_database="onlineshop"

cnx = mc.connect(host=db_host,
           port=db_port,
           user=db_user,
           password=db_password,
           database=db_database)

cu = cnx.cursor()


# In[76]:


try:    
    q1="CREATE TABLE Users(Usernames varchar(40), Password varchar(100));"
    #q1="DROP TABLE Users"
    cu.execute(q1)
    cnx.commit()
except mc.errors.ProgrammingError:
    pass


# In[77]:


res=None
while res==None :    
    user=input("Username: ")
    res = re.search(r'^.*@[^\d\n]+\.[^\d\n]+',user)
    if res==None :
        print('Right format of email : expression@string.string')


# In[78]:


password=input("password: ")


# In[79]:


q2="INSERT INTO Users(Usernames,Password) VALUES(\'%s\',\'%s\');" %(user,password)

cu.execute(q2)
cnx.commit()


# In[ ]:




