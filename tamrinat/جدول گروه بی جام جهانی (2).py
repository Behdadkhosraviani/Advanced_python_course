#!/usr/bin/env python
# coding: utf-8

# In[184]:


Iran1,Spain1 = input().split("-")
Iran2,Portugal1 = input().split("-")
Iran3,Marocco1 = input().split("-")
Spain2,Portugal2 = input().split("-")
Spain3,Marocco2 = input().split("-")
Portugal3,Marocco3 = input().split("-")


# In[251]:


iran=[]
portugal=[]
spain=[]
marocco=[]
iran.append(int(Iran1))
iran.append(int(Iran2))
iran.append(int(Iran3))
portugal.append(int(Portugal1))
portugal.append(int(Portugal2))
portugal.append(int(Portugal3))
spain.append(int(Spain1))
spain.append(int(Spain2))
spain.append(int(Spain3))
marocco.append(int(Marocco1))
marocco.append(int(Marocco2))
marocco.append(int(Marocco3))


# In[252]:


m1=[[0,1],[iran[0],spain[0]]]
m2=[[0,2],[iran[1],portugal[0]]]
m3=[[0,3],[iran[2],marocco[0]]]
m4=[[1,2],[spain[1],portugal[1]]]
m5=[[1,3],[spain[2],marocco[1]]]
m6=[[2,3],[portugal[2],marocco[2]]]


# In[253]:


listr=[m1,m2,m3,m4,m5,m6]


# In[254]:


wins=[0,0,0,0]
looses=[0,0,0,0]
draws=[0,0,0,0]
points=[0,0,0,0]
goal_def=[0,0,0,0]


# In[255]:


for m in listr:
    if m[1][0] > m[1][1]:
        wins[m[0][0]] += 1
        looses[m[0][1]] += 1
        points[m[0][0]] += 3
        goal_def[m[0][0]] += m[1][0] - m[1][1]
        goal_def[m[0][1]] += m[1][1] - m[1][0]
    elif m[1][0] < m[1][1]:
        wins[m[0][1]] += 1
        looses[m[0][0]] += 1 
        points[m[0][1]] += 3
        goal_def[m[0][0]] += m[1][0] - m[1][1]
        goal_def[m[0][1]] += m[1][1] - m[1][0]
    else:
        draws[m[0][0]] +=1
        draws[m[0][1]] +=1
        points[m[0][0]] += 1
        points[m[0][1]] += 1
    print(goal_def)


# In[256]:


goal_def


# In[257]:


res={"Iran" : [wins[0],
               looses[0],
               draws[0],
               goal_def[0],
               points[0]],
    "Spain" : [wins[1],
               looses[1],
               draws[1],
               goal_def[1],
               points[1]],
    "Portugal" : [wins[2],
               looses[2],
               draws[2],
               goal_def[2],
               points[2]],
    "Morocco" : [wins[3],
               looses[3],
               draws[3],
               goal_def[3],
               points[3]]}


# In[258]:


from pandas import DataFrame


# In[259]:


res1=pd.DataFrame(res).T


# In[260]:


res1.columns=["wins","looses","draws"
            ,"goal difference","points"]


# In[261]:


res1=res1.sort_values(by=["points","goal difference"],ascending=False)


# In[262]:


for n in range(0,4):
    print((res1.iloc[n].name)+"  "+"wins:{}".format(res1.iloc[n,0])
              , "," ,

                                 "loses:{}".format(res1.iloc[n,1])

              , "," ,
                                 "draws:{}".format(res1.iloc[n,2])

              , "," ,

                                 "goal difference:{}".format(res1.iloc[n,3])

              , "," ,

                                 "points:{}".format(res1.iloc[n,4]))


# In[ ]:





# In[ ]:




