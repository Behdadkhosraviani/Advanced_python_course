#!/usr/bin/env python
# coding: utf-8

# In[26]:


class Class:
        c=[]
        values=[]
        def __init__(self,num):
            self.num = num
        def get_values(self):
            for i in range(0,3):
                Class.c.append(input())
                Class.values=list(map(lambda x :x.split(" "),(Class.c)))
            for i in range(0,len(Class.values)):
                for j in range(0,self.num):
                    Class.values[i][j]=int(Class.values[i][j])
        def mid_age(self):
            age=[]
            if len(Class.values)==6:
                age.append((sum(Class.values[0]))/self.num)
                age.append((sum(Class.values[3]))/self.num)
            else :
                age.append((sum(Class.values[0]))/self.num)
            return age
        def mid_hight(self):
            hight=[]
            if len(Class.values)==6:
                hight.append((sum(Class.values[1]))/self.num)
                hight.append((sum(Class.values[4]))/self.num)
            else :
                hight.append((sum(Class.values[1]))/self.num)
            return hight
        def mid_weight(self):
            weight=[]
            if len(Class.values)==6:
                weight.append((sum(Class.values[2]))/self.num)
                weight.append((sum(Class.values[5]))/self.num)
            else :
                weight.append((sum(Class.values[2]))/self.num)
            return weight
        def show_value(self):
            for i in range(0,len(Class.values)):
                print((sum(Class.values[i]))/self.num)


# In[27]:


numc1=int(input())
c1=Class(numc1)
c1.get_values()

numc2=int(input())
c2=Class(numc1)
c1.get_values()


# In[31]:


c2.show_value()


# In[30]:


if c1.mid_hight()[0] > c2.mid_hight()[1]:
    print("A")
if c1.mid_hight()[0] < c2.mid_hight()[1]:
    print("B")
if c1.mid_hight()[0] == c2.mid_hight()[1]:
    if c1.mid_weight()[0] < c1.mid_weight()[1]:
        print("A")
    elif c1.mid_weight()[0] > c1.mid_weight()[1]:
        print("B")
    else :
        print("Same")

