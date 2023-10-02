#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql


# In[2]:


db_host="localhost"
db_port=3306
db_user="root"
db_password="**************"


cnx = mc.connect(host=db_host,
           port=db_port,
           user=db_user,
           password=db_password,)

cu = cnx.cursor()


# In[3]:


"CREATE DATABASE testdb"
try:    
    q1="CREATE DATABASE testdb"
    cu.execute(q1)
    cnx.commit()
except mc.errors.DatabaseError:
    pass


# In[4]:


cnx = mc.connect(host=db_host,
           port=db_port,
           user=db_user,
           password=db_password,
           database="testdb")
cu = cnx.cursor()


# In[5]:


try:    
    q1 = """CREATE TABLE Cars(
                Name varchar(20),
                Model Smallint(4),
                Miles Int(20),
                Price int(20)
                ); 
                """
    #q1="DROP TABLE Cars"
    cu.execute(q1)
    cnx.commit()
except mc.errors.ProgrammingError:
    pass


# In[6]:


url = "https://divar.ir/s/tehran-province/auto"
row_data = rq.get(url)
soup = BeautifulSoup(row_data.text , "html.parser")

all_labels = soup.find_all("div",class_ = "kt-post-card__body")

name=[]
model=[]
mile=[]
price=[]
for i in all_labels:
    temp = i.find("h2",class_="kt-post-card__title")
    check = i.find_all("div",class_="kt-post-card__description")
    if len(check)!=2 :
        continue
    temp2 = i.find_all("div",class_="kt-post-card__description")[0].text
    temp3 = i.find_all("div",class_="kt-post-card__description")[1].text
    
    if re.search(r'(.*)مدل',temp.text) != None and re.search(r'(.*)کیلومتر',temp2)!=None and re.search(r'(.*)تومان', temp3) != None:
        name.append(re.search(r'(.*)مدل',temp.text).group(1))
    else:
        continue
        
    model.append(re.search(r'مدل(.*)',temp.text).group(1).strip())
    
    mile.append(re.search(r'(.*)کیلومتر', temp2).group(1).replace(",",""))
    
    price.append(  re.search(r'(.*)تومان', temp3).group(1).replace(",","")   )

for i in range(len(name)):
    try:
        model[i]=int(model[i])
        mile[i]=int(mile[i])
        price[i]=int(price[i])
    except ValueError:
        name[i] = None
        model[i] = None
        mile[i] = None
        price[i] = None
        continue
name = list(filter(None,name))
model = list(filter(None,model))
mile = list(filter(None,mile))
price = list(filter(None,price))

nd= [(x,y,z,t) for x,y,z,t in zip(name,model,mile,price)]

try:    
    query = """CREATE UNIQUE INDEX uniq_idx
    ON testdb.Cars(Name,Model,Miles)
    """

    cu.execute(query)
    #cnx.commit()
except mc.errors.ProgrammingError:
    pass

for n in range(len(nd)):    
    add_qu = """INSERT IGNORE INTO Cars(Name,Model,Miles,Price)
    VALUES (\"%s\",%i,%i,%i); """ % (nd[n][0],nd[n][1],nd[n][2],nd[n][3])
    cu.execute(add_qu)
    cnx.commit()


# تا این جا اطلاعات از سایت دیوار خوانده شده و در دیتابیس بدون ثبت یک داده ی تکراری ثبت شده اند . علاوه بر آن دیتای عددی به عددی قابل فهم برای پایتون تبدیل شده اند

# In[7]:


call_data = '''SELECT * FROM Cars'''
cu.execute(call_data)

rec = cu.fetchall()


# In[8]:


import pandas as pd


# In[9]:


tdata = pd.DataFrame(rec)


# In[10]:


from sklearn import tree


# In[11]:


model=tree.DecisionTreeClassifier()


# In[12]:


x = tdata.iloc[:, [True, True, True, False]].values
y = tdata.iloc[:, [False, False, False, True]].values


# In[13]:


#model.fit(x,y)
#پیش پردازش داده در این بخش نیازمند دانش خاصی است که بنده هنوز آن را دارا نیستم و از بحث دوره هم خارج است

