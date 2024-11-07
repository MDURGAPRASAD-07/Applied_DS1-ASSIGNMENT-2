#!/usr/bin/env python
# coding: utf-8

# In[104]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[105]:


df = pd.read_csv(r"C:\Users\91910\OneDrive\Desktop\weight_change_dataset.csv")
df.head(10)


# In[106]:


print(df.isnull().sum())


# In[107]:


df.describe()


# In[108]:


# Correlation
df.corr()


# In[109]:


print(df['Age'].value_counts())


# In[110]:


df.columns


# In[127]:


# Function to create a histogram
def plot_histogram(data):
    plt.hist(data['Stress_Level'], bins=5, color='orange', edgecolor='black')
    
    # Formatting
    # Add Axis Labels
    plt.title('Participants Stress Level')
    plt.xlabel('Stress level')
    plt.ylabel('Participants')
    plt.show()


# In[128]:


plot_histogram(df)


# In[129]:


#PIE CHART
def plot_pie(data):
    gender_counts = data['Gender'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
    
    # Formatting
    plt.title('Gender Distribution')
    
    # Axis equal sets the axis to look square
    plt.axis('equal')
    plt.show()





# In[130]:


plot_pie(df)


# In[115]:


# Function to create a line graph
def plot_line(data):
    avg_weight_by_age = data.groupby('Age')['Current_Weight'].mean().reset_index()
    #plt.figure(figsize=(10, 6))
    plt.plot(avg_weight_by_age['Age'], avg_weight_by_age['Current_Weight'], marker='o')
    
    # Formatting
    # Add Axis Labels
    plt.title('Average Weight by Age')
    plt.xlabel('Age')
    plt.ylabel('Average Weight')
    plt.grid()
    plt.show()




# In[116]:


plot_line(df)


# In[117]:


# Function to create a Violin Graph
def plot_violin(data):
    plt.figure(figsize=(12, 6))
    sns.violinplot(x='Duration', y='Final_Weight', data=data)
    plt.title('Final Weight By Its Duration')
    #plt.xticks(rotation=45)
    plt.show()




# In[118]:


plot_violin(df)


# In[119]:


# Function to create a heatmap
def plot_heatmap(correlation):
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, fmt=".2f", cmap='RdBu', square=True)
    
    # Formatting
    plt.title('Correlation Heatmap')
    plt.show()




# In[120]:


plot_heatmap(correlation)


# In[ ]:




