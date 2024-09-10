# 📝 Programming Assignment 3: Python Data Analysis
#### This GitHub repository contains two engaging problems designed to enhance your skills in Python data analysis. Each problem focuses on real-world scenarios, encouraging users to apply their knowledge in subsetting, slicing, and indexing of data structures using practical library such as ```Pandas```. 

## 📚 About Pandas
Python Data Analyis (```Pandas```) is a powerful and flexible open-source data analysis and manipulation library for Python, widely used in data science and analytics. It provides essential tools for handling structured data, particularly in tabular formats like ```CSV``` files and Excel spreadsheets. It is particularly valued for its ability to handle large datasets efficiently, making it a critical tool for data analysts and scientists across various domains, including finance, healthcare, and social sciences. 
### ✨ Why Pandas? 
> ###### 🔹 Efficiently handles large datasets.
> ###### 🔹 Critical for solving computational problems and optimizing algorithms.
> ###### 🔹 Widely used in fields such as finance, healthcare, and social sciences.

## 📑 Description of the Given Problems
### 1️⃣ PONCE_Pandas-P1
Applying python data structures on this code, the goal is to be able to write a code that loads an existing file, in this instance: a ```CSV``` file, into a data frame that then it could print. The code should then be able to display the first and last five rows of the ```CSV``` file list using a function of ```pandas```.

> ##### 🎯 **Write a code that can load a file then print it.**
> ###### ✅ *Load the corresponding ```.csv``` file into a data frame named ```cars``` using ```pandas.```*
> ###### ✅ *Display the first five and last five rows of the resulting ```cars.```*

#### 💻 Code
###### *Below shows the code that loads and prints the ```CSV``` file into a data structure:*
```Ruby
# Used to access pandas library
import pandas as pd

# Assigns function as JDM and it loads the file. It then prints the data structure
JDM = pd.read_csv('cars.csv')
JDM
```
```Ruby
# Extracts and displays the first five rows of the list
JDM.head()
```
```Ruby
# Extracts and displays the last five rows of the list
JDM.tail()
```
### 2️⃣ PONCE_Pandas-P2
Another important data structure of ```pandas``` is subsetting, slicing, and indexing. Subsetting refers to the process of selecting a subset of rows and/or columns from a DataFrame or Series. It allows you to extract specific parts of the data based on certain criteria. Slicing is used to select a range of rows or columns from a DataFrame or Series. It allows you to extract a subset of data based on the row or column position. Indexing refers to the way data is labeled and referenced within a DataFrame or Series. Indexing allows you to select data based on these labels. 

> ##### 🎯 **Write a code that can perfrom these data structures given certain conditions.** 
> ###### ✅ *Display the first five rows with odd-numbered columns (```columns 1, 3, 5, 7...```) of ```cars.```*
> ###### ✅ *Display the row that contains the ```‘Model’``` of ```‘Mazda RX4’```.*
> ###### ✅ *Display the number of cylinders (```‘cyl’```) does the car ```model``` ```‘Camaro Z28’``` have.*
> ###### ✅ *Display the number of cylinders (```‘cyl’```) and what gear type (```‘gear’```) do the car ```models``` ```‘Mazda RX4 Wag’```, ```‘Ford Pantera L’``` and ```‘Honda Civic’``` have.*

#### 💻 Code
###### *Below shows the code for subsetting, splicing, and indexing:*
```Ruby
# Extracts and displays the first five rows with odd-numbered columns
JDM.iloc[[1,3,5,7,9]]
```
```Ruby
# Extracts and displays the entire row that contains the model of 'Mazda RX4'
JDM.loc[JDM['Model'] == 'Mazda RX4'] 
```
```Ruby
# Displays only the number of cylinder of the model car 'Camaro Z28'
JDM.loc[JDM['Model'] == 'Camaro Z28', ['Model', 'cyl']]
```
```Ruby
# Displays the number of cylinder and gear type of car models 'Mazda RX4 Wag', ‘Ford Pantera L’, and ‘Honda Civic’
JDM.loc[[1, 18, 28], ['Model', 'cyl', 'gear']]
```

## 👨‍💻 Author
#### *Zildjan Zatyr C. Ponce* 
##### *2ECE - A*

