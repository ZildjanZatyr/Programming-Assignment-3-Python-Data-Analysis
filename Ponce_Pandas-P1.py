#!/usr/bin/env python
# coding: utf-8

# # Experiment 3: Python Data Analysis (Part 1)
# ### Pandas Problem 1
# ##### *Load the corresponding .csv file into a data frame named cars using pandas and display the first five and last five rows of the resulting ```cars```.*

# In[7]:


# Used to access pandas library
import pandas as pd

# Assigns function as JDM and it loads the file. It then prints the data structure
JDM = pd.read_csv('cars.csv')
JDM


# In[9]:


# Extracts and displays the first five rows of the list
JDM.head()


# In[11]:


# Extracts and displays the last five rows of the list
JDM.tail()

