#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# ## Mage Duel!
# 
# Let's use what we've learned to play a mage duel!
# 
# Imagine your wizard has 6d4 health points and you have spells that do 6d4 damage. "6d4" means rolling six 4-sided dice and summing the result.
# 
# Your opposing mage has 4d6 health points and spells that do 4d6. "4d6" means rolling four six-sided dice and summing the result.

# ## Exercises
# 
# Simulate mage duels to answer who is the more powerful mage?

# ## Exercise 1
# 
# Before running simulations, do you have a hypothesis of which mage will win? Do you have a hunch? Write it down.
# 
# ### I believe 4d6 mage guy will win because umm infinite series

# ## Exercise 2 
# Simulate 10 mage duels. Is there a clear winner? Run that 10 duel simulation again. Was the answer similar?

# In[2]:


def pwrful_mage(n_duels):
    mage_4d6_dmg = np.random.choice(list(range(1, 7)), size = (n_duels, 4))
    mage_6d4_dmg = np.random.choice(list(range(1, 5)), size = (n_duels, 6))
    mage_4d6_health = np.random.choice(list(range(1, 7)), size = (n_duels, 4))
    mage_6d4_health = np.random.choice(list(range(1, 5)), size = (n_duels, 6))
    R4_D6 = pd.DataFrame([mage_4d6_dmg, mage_4d6_health])
    R6_D4 = pd.DataFrame([mage_6d4_dmg, mage_6d4_health])
    R4_dmg['damage'] = R4_dmg.sum(axis = 1)
    R4_hrts['health_points'] = R4_hrts.sum(axis = 1)
    R6_dmg['damage'] = R6_dmg.sum(axis = 1)
    R6_hrts['health_points'] = R6_hrts.sum(axis = 1)
    duels = pd.DataFrame(data = {'R4_dmg': R4_dmg.damage,
                     'R4_hrts': R4_hrts.health_points,
                     'R6_dmg': R6_dmg.damage,
                     'R6_hrts': R6_hrts.health_points})


# In[3]:


n_duels = 10
mage_4d6_dmg = np.random.choice(list(range(1, 7)), size = (n_duels, 4))
mage_6d4_dmg = np.random.choice(list(range(1, 5)), size = (n_duels, 6))
mage_4d6_health = np.random.choice(list(range(1, 7)), size = (n_duels, 4))
mage_6d4_health = np.random.choice(list(range(1, 5)), size = (n_duels, 6))
R4_dmg = pd.DataFrame(mage_4d6_dmg)
R6_dmg = pd.DataFrame(mage_6d4_dmg)
R4_hrts = pd.DataFrame(mage_6d4_health)
R6_hrts = pd.DataFrame(mage_6d4_health)


# In[4]:


R4_dmg['damage'] = R4_dmg.sum(axis = 1)
R4_hrts['health_points'] = R4_hrts.sum(axis = 1)
R6_dmg['damage'] = R6_dmg.sum(axis = 1)
R6_hrts['health_points'] = R6_hrts.sum(axis = 1)


# In[5]:


duels = pd.DataFrame(data = {'R4_dmg': R4_dmg.damage,
                     'R4_hrts': R4_hrts.health_points,
                     'R6_dmg': R6_dmg.damage,
                     'R6_hrts': R6_hrts.health_points})


# In[6]:


duels


# ## Exercise 3
# Do the results change much at 100 duels?

# In[ ]:





# In[ ]:





# ## Exercise 4
# Now, simulate 10,000 mage duels. Is there a clear winner?

# In[ ]:





# In[ ]:




