#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Mini Project: E-commerce Data Visualization Dashboard
#Project Tasks
#Load & Clean the Data


# In[6]:


import pandas as pd

df = pd.read_csv("ecommerce_data.csv")

# Fix dates
df["Date"] = pd.to_datetime(df["Date"])

# Handle missing values
df["Sales"] = df["Sales"].ffill()
df["Profit"] = df["Profit"].fillna(0)

# Confirm clean
df.info()



# In[7]:


#Sales Line Chart (Over Time)
#Goal: Show how sales change daily/monthly
import matplotlib.pyplot as plt

sales_trend = df.groupby("Date")["Sales"].sum()

plt.figure(figsize=(12,5))
plt.plot(sales_trend.index, sales_trend.values)
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()


# In[8]:


#Profit Bar Chart (By Category)
#Goal: Which product category is most profitable?
profit_by_category = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
plt.bar(profit_by_category.index, profit_by_category.values)
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.show()


# In[11]:


#Customer Distribution Pie Chart (By Payment Method)
#Goal: Which payment method is most used?


# In[13]:


payment_counts = df["Payment_Method"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(payment_counts, labels=payment_counts.index, autopct="%1.1f%%")
plt.title("Customer Distribution by Payment Method")
plt.show()


# In[14]:


#Correlation Heatmap (Sales, Profit, Quantity)
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(6,4))
numeric_cols = df[["Sales", "Profit", "Quantity"]]

corr = numeric_cols.corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# In[15]:


#Monthly Aggregation
#Convert date if needed
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month


# In[16]:


#Group by month
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(8,4))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()


# In[17]:


#Top 10 Customers by Sales
top_customers = df.groupby("Customer_ID")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,4))
plt.bar(top_customers.index.astype(str), top_customers.values)
plt.title("Top 10 Customers by Sales")
plt.xlabel("Customer ID")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()


# In[18]:


#Category-wise Monthly Sales
category_month = df.groupby(["Month", "Category"])["Sales"].sum().unstack()

plt.figure(figsize=(10,6))
category_month.plot(kind="line", marker="o", figsize=(10,6))

plt.title("Category-wise Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()


# In[19]:


#If you want the plot outside the pandas plot
plt.figure(figsize=(10,6))
for col in category_month.columns:
    plt.plot(category_month.index, category_month[col], marker="o", label=col)

plt.title("Category-wise Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:


## Summary of Insights

1. **Sales Trend:** Shows how total sales change each month — useful for identifying peak periods.
2. **Profit by Category:** Identifies which product categories generate the most profit.
3. **Payment Method Distribution:** Shows customer preferences, helping target marketing or payment options.

