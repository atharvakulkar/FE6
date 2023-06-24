#!/usr/bin/env python
# coding: utf-8

# # Q1. Pearson correlation coefficient is a measure of the linear relationship between two variables. Suppose you have collected data on the amount of time students spend studying for an exam and their final exam scores. Calculate the Pearson correlation coefficient between these two variables and interpret the result.

# In[2]:


import pandas as pd
df = pd.DataFrame({
    'Time_Studied': [4,3,5,7,6],
    'Marks_Obtained': [60 ,45, 70, 90, 83]
})


# In[3]:


df


# ![image.png](attachment:image.png)

# In[4]:


df.corr(method='pearson')


# In[ ]:




Q2. Spearman's rank correlation is a measure of the monotonic relationship between two variables. Suppose you have collected data on the amount of sleep individuals get each night and their overall job satisfaction level on a scale of 1 to 10. Calculate the Spearman's rank correlation between these two variables and interpret the result.
# In[8]:


df = pd.DataFrame({
    'Sleep_Amount': [6, 7, 5, 8, 7, 6, 5, 9, 8, 7],
    'Job_Satisfaction': [8, 9, 4, 7, 6, 5, 3, 10, 9, 8]
})


# In[6]:


df


# ![image.png](attachment:image.png)

# In[9]:


df['Sleep_Amount'].corr(df['Job_Satisfaction'], method='spearman')


# In[10]:


df.corr(method='spearman')


# # Q3. Suppose you are conducting a study to examine the relationship between the number of hours of exercise per week and body mass index (BMI) in a sample of adults. You collected data on both variables for 50 participants. Calculate the Pearson correlation coefficient and the Spearman's rank correlation between these two variables and compare the results.
To calculate the Pearson correlation coefficient and the Spearman's rank correlation between the number of hours of exercise per week and body mass index (BMI) in a sample of 50 adults, we need to have data for both variables.

We can use Python to generate random data for both variables and then calculate the Pearson and Spearman's rank correlation between them:
# In[12]:


import numpy as np
num_of_hours = np.random.normal(5, 2, 50)
bmi = np.random.normal(25, 5, 50)
df = pd.DataFrame({
    'num_of_hours': num_of_hours,
    'bmi': bmi
})
df.head()


# In[13]:


df.corr(method='pearson')


# In[14]:


df.corr(method='spearman')


# Results Comparison:
# 
# The Pearson correlation coefficient measures the linear relationship between two variables, and it ranges from -1 (perfect negative correlation) to +1 (perfect positive correlation), with 0 indicating no correlation. In this case, the Pearson correlation coefficient between num_of_hours and bmi is 0.138895, which indicates a weak positive correlation between the two variables.
# 
# On the other hand, the Spearman correlation coefficient measures the monotonic relationship between two variables, which means it assesses the strength and direction of a relationship between two variables, without assuming any particular functional form of the relationship. It also ranges from -1 to +1, with 0 indicating no correlation. In this case, the Spearman correlation coefficient between num_of_hours and bmi is 0.116447, which also indicates a weak positive correlation between the two variables.

# In[ ]:




Q4. A researcher is interested in examining the relationship between the number of hours individuals spend watching television per day and their level of physical activity. The researcher collected data on both variables from a sample of 50 participants. Calculate the Pearson correlation coefficient between these two variables.

To calculate the Pearson correlation coefficient between the number of hours individuals spend watching television per day and their level of physical activity of hours of exercise per week in a sample of 50 pariticipants, we need to have data for both variables.

We can use Python to generate random data for both variables and then calculate the Pearson correlation coeffiecients:
# In[15]:


num_of_hours = np.random.normal(6, 4, 50)
amount_of_activity= np.random.normal(10, 6, 50)
df = pd.DataFrame({
    'num_of_hours': num_of_hours,
    'physical_activity': amount_of_activity
})
df.head()


# In[16]:


df.corr(method='pearson')


# # Q5. A survey was conducted to examine the relationship between age and preference for a particular brand of soft drink. The survey results are shown below:

# ![image.png](attachment:image.png)

# In[17]:


df = pd.DataFrame({
    "Age(Years)": [25, 42, 37, 19, 31, 28],
    "Soft Drink Preference": ['Coke', 'Pepsi', 'Mountain Dew', 'Coke', 'Pepsi', 'Coke']
})


# In[19]:


df


# In[20]:


from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
encoded_col = encoder.fit_transform(df['Soft Drink Preference'])
df_encoded = pd.DataFrame(encoded_col, columns=['Soft Drink Preference Enc'])
df_new = pd.concat([df, df_encoded], axis=1)
df_new = df_new.drop('Soft Drink Preference', axis=1)
df_new


# In[21]:


df_new.corr(method='pearson')


# In[ ]:





# In[ ]:





# Q6. A company is interested in examining the relationship between the number of sales calls made per day and the number of sales made per week. The company collected data on both variables from a sample of 30 sales representatives. Calculate the Pearson correlation coefficient between these two variables.

# In[22]:


num_of_calls = [20, 30, 10, 40, 60, 80, 60, 50, 40, 100]
num_of_sales = [2, 3, 2, 5, 5, 6, 8, 5, 7, 20]
df = pd.DataFrame({
    'num_of_calls': num_of_calls,
    'num_of_sales': num_of_sales
})
df


# In[24]:


df.corr(method='pearson')


# In[25]:


df.corr(method='spearman')


# In[ ]:




