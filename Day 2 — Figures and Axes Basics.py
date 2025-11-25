#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Objectives

Today you will learn:

What a Figure is

What an Axes is

How to create multiple plots

How to style each subplot

How to plot sin(x) and cos(x) separately


# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[3]:


#Create Data for sin(x) and cos(x)
x = np.linspace(0, 10, 100)
sin_y = np.sin(x)
cos_y = np.cos(x)


# In[9]:


#One Figure, Two Subplots
plt.figure(figsize=(10, 4))

# Subplot 1
plt.subplot(1, 2, 1)   # (rows, columns, position)
plt.plot(x, sin_y)
plt.title("sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")

# Subplot 2
plt.subplot(1, 2, 2)
plt.plot(x, cos_y, color="red",linestyle='--')
plt.title("cos(x)")
plt.xlabel("x")
plt.ylabel("cos(x)")

plt.tight_layout()
plt.show()


# In[6]:


#Using Axes Objects (More Modern Method)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# Left plot
ax[0].plot(x, sin_y)
ax[0].set_title("sin(x)")
ax[0].set_xlabel("x")
ax[0].set_ylabel("sin(x)")

# Right plot
ax[1].plot(x, cos_y)
ax[1].set_title("cos(x)")
ax[1].set_xlabel("x")
ax[1].set_ylabel("cos(x)")

plt.show()


# In[7]:


#Adding Styles to Each Subplot
fig, ax = plt.subplots(2, 1, figsize=(6, 8))

ax[0].plot(x, sin_y, linestyle="--", marker="o")
ax[0].set_title("Styled sin(x)")

ax[1].plot(x, cos_y, linestyle="-.", marker="s", color="green")
ax[1].set_title("Styled cos(x)")

plt.tight_layout()
plt.show()


# In[ ]:




