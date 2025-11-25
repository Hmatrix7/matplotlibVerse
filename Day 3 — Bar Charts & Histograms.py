#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Objectives

By the end of today, you will be able to:

Create vertical and horizontal bar charts

Customize bar appearance

Add labels and colors

Understand and plot histograms

Change number of bins in histograms


# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[5]:


#Vertical Bar Chart
#Example: Sales of products A–E
products=["A","B","C","D","E"]
sales=[300,450,150,500,250]
plt.bar(products,sales)


# In[6]:


products = ["A", "B", "C", "D", "E"]
sales = [300, 450, 150, 500, 250]

plt.bar(products, sales)
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()


# In[7]:


#Horizontal Bar Chart
plt.barh(products, sales)
plt.title("Product Sales (Horizontal)")
plt.xlabel("Sales")
plt.ylabel("Products")
plt.show()


# In[10]:


#plt.bar(products, sales, color="orange", edgecolor="black")
plt.bar(products, sales, color="orange", edgecolor="black")

plt.title("Styled Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.grid(axis="y", linestyle="--", alpha=0.9)

plt.show()




# In[11]:


#Adding Bar Labels
bars = plt.bar(products, sales, color="skyblue")

for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 10,
             bar.get_height(),
             ha="center")

plt.title("Sales with Labels")
plt.show()


# In[ ]:


get_ipython().run_line_magic('pinfo', 'histogram')

A histogram shows distribution of numerical data by grouping it into bins.

Good for:

age distributions

exam scores

random data

frequencies


# In[16]:


#Basic Histogram
data = np.random.randn(200)

plt.hist(data,edgecolor="black")
plt.title("Histogram of Random Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# In[17]:


#Histogram with More Bins
plt.hist(data, bins=20, edgecolor="black")
plt.title("Histogram with 20 Bins")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# In[18]:


#Styled Histogram
plt.hist(data, bins=15, edgecolor="black")
plt.title("Styled Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()


# In[ ]:




