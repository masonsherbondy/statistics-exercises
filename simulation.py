#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd


# Exercise 1. How likely is it that you roll doubles when rolling two dice?

# In[9]:


die1 = np.random.choice([1, 2, 3, 4, 5, 6], 1_000_000)
die2 = np.random.choice([1, 2, 3, 4, 5, 6], 1_000_000)


# In[10]:


doubles = die1 == die2
doubles


# In[11]:


doubles.mean()
#there is a 17% chance that you will roll doubles when rolling 2 dice


# Exercise 2. If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

# In[25]:


n_trials = 1_000_000
n_coins = 8

coins = np.random.choice([0, 1], size = (n_trials, n_coins)) 
coins = pd.DataFrame(coins)


# In[26]:


coins.shape


# In[27]:


coins.head()


# In[28]:


coins['heads'] = coins.sum(axis = 1)


# In[29]:


coins.head()


# In[113]:


(coins.heads == 3).mean()
#there is a 22% probability you will get exactly 3 heads when you flip 8 coins


# In[114]:


(coins.heads > 3).mean()
#there is a 64% probability you will get more than 3 heads when you flip 8 coins


# Exercise 3. 
# There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

# In[45]:


n_trials = 1_000_000
n_picks = 2

picks = np.random.choice([0, 1], p = [(3/4), (1/4)], size = (n_trials, n_picks))
picks = pd.DataFrame(picks)
picks


# In[46]:


picks.sum(axis = 1) == 2


# In[47]:


picks[picks.sum(axis = 1) == 2]


# In[48]:


picks[picks.sum(axis = 1) == 2].shape[0] / n_trials


# In[49]:


picks['codeup'] = picks.sum(axis = 1)


# In[50]:


picks.head()


# In[118]:


ds_prob = (picks.codeup == 2).mean()
odds = ds_prob / (1 - ds_prob)
1 / odds
#the odds are 1 to 15 that both billboards will feature data science students


# Exercise 4. Codeup students buy, on average, 3 poptart packages with a standard deviation of 1.5 a day from the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon? (Remember, if you have mean and standard deviation, use the np.random.normal)

# In[64]:


n_days = 5
n_trials = 1_000_000
consumed = np.random.normal(loc = 3, scale = 1.5, size = (n_trials, n_days))
consumed = pd.DataFrame(consumed)
consumed


# In[65]:


consumed['poptarts_consumed'] = consumed.sum(axis = 1)
consumed.head()


# In[67]:


consumed.poptarts_consumed <= 16


# In[68]:


(consumed.poptarts_consumed <= 16).mean()


# Exercise 5. Compare Heights
# 
# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# Since you have means and standard deviations, you can use np.random.normal to generate observations.
# If a man and woman are chosen at random, P(woman taller than man)?

# In[75]:


n_trials = 1_000_000
man = np.random.normal(loc = 178, scale = 8, size = n_trials)
woman = np.random.normal(loc = 170, scale = 6, size = n_trials)
man = pd.DataFrame(man)
woman = pd.DataFrame(woman)
woman


# In[76]:


man


# In[82]:


man[0]


# In[83]:


woman['man'] = man[0]


# In[84]:


woman.head()


# In[88]:


women_taller_than_men = woman[0] > woman['man']
women_taller_than_men.mean()


# Exercise 6. When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?
# 
# What is the probability that we observe an installation issue within the first 150 students that download anaconda?
# 
# How likely is it that 450 students all download anaconda without an issue?

# In[94]:


n_trials = 1_000_000
n_students = 50
no_issues = np.random.choice([0, 1], p = [(249/250), (1/250)], size = (n_trials, n_students))
no_issues = pd.DataFrame(no_issues)


# In[101]:


no_issues.sum(axis = 1) == 0


# In[102]:


(no_issues.sum(axis = 1) == 0).mean()
#There is an 82% chance that there will be no issues if 50 students download anaconda


# In[103]:


n_students = 100
no_issues = np.random.choice([0, 1], p = [(249/250), (1/250)], size = (n_trials, n_students))
no_issues = pd.DataFrame(no_issues)


# In[104]:


(no_issues.sum(axis = 1) == 0).mean()
#There is a 67% chance that there will be no issues if 100 students download anaconda


# In[ ]:


n_students = 150
no_issues = np.random.choice([0, 1], p = [(249/250), (1/250)], size = (n_trials, n_students))
no_issues = pd.DataFrame(no_issues)


# In[105]:


(no_issues.sum(axis = 1) > 0).mean()
#there is a 33 percent probability that there will be an issue within the first 150 downloads


# In[107]:


n_students = 450
no_issues = np.random.choice([0, 1], p = [(249/250), (1/250)], size = (n_trials, n_students))
no_issues = pd.DataFrame(no_issues)


# In[108]:


(no_issues.sum(axis = 1) == 0).mean()
#there is a 16% chance there will be no issues if 450 students download anaconda


# Exercise 7.
# There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?
# 
# How likely is it that a food truck will show up sometime this week?

# In[110]:


n_trials = 1_000_000
n_days = 3
food_truck = np.random.choice([0, 1], p = [(3/10), (7/10)], size = (n_trials, n_days))
food_truck = pd.DataFrame(food_truck)
food_truck


# In[111]:


(food_truck.sum(axis = 1) == 0).mean()
#you have a 3% chance of seeing no food trucks in Travis park in 3 days


# In[ ]:


n_trials = 1_000_000
n_days = 7
food_truck = np.random.choice([0, 1], p = [(3/10), (7/10)], size = (n_trials, n_days))
food_truck = pd.DataFrame(food_truck)
food_truck


# In[112]:


(food_truck.sum(axis = 1) > 0).mean()
#There is a 97% chance that a food truck will show up sometime this week


# Exercise 8. If 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?

# In[ ]:




