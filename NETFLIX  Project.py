#!/usr/bin/env python
# coding: utf-8

# # Q:1

# # read_csv()

# In[1]:


import pandas as pd 
df = pd.read_csv('NETFLIX Capstone Project.csv')
df


# # info()

# In[2]:


import pandas as pd 
df = pd.read_csv('NETFLIX Capstone Project.csv')
df.info()


# # Q:2

# # isnull()

# In[3]:


import pandas as pd 

df = pd.read_csv('NETFLIX Capstone Project.csv')

missing_values = df.isnull().sum()

print("Number of missing values in each column:")

print(missing_values)


# # Q:3

# In[4]:


import pandas as pd
df =pd.read_csv('NETFLIX Capstone Project.csv')
df.describe()


# # Q:4

# # select_dtype()

# In[5]:


import pandas as pd
df =pd.read_csv('NETFLIX Capstone Project.csv')
categorical = df.select_dtypes(include=['object','category']).columns
categorical


# # Q:5

# In[6]:


import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

Netflix_dataset = pd.read_csv('NETFLIX Capstone Project.csv')

plt.figure(figsize=(14,6))

sns.countplot(data=Netflix_dataset)
plt.title('NETFLIX DATA SET')
plt.xlabel('Count')


# # Q:6

# In[7]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Netflix_dataset = pd.read_csv('NETFLIX Capstone Project.csv')

plt.figure(figsize=(10, 6))

sns.histplot(Netflix_dataset['Runtime'], bins=10, kde=True)

plt.title('Distribution of Runtime')
plt.xlabel('Runtime')
plt.ylabel('Frequency')


# # Q:7

# In[8]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Netflix_dataset = pd.read_csv('NETFLIX Capstone Project.csv')
plt.figure(figsize=(10, 6))

sns.scatterplot(x='Runtime', y='IMDb Score', data=Netflix_dataset)

plt.title('Relationship between Runtime and IMDb Score')
plt.xlabel('Runtime')
plt.ylabel('IMDb Score')


# # Q:8

# # Box plot

# In[9]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

Netflix_dataset = pd.read_csv('NETFLIX Capstone Project.csv')

plt.figure(figsize=(13, 4))

sns.boxplot(x='IMDb Votes', y='Runtime', data= Netflix_dataset, color='skyblue')

plt.title('IMDb Votes and Runtime')
plt.xlabel('IMDb Votes')
plt.ylabel('Runtime')


# # Q:9

# # Bar plot

# In[10]:


import seaborn as sns
import matplotlib.pyplot as plt

Netflix_dataset = pd.read_csv('NETFLIX Capstone Project.csv')

plt.figure(figsize=(10, 4))

sns.barplot(x='IMDb Votes', y='Runtime', data= Netflix_dataset, color='skyblue')

plt.title('IMDb Votes and Runtime')
plt.xlabel('IMDb Votes')
plt.ylabel('Runtime')

plt.show()


# # Q:10

# In[11]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

Netflix_dataset = pd.read_csv('NETFLIX Capstone Project.csv')

plt.figure(figsize=(10, 4))

sns.countplot(x = "Awards Received", data = Netflix_dataset)  

plt.figure(figsize=(20, 4))

sns.histplot(x = "View Rating" , data = Netflix_dataset) 

plt.show()



# In[ ]:




