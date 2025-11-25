#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Customization & Styling
Objectives

By the end of today, you will be able to:

Change figure size

Add legends

Customize colors

Add grid lines

Format ticks

Add annotations (arrows, highlighted points)

Improve layout using tight_layout()


# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


#Change Figure Size
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y)

plt.title("Custom Figure Size")
plt.show()


# In[3]:


#Add Legends
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")

plt.title("Plot with Legend")
plt.legend()          # show legend
plt.show()


# In[4]:


#Custom Colors and Line Styles
plt.plot(x, np.sin(x), color="red", linestyle="--", linewidth=2)
plt.plot(x, np.cos(x), color="green", linestyle="-.", linewidth=3)

plt.title("Styled Lines")
plt.show()


# In[5]:


#Grid Lines
plt.plot(x, y)
plt.grid(True, linestyle="--", alpha=0.6)
plt.title("Plot with Grid")
plt.show()


# In[6]:


#Custom Tick Marks
plt.plot(x, y)
plt.xticks(np.arange(0, 11, 1))   # custom x ticks
plt.yticks([-1, -0.5, 0, 0.5, 1]) # custom y ticks

plt.title("Custom Ticks")
plt.grid(True, alpha=0.3)
plt.show()


# In[7]:


#Annotations (Very Important Skill)
#Highlight important points.
plt.plot(x, y)
plt.title("Plot with Annotation")

# Annotate maximum point
plt.annotate(
    "Peak here",
    xy=(np.pi/2, 1),
    xytext=(2, 1.2),
    arrowprops=dict(arrowstyle="->")
)

plt.show()


# In[8]:


#Multiple Styling Together
plt.figure(figsize=(10, 6))

plt.plot(x, np.sin(x), label="sin(x)", color="blue", linewidth=2)
plt.plot(x, np.cos(x), label="cos(x)", color="orange", linestyle="--")

plt.grid(True, alpha=0.4)
plt.legend()
plt.title("Clean and Styled Plot")

plt.xlabel("X Values")
plt.ylabel("Function Value")

plt.tight_layout()
plt.show()


# In[ ]:




