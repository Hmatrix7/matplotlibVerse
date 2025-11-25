#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Objectives

By the end of today, you will be able to:

Create scatter plots (with size, color, transparency)

Create pie charts (with labels, explode, percentages)

Style both charts professionally


# In[1]:


#SCATTER PLOTS
#Scatter plots are used to visualize the relationship between two numeric variables.
#STEP 1 — Basic Scatter Plot
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1, 50, 50)
y = np.random.randint(1, 50, 50)

plt.scatter(x, y)
plt.title("Basic Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()


# In[2]:


#Scatter Plot with Color and Size
sizes = np.random.randint(20, 200, 50)
colors = np.random.rand(50)

plt.scatter(x, y, s=sizes, c=colors, alpha=0.7)
plt.title("Styled Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.colorbar(label="Color Scale")

plt.show()


# In[3]:


#Scatter Plot with Trend Line
plt.scatter(x, y)

# Trend line
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, linestyle='--')

plt.title("Scatter Plot with Trend Line")
plt.show()


# In[4]:


#PIE CHARTS
#Pie charts are used to show proportional distribution of categories.
#STEP 4 — Basic Pie Chart
labels = ["Rent", "Food", "Transport", "Entertainment"]
sizes = [40, 25, 20, 15]

plt.pie(sizes, labels=labels)
plt.title("Monthly Expenses")
plt.show()


# In[5]:


#Pie Chart with autopct & explode
explode = [0.1, 0, 0, 0]  # explode only the first slice

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    explode=explode,
    shadow=True
)

plt.title("Monthly Expenses (Detailed)")
plt.show()


# In[6]:


#Pie Chart with Start Angle
plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Pie Chart with Start Angle")
plt.show()


# In[ ]:




