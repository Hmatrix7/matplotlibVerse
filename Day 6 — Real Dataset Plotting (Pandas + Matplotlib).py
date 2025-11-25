#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Real Dataset Plotting (Pandas + Matplotlib)
Objectives

By the end of today, you will be able to:

Load datasets using pandas

Plot DataFrame columns directly

Plot line, bar, and scatter using real data

Handle missing values

Plot date-time data

Combine pandas + Matplotlib styling


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df = pd.read_csv("day6_big_ecommerce_dataset.csv")


# In[4]:


#small e-commerce dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [1200, 1500, 1600, 1800, 1700, 2000],
    "Profit": [200, 250, 300, 350, 320, 400],
    "Quantity": [50, 60, 70, 65, 68, 80]
}

df = pd.DataFrame(data)
df


# In[5]:


#LINE PLOT (Sales Over Months)
plt.figure(figsize=(10, 5))
plt.plot(df["Month"], df["Sales"], marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.show()


# In[6]:


#BAR PLOT (Profit by Month)
plt.figure(figsize=(10, 5))
plt.bar(df["Month"], df["Profit"], color="orange")

plt.title("Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid(axis="y", alpha=0.5)

plt.show()


# In[7]:


#SCATTER PLOT (Quantity vs Profit)
plt.scatter(df["Quantity"], df["Profit"], s=110, alpha=0.7)

plt.title("Quantity vs Profit")
plt.xlabel("Quantity Sold")
plt.ylabel("Profit")

plt.grid(True)
plt.show()


# In[8]:


#Handling Missing Values
df.loc[2, "Sales"] = np.nan
df


# In[9]:


#Plot while skipping NaN
df["Sales"].plot()
plt.title("Sales (handles NaN automatically)")
plt.show()


# In[15]:


#Fill missing values
df["Sales"] = df["Sales"].ffill()
#..or 
df["Sales"] = df["Sales"].bfill()


# In[17]:


#Plotting Date-Time Data
#Create a time series
dates = pd.date_range(start="2024-01-01", periods=12, freq="ME")
sales = np.random.randint(1000, 3000, 12)

ts = pd.DataFrame({"Date": dates, "Sales": sales})

plt.plot(ts["Date"], ts["Sales"], marker="o")
plt.xticks(rotation=45)

plt.title("Sales Trend Over the Year")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)

plt.tight_layout()
plt.show()


# In[13]:


#Pandas Built-In Plotting (Fast & Easy)
df.plot(kind="line", x="Month", y="Sales", figsize=(10, 5), marker="o")
plt.title("Monthly Sales (Pandas Plot)")
plt.grid(True)
plt.show()


# In[ ]:




