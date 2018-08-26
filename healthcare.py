
# coding: utf-8

# In[2]:

# Import Dependencies
import csv
import pandas as pd
import numpy as np
from collections import defaultdict
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[ ]:

csv_filename="DATA/DiabetesData.csv"
df = pd.read_csv(csv_filename).as_module


# In[ ]:

df = pd.read_csv('C:\\DATA/DiabetesTestData.csv').as_module


# In[ ]:

df.head()


# In[ ]:

data = df.fillna(method='ffill')


# In[ ]:

data.head()


# In[3]:

list(data)


# In[ ]:

disease_list = []
disease_symptom_dict = defaultdict(list)
disease_symptom_count = {}
count = 0

for idx, row in data.iterrows():


# In[ ]:

disease_symptom_dict


# In[ ]:

disease_symptom_count


# In[4]:

df1 = pd.DataFrame(list(disease_symptom_dict.items()), columns=['Disease','Symptom'])


# In[ ]:


df1.head()


# In[ ]:

for vals in disease_symptom_count.items():
    print(vals[1])


# In[5]:

df1.head()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



