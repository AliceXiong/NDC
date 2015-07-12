
# coding: utf-8

# In[1]:

get_ipython().system(u'ls')


# In[115]:

# source file comes from
# http://www.fda.gov/drugs/informationondrugs/ucm142438.htm


# In[2]:

import pandas as pd
product = pd.read_csv('product.txt',sep='\t')
package = pd.read_csv('package.txt',sep='\t')


# In[3]:

product.shape


# In[4]:

package.shape


# In[5]:

#%timeit
df = pd.merge(package,product, on=['PRODUCTNDC', 'PRODUCTID'], how='left')


# In[122]:

# the purpose is to have one table contains two columns, NDCpackagecode(10 digit, lenght12)+marketingcategortyname


# In[6]:

df.shape


# In[7]:

def ndconv(code='0002-120-1'):
    s = code.split('-')
    S = []
    
    for i, L in enumerate([5,4,2]):
        
        if len(s[i]) < L:
            S.append('0'*(L-len(s[i])) + s[i])
        else:
            S.append(s[i])
        
    return '-'.join(S)
    #return ''.join(S)
ndconv()


# In[8]:

#%timeit 
df['11NDCPACKAGECODE'] = df[['NDCPACKAGECODE']].applymap(ndconv)


# In[9]:

df[['11NDCPACKAGECODE', 'NDCPACKAGECODE', 'MARKETINGCATEGORYNAME']].head()


# In[11]:

df[['11NDCPACKAGECODE', 'NDCPACKAGECODE', 'MARKETINGCATEGORYNAME']].to_csv('result.csv')


# In[10]:

df[['11NDCPACKAGECODE', 'NDCPACKAGECODE']].drop_duplicates().ix[df[['NDCPACKAGECODE']].drop_duplicates().index - df[['11NDCPACKAGECODE']].drop_duplicates().index]


# In[137]:

df[df['NDCPACKAGECODE']=='49799-001-01']


# In[138]:

df[df['11NDCPACKAGECODE']=='49799-0001-01']


# In[1]:

5^10


# In[ ]:



