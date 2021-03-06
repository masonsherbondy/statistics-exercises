#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd


# ## Exercise 1
# How likely is it that you roll doubles when rolling two dice?

# In[2]:


die1 = np.random.choice([1, 2, 3, 4, 5, 6], 1_000_000)
die2 = np.random.choice([1, 2, 3, 4, 5, 6], 1_000_000)


# In[3]:


doubles = die1 == die2
doubles


# In[4]:


doubles.mean()
#there is a 17% chance that you will roll doubles when rolling 2 dice


# ## global variable n_trials

# In[5]:


n_trials = 1_000_000


# ## Exercise 2
# If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

# In[6]:


n_coins = 8

coins = np.random.choice([0, 1], size = (n_trials, n_coins)) 
coins = pd.DataFrame(coins)


# In[7]:


coins.shape


# In[8]:


coins.head()


# In[9]:


coins['heads'] = coins.sum(axis = 1)


# In[10]:


coins.head()


# In[11]:


(coins.heads == 3).mean()
#there is a 22% probability you will get exactly 3 heads when you flip 8 coins


# In[12]:


(coins.heads > 3).mean()
#there is a 64% probability you will get more than 3 heads when you flip 8 coins


# ## Exercise 3
# There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

# In[13]:


n_picks = 2

picks = np.random.choice([0, 1], p = [(3/4), (1/4)], size = (n_trials, n_picks))
picks = pd.DataFrame(picks)
picks


# In[14]:


picks.sum(axis = 1) == 2


# In[15]:


picks[picks.sum(axis = 1) == 2]


# In[16]:


picks[picks.sum(axis = 1) == 2].shape[0] / n_trials
#there is a 6% chance that both billboards feature a data scientist alumni


# In[17]:


#alternatively
picks['codeup'] = picks.sum(axis = 1)


# In[18]:


picks.head()


# In[19]:


ds_prob = (picks.codeup == 2).mean()
odds = ds_prob / (1 - ds_prob)
1 / odds
#the odds are about 1 to 15 that both billboards will feature data science students


# ## Exercise 4
# Codeup students buy, on average, 3 poptart packages with a standard deviation of 1.5 a day from the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon? (Remember, if you have mean and standard deviation, use the np.random.normal)

# In[20]:


n_days = 5
consumed = np.random.normal(loc = 3, scale = 1.5, size = (n_trials, n_days)).astype(int)
consumed = pd.DataFrame(consumed)
consumed


# In[21]:


consumed['poptarts_consumed'] = consumed.sum(axis = 1)
consumed.head()


# In[22]:


consumed.poptarts_consumed <= 16


# In[23]:


(consumed.poptarts_consumed <= 16).mean()
#there is an 88% chance you will be able to buy poptarts on a Friday afternoon


# ## Exercise 5 Compare Heights
# 
# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# Since you have means and standard deviations, you can use np.random.normal to generate observations.
# If a man and woman are chosen at random, P(woman taller than man)?

# In[24]:


man = np.random.normal(loc = 178, scale = 8, size = n_trials)
woman = np.random.normal(loc = 170, scale = 6, size = n_trials)
man = pd.DataFrame(man)
woman = pd.DataFrame(woman)
woman


# In[25]:


man


# In[26]:


man[0]


# In[27]:


woman['man'] = man[0]


# In[28]:


woman.head()


# In[29]:


women_taller_than_men = woman[0] > woman['man']
women_taller_than_men.mean()
#There is a 21% that a woman is taller than a man when both are chosen at random


# ## Exercise 6
# When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?
# 
# What is the probability that we observe an installation issue within the first 150 students that download anaconda?
# 
# How likely is it that 450 students all download anaconda without an issue?

# In[30]:


n_students = 50
no_issues = np.random.choice([0, 1], p = [(249/250), (1/250)], size = (n_trials, n_students))
no_issues = pd.DataFrame(no_issues)


# In[31]:


no_issues.sum(axis = 1) == 0


# In[32]:


issue_rate = (no_issues.sum(axis = 1) == 0).mean()
#There is an 82% chance that there will be no issues if 50 students download anaconda
odds = issue_rate / (1 - issue_rate)
odds
#the odds that there will be no issues are about 9 to 2


# In[33]:


n_students = 100
no_issues = np.random.choice([0, 1], p = [(249/250), (1/250)], size = (n_trials, n_students))
no_issues = pd.DataFrame(no_issues)


# In[34]:


issue_rate = (no_issues.sum(axis = 1) == 0).mean()
#There is a 67% chance that there will be no issues if 100 students download anaconda
odds = issue_rate / (1 - issue_rate)
odds
#the odds that there will be no issues in 100 downloads are about 2 to 1


# In[35]:


n_students = 150
no_issues = np.random.choice([0, 1], p = [(249/250), (1/250)], size = (n_trials, n_students))
no_issues = pd.DataFrame(no_issues)


# In[36]:


(no_issues.sum(axis = 1) > 0).mean()
#there is a 45 percent probability that there will be an issue within the first 150 downloads


# In[37]:


n_students = 450
no_issues = np.random.choice([0, 1], p = [(249/250), (1/250)], size = (n_trials, n_students))
no_issues = pd.DataFrame(no_issues)


# In[38]:


(no_issues.sum(axis = 1) == 0).mean()
#there is a 17% chance there will be no issues if 450 students download anaconda


# ## Exercise 7
# There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?
# 
# How likely is it that a food truck will show up sometime this week?

# In[39]:


n_days = 3
food_truck = np.random.choice([0, 1], p = [(3/10), (7/10)], size = (n_trials, n_days))
food_truck = pd.DataFrame(food_truck)
food_truck


# In[40]:


(food_truck.sum(axis = 1) == 0).mean()
#you have a 3% chance of seeing no food trucks in Travis park in 3 days


# In[41]:


n_days = 7
food_truck = np.random.choice([0, 1], p = [(3/10), (7/10)], size = (n_trials, n_days))
food_truck = pd.DataFrame(food_truck)
food_truck


# In[42]:


(food_truck.sum(axis = 1) > 0).mean()
#There is a 100% chance that a food truck will show up sometime this week


# ## Exercise 8
# If 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?

# In[43]:


n_peeps = 23
birthdays = np.random.choice(list(range(366)), size = (n_trials, n_peeps))
birthdays = pd.DataFrame(birthdays)
birthdays


# In[44]:


birthdays.nunique(axis = 1) < 23


# In[45]:


(birthdays.nunique(axis = 1) < 23).mean()
#there is a 51% chance of finding 2 people with the same birthday in the same room of 23 people 
#the odds that 2 people in the same room of 23 people share a birthday are 51 to 49 (about 1 to 1)


# In[46]:


n_peeps = 20
birthdays = np.random.choice(list(range(366)), size = (n_trials, n_peeps))
birthdays = pd.DataFrame(birthdays)


# In[47]:


(birthdays.nunique(axis = 1) < 20).mean()
#the odds that 2 people in the same room of 20 people share a birthday are 41 to 59 (about 2 to 3)


# In[48]:


n_peeps = 40
birthdays = np.random.choice(list(range(366)), size = (n_trials, n_peeps))
birthdays = pd.DataFrame(birthdays)


# In[49]:


(birthdays.nunique(axis = 1) < 40).mean()
#the odds that 2 people in the same room of 40 people share a birthday are 89 to 11 (about 9 to 1)

