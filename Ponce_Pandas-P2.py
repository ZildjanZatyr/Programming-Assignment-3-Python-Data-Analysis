#!/usr/bin/env python
# coding: utf-8

# # Experiment 3: Python Data Analysis (Part 2)
# ### Pandas Problem 2
# ##### *Using the data frame cars in problem 1, extract the following information using subsetting, slicing and indexing operations.*
# ##### *A. Display the first five rows with odd-numbered columns (```columns 1, 3, 5, 7...```) of ```cars```.*

# In[20]:


# Used to access pandas library
import pandas as pd

# Loads the CSV file and displays the first five rows with odd-numbered columns
JDM = pd.read_csv('cars.csv')
JDM.iloc[[1,3,5,7,9]]


# ##### *B. Display the row that contains the ```‘Model’``` of ```‘Mazda RX4’```.*

# In[8]:


# Extracts and displays the entire row that contains the model of 'Mazda RX4'
JDM.loc[JDM['Model'] == 'Mazda RX4'] 


# ##### *C. How many cylinders (```‘cyl’```) does the car model ```‘Camaro Z28’``` have?*

# In[10]:


# Displays only the number of cylinder of the model car 'Camaro Z28'
JDM.loc[JDM['Model'] == 'Camaro Z28', ['Model', 'cyl']]


# ##### *D. Determine how many cylinders (```‘cyl’```) and what gear type (```‘gear’```) do the car models ```‘Mazda RX4  Wag’```, ```‘Ford Pantera L’```, and ```‘Honda Civic’``` have.*

# In[14]:


# Displays the number of cylinder and gear type of car models 'Mazda RX4 Wag', ‘Ford Pantera L’, and ‘Honda Civic’
JDM.loc[[1, 18, 28], ['Model', 'cyl', 'gear']]

