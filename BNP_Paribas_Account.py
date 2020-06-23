#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np


# In[188]:


conda install scikit-learn


# In[ ]:





# In[162]:


test = pd.read_csv("C:\\kaggle\\Dataset\\bnp\\test.csv")
train = pd.read_csv("C:\\kaggle\\Dataset\\bnp\\train.csv")


# In[ ]:





# In[135]:


test.shape


# In[136]:


train.shape


# In[13]:


test.head()


# In[31]:


train.head()


# In[163]:


# remove constant columns
remove = []
for col in train.columns:
    if train[col].std() == 0:
        remove.append(col)

train.drop(remove, axis=1, inplace=True)
test.drop(remove, axis=1, inplace=True)


# In[164]:


train.shape


# In[165]:


# remove duplicated columns
remove = []
c = train.columns
for i in range(len(c)-1):
    v = train[c[i]].values
    for j in range(i+1,len(c)):
        if np.array_equal(v,train[c[j]].values):
            remove.append(c[j])


# In[166]:


train.drop(remove, axis=1, inplace=True)
test.drop(remove, axis=1, inplace=True)


# In[167]:


test.shape


# In[168]:


train.shape


# In[169]:



y_train = train['TARGET']


# In[170]:


train.drop(['TARGET'], axis = 1, inplace = True)


# In[171]:


train.shape


# In[172]:


x_train = train


# In[173]:


x_train.shape


# In[174]:


test.shape


# In[176]:


##x_train.drop(['TARGET'],  axis =1,inplace = True)


# In[177]:


from sklearn.feature_selection import VarianceThreshold
sel = VarianceThreshold(threshold=0.01)
sel.fit(x_train)


# In[39]:


### if we sum over get_support, we get the number of features that are not constant


# In[178]:


sum(sel.get_support())


# In[179]:


x_train = sel.transform(x_train)
test = sel.transform(test)


# In[180]:


test.shape


# In[181]:


x_train.shape


# In[ ]:


# classifier
clf = xgb.XGBClassifier(missing=np.nan, max_depth=5, n_estimators=350, learning_rate=0.03, nthread=4, subsample=0.95, colsample_bytree=0.85, seed=4242)


# In[ ]:


X_fit, X_eval, y_fit, y_eval= train_test_split(X_train, y_train, test_size=0.3)


# In[ ]:


# fitting
clf.fit(X_train, y_train, early_stopping_rounds=20, eval_metric="auc", eval_set=[(X_eval, y_eval)])


# In[ ]:


print('Overall AUC:', roc_auc_score(y_train, clf.predict_proba(X_train)[:,1]))


# # End

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Startefd next

# In[107]:


test_1 = pd.read_csv("C:\\kaggle\\Dataset\\bnp\\test.csv")
train_1 = pd.read_csv("C:\\kaggle\\Dataset\\bnp\\train.csv")


# In[111]:


y =train_1['TARGET']


# In[112]:


train_1.drop(['TARGET'],  axis =1,inplace = True)


# In[114]:


from sklearn.feature_selection import SelectKBest, chi2


# In[116]:


# convert to categorical data by converting data to integers
train_1 = train_1.astype(int)


# In[117]:


train_new = SelectKBest(chi2, k =10).fit_transform(train_1, y)


# In[118]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




