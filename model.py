#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import pickle
df=pd.read_excel('C:\\Users\\Ravi yadav\\Desktop\\air_quality.xlsx',header=1)


# In[3]:


df


# In[4]:


df['Date']=pd.to_datetime(df['Date'])


# In[5]:


df.drop('Sr No.',axis=1,inplace=True)


# In[6]:


df.info()


# In[7]:


df.dropna()


# In[8]:


df.drop(['Name of Station','Date'],axis=1,inplace=True)


# In[9]:


df.head()


# In[10]:


df['Air Quality'].nunique()


# In[33]:


df['Air Quality'].unique()


# In[44]:


((df['Air Quality']=="#") |(df['Air Quality']=="$") | (df['Air Quality']=="Not-Obtained")).sum()


# In[11]:


import seaborn as sns
x=df.corr()
sns.heatmap(x,annot=True)


# In[12]:


df.isnull().sum()


# In[13]:


df.describe()


# In[14]:


df.duplicated().sum()


# In[15]:


df.drop_duplicates( keep='first', inplace=True)


# In[16]:


from sklearn.model_selection import train_test_split


# In[ ]:


def covert_to_int(word):
    word_dict={''}
    


# In[21]:


real_x=df.iloc[:,:9]
real_y=df.iloc[:,10]


# In[23]:


training_x,testing_x,training_y,testing_y=train_test_split(real_x,real_y,test_size=.2,random_state=50)


# In[25]:


from sklearn.linear_model import LinearRegression


# In[26]:


lnr=LinearRegression()
lnr.fit(training_x,training_y)


# In[27]:


Pred_y=lnr.predict(testing_x)


# In[28]:


y_train_predict_1 = lnr.predict(training_x)


# In[29]:


lnr.score(testing_x,Pred_y)


# In[30]:


from sklearn.metrics import mean_squared_error


# In[31]:


rmse = (np.sqrt(mean_squared_error(training_y, y_train_predict_1)))


# In[32]:


rmse


# In[46]:


pickle.dump(lnr,open('model.pkl','wb'))


# In[ ]:


model=pickle.load(open('model.pkl','rb'))
print(model.predict([]))

