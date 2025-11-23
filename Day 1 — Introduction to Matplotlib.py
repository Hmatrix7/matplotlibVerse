#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install matplotlib')


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import pandas as pd


# In[4]:


import numpy as np


# In[5]:


#Create a Simple Plot
#We will plot the equation:
#y = 2x + 3
x = np.arange(0, 11)    # numbers 0–10
y = 2*x + 3

plt.plot(x, y)
plt.show()


# In[16]:


#Add Title and Labels
plt.plot(x,y, linestyle='--')
plt.xlabel("X values")
plt.ylabel("y values")
plt.title("matplotlib introduction")
plt.grid(True)
plt.show()


# In[10]:


#Add Style (optional)
plt.plot(x, y, marker='o', linestyle='--')
plt.title("Styled Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

plt.show()


# In[17]:


#Save the Plot
plt.savefig("matplotlib day 1")


# In[18]:


plt.plot(x, y)
plt.title("Saved Plot Example")
plt.savefig("day1_plot.png")
plt.show()


# In[ ]:




