#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('Algerian_forest_fires_cleaned_dataset.csv')


# In[3]:


df.head()


# In[4]:


df.drop(['Day','Month','year'],axis=1,inplace=True)


# In[5]:


df['Classes'] = np.where(df['Classes'].str.contains('not fire'),0,1)


# In[6]:


df.head()


# In[7]:


df['Classes'].value_counts()


# In[8]:


df.head()


# In[9]:


df.tail()


# ### Splitting data into independent and dependent features

# In[11]:


x = df.drop('FWI',axis=1)
y = df['FWI']


# In[12]:


x.head()


# In[13]:


y.head()


# ### Train Test Split

# In[15]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)


# In[16]:


x_train.shape


# In[95]:


x_test.columns


# In[18]:


plt.figure(figsize=(10,8))
sns.heatmap(x_train.corr(),annot=True,fmt=".2f",cmap=plt.cm.CMRmap_r,linewidth=0.5,linecolor='black')
plt.title("Correlation Matrix Heatmap", fontsize=14)


# In[19]:


def correlation(dataset, threshold):
    col_corr = set()  # Set of all the names of correlated columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold:  # we are interested in absolute coeff value
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)

    return col_corr


# In[20]:


correlated_features = correlation(x_train,0.9) # 70% of correlated features


# In[21]:


correlated_features


# In[22]:


x_train.drop(correlated_features,axis=1,inplace=True)


# In[23]:


x_test.drop(correlated_features,axis=1,inplace=True)


# In[24]:


x_train.shape


# ## Feature Scaling or Standardization

# In[26]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)


# In[27]:


x_train_scaled


# ## Box plots to understand the effect of standard scaler

# In[29]:


plt.subplots(figsize=(15,5))
plt.subplot(1,2,1)
sns.boxplot(data=x_train)
plt.title('X train before scaling')
plt.subplot(1,2,2)
sns.boxplot(data=x_train_scaled)
plt.title('X train after scaling')


# # Applying Models
# ### 1. Linear Regression Model

# In[31]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error , r2_score
regression = LinearRegression()
regression.fit(x_train_scaled,y_train)
y_pred = regression.predict(x_test_scaled)
mae = mean_absolute_error(y_test,y_pred)
score = r2_score(y_test,y_pred)
print('Mean Absolute Error ',mae)
print('R2 Score',score)
plt.scatter(y_test,y_pred)


# ### 2. Lasso Regression

# In[33]:


from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error , r2_score
lasso = Lasso()
lasso.fit(x_train_scaled,y_train)
y_pred = lasso.predict(x_test_scaled)
mae = mean_absolute_error(y_test,y_pred)
score = r2_score(y_test,y_pred)
print('Mean Absolute Error ',mae)
print('R2 Score',score)
plt.scatter(y_test,y_pred)


# ### 3. Ridge Regression

# In[35]:


from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error , r2_score
ridge = Ridge()
ridge.fit(x_train_scaled,y_train)
y_pred = ridge.predict(x_test_scaled)
mae = mean_absolute_error(y_test,y_pred)
score = r2_score(y_test,y_pred)
print('Mean Absolute Error ',mae)
print('R2 Score',score)
plt.scatter(y_test,y_pred)


# ### 3. Elastic Net Regression

# In[37]:


from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error , r2_score
elastic = ElasticNet()
elastic.fit(x_train_scaled,y_train)
y_pred = elastic.predict(x_test_scaled)
mae = mean_absolute_error(y_test,y_pred)
score = r2_score(y_test,y_pred)
print('Mean Absolute Error ',mae)
print('R2 Score',score)
plt.scatter(y_test,y_pred)


# # Cross Validation Starts

# ### 1. LassoCV

# In[40]:


from sklearn.linear_model import LassoCV
from sklearn.metrics import mean_absolute_error , r2_score
lassocv = LassoCV()
lassocv.fit(x_train_scaled,y_train)
y_pred = lassocv.predict(x_test_scaled)
mae = mean_absolute_error(y_test,y_pred)
score = r2_score(y_test,y_pred)
print('Mean Absolute Error ',mae)
print('R2 Score',score)
plt.scatter(y_test,y_pred)


# ### 2. Ridge CV

# In[42]:


from sklearn.linear_model import RidgeCV
from sklearn.metrics import mean_absolute_error , r2_score
ridgecv = RidgeCV(cv=5)
ridgecv.fit(x_train_scaled,y_train)
y_pred = ridgecv.predict(x_test_scaled)
mae = mean_absolute_error(y_test,y_pred)
score = r2_score(y_test,y_pred)
print('Mean Absolute Error ',mae)
print('R2 Score',score)
plt.scatter(y_test,y_pred)


# ### 3. Elastic Net CV

# In[44]:


from sklearn.linear_model import ElasticNetCV
from sklearn.metrics import mean_absolute_error , r2_score
elasticnetcv = ElasticNetCV()
elasticnetcv.fit(x_train_scaled,y_train)
y_pred = elasticnetcv.predict(x_test_scaled)
mae = mean_absolute_error(y_test,y_pred)
score = r2_score(y_test,y_pred)
print('Mean Absolute Error ',mae)
print('R2 Score',score)
plt.scatter(y_test,y_pred)


# In[45]:


ridgecv.alphas


# In[46]:


ridgecv.get_params()


# In[47]:


lassocv.mse_path_


# ## Now we will choose one model with highest accuracy and pickle it

# In[85]:


scaler


# In[89]:


ridge


# In[91]:


import pickle


# In[93]:


pickle.dump(scaler,open('scaler.pkl','wb')) # Dump scaler model in scaler.pkl file
pickle.dump(ridge,open('ridge.pkl','wb')) # Dumping ridge model in ridge.pkl file


# In[29]:


get_ipython().system('jupyter nbconvert --to script ModelTraining.ipynb')


# In[ ]:




