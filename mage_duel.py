#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

# In[ ]:


#pwrful_mage defines a single paramater, an integer, and returns print statements with relevant data
#input the number of duels and output duel value counts
def pwrful_mage(n_duels):
    #damage output generator for roll 4 mage
    mage_4d6_dmg = np.random.choice(list(range(1, 7)), size = (n_duels, 4))
    
    #damage output generator for roll 6 mage
    mage_6d4_dmg = np.random.choice(list(range(1, 5)), size = (n_duels, 6))
    
    #health points generator for roll 4 mage
    mage_4d6_health = np.random.choice(list(range(1, 7)), size = (n_duels, 4))
    
    #health points generator for roll 6 mage
    mage_6d4_health = np.random.choice(list(range(1, 5)), size = (n_duels, 6))
    
    #assign a variable name to a dataframe for R4 damage die values
    R4_dmg = pd.DataFrame(mage_4d6_dmg)
    
    #assign a variable name to a dataframe for R6 damage die values
    R6_dmg = pd.DataFrame(mage_6d4_dmg)
    
    #assign a variable name to a dataframe for R4 health die values
    R4_hrts = pd.DataFrame(mage_4d6_health)
    
    #assign a variable name to a dataframe for R6 health die values
    R6_hrts = pd.DataFrame(mage_6d4_health)
    
    #sum up the values of rolling 4 six-sided dice to get damage output
    R4_dmg['damage'] = R4_dmg[:].sum(axis = 1)
    
    #do it again for the health points to get total health
    R4_hrts['health_points'] = R4_hrts[:].sum(axis = 1)
    
    #sum up the values of rolling 6 four-sided dice to get damage output
    R6_dmg['damage'] = R6_dmg[:].sum(axis = 1)
    
    #total health for R6 mage
    R6_hrts['health_points'] = R6_hrts[:].sum(axis = 1)
    
    #assign a variable name for a dataframe with the duel data
    duels = pd.DataFrame(data = {'R4_hrts': R4_hrts.health_points,
                             'R6_hrts': R6_hrts.health_points,
                             'R4_dmg': R4_dmg.damage,
                             'R6_dmg': R6_dmg.damage})
    
    #set counters for mage duel results
    R4_wins = 0
    R6_wins = 0
    draws = 0
    
    #start a for loop to run through each row of the duels dataframe (simulate each duel)
    for n in range(len(duels)):
        
        #start a while loop to simulate attacks while both mages still live (until someone croaks)
        while duels.R4_hrts[n] and duels.R6_hrts[n] > 0:
            
            #deduct health points by damage points (simulate attacks)
            duels.R4_hrts[n] = duels.R4_hrts[n] - duels.R6_dmg[n]
            duels.R6_hrts[n] = duels.R6_hrts[n] - duels.R4_dmg[n]
            
        #if R4 survives, add a victory to R4's tally        
        if duels.R4_hrts[n] > duels.R6_hrts[n] and duels.R4_hrts[n] > 0:
            R4_wins += 1
            
        #if R6 survives, add a victory to R6's tally
        elif duels.R6_hrts[n] > duels.R4_hrts[n] and duels.R6_hrts[n] > 0:
            R6_wins += 1
     
        #if R4 and R6 slay each other simultaneously, add a tally to the draws
        else:
            draws += 1
        
    #if R4 wins more duels, declare the winner
    if R4_wins > R6_wins:
        print(f'R4-6SD wins with {R4_wins} victories.')
        print(f'R6-4SD perishes with {R6_wins}.')
        if draws == 1:
            print(f'There was one glorious instance of simultaenous destruction.')
        else:
            print(f'There were {draws} glorious instances of simultaneous destruction.')
        
    #if R6 wins more duels, declare the winner    
    elif R6_wins > R4_wins:
        print(f'R6-4SD wins with {R6_wins} victories')
        print(f'R4-6SD perishes with {R4_wins}')
        if draws == 1:
            print(f'There was one glorious instance of simultaenous destruction.')
        else:
            print(f'There were {draws} glorious instances of simultaneous destruction.')
            
    #if the amount of duel wins is equal, declare a draw        
    else:
        print('Draw')
        print(f'There were {draws} draws.')
        print(f'R4-6SD had {R4_wins} wins.')
        print(f'R6-4SD had {R6_wins} wins.')


# In[ ]:


pwrful_mage(10)


# In[ ]:


pwrful_mage(10)


# ## Exercise 3
# Do the results change much at 100 duels?

# In[ ]:


pwrful_mage(100)


# ## Exercise 4
# Now, simulate 10,000 mage duels. Is there a clear winner?

# In[ ]:


pwrful_mage(10_000)


# # A Simpleton Duel

# In[ ]:


def ur_a_wizard_arry(n_duels):
    mage_4d6_health_and_dmg = np.random.choice(list(range(1, 7)), size = (n_duels, 4))
    mage_6d4_health_and_dmg = np.random.choice(list(range(1, 5)), size = (n_duels, 6))
    R4_stats = pd.DataFrame(mage_4d6_health_and_dmg)
    R6_stats = pd.DataFrame(mage_6d4_health_and_dmg)
    R4_stats['power'] = R4_stats[:].sum(axis = 1)
    R6_stats['power'] = R6_stats[:].sum(axis = 1)
    duel_data = pd.DataFrame({'R4_power': R4_stats.power,
                              'R6_power': R6_stats.power})
    duel_data['R4_wins'] = duel_data.R4_power > duel_data.R6_power
    duel_data['R6_wins'] = duel_data.R6_power > duel_data.R4_power
    duel_data['Draws'] = duel_data.R4_power == duel_data.R6_power
    
    if duel_data.R4_wins.sum() > duel_data.R6_wins.sum():
        print(f'R4-D6 wins with {duel_data.R4_wins.sum()} victories.')
        print(f'R6-D4 perishes with {duel_data.R6_wins.sum()}.')
        if duel_data.Draws.sum() == 1:
            print(f'There was one glorious instance of simultaneous destruction.')
        else:
            print(f'There were {duel_data.Draws} glorious instances of simultaneous destruction.')
    elif duel_data.R6_wins.sum() > duel_data.R4_wins.sum():
        print(f'R6-D4 wins with {duel_data.R6_wins.sum()} victories.')
        print(f'R4-D6 perishes with {duel_data.R4_wins.sum()}.')
        if duel_data.Draws.sum() == 1:
            print(f'There was one glorious instance of simultaenous destruction.')
        else:
            print(f'There were {duel_data.Draws.sum()} glorious instances of simultaneous destruction.')
    else:
        print('Draw')
        print(f'There were {duel_data.Draws.sum()} draws.')
        print(f'R4-D6 had {duel_data.R4_wins.sum()} wins.')
        print(f'R6-D4 had {duel_data.R6_wins.sum()} wins.')


# Simulate 10 duels

# In[ ]:


ur_a_wizard_arry(10)


# 10 duels again

# In[ ]:


ur_a_wizard_arry(10)


# 100 duels

# In[ ]:


ur_a_wizard_arry(100)


# 10,000 duels

# In[ ]:


ur_a_wizard_arry(10_000)


# One million duels

# In[ ]:


ur_a_wizard_arry(1_000_000)


# # A compromise scenario

# In[ ]:


def powerful_wizard(n_duels):
    #damage output generator for roll 4 mage
    mage_4d6_dmg = np.random.choice(list(range(1, 7)), size = (n_duels, 4))
    
    #damage output generator for roll 6 mage
    mage_6d4_dmg = np.random.choice(list(range(1, 5)), size = (n_duels, 6))
    
    #health points generator for roll 4 mage
    mage_4d6_health = np.random.choice(list(range(1, 7)), size = (n_duels, 4))
    
    #health points generator for roll 6 mage
    mage_6d4_health = np.random.choice(list(range(1, 5)), size = (n_duels, 6))
    
    #assign a variable name to a dataframe for R4 damage die values
    R4_dmg = pd.DataFrame(mage_4d6_dmg)
    
    #assign a variable name to a dataframe for R6 damage die values
    R6_dmg = pd.DataFrame(mage_6d4_dmg)
    
    #assign a variable name to a dataframe for R4 health die values
    R4_hrts = pd.DataFrame(mage_4d6_health)
    
    #assign a variable name to a dataframe for R6 health die values
    R6_hrts = pd.DataFrame(mage_6d4_health)
    
    #sum up the values of rolling 4 six-sided dice to get damage output
    R4_dmg['damage'] = R4_dmg[:].sum(axis = 1)
    
    #do it again for the health points to get total health
    R4_hrts['health_points'] = R4_hrts[:].sum(axis = 1)
    
    #sum up the values of rolling 6 four-sided dice to get damage output
    R6_dmg['damage'] = R6_dmg[:].sum(axis = 1)
    
    #total health for R6 mage
    R6_hrts['health_points'] = R6_hrts[:].sum(axis = 1)
    
    #assign a variable name for a dataframe with the duel data
    duels = pd.DataFrame(data = {'R4_hrts': R4_hrts.health_points,
                             'R6_hrts': R6_hrts.health_points,
                             'R4_dmg': R4_dmg.damage,
                             'R6_dmg': R6_dmg.damage})
    
    #set counters for mage duel results
    R4_wins = 0
    R6_wins = 0
    draws = 0
    
    #start a for loop to run through each row of the duels dataframe (simulate each duel)
    for n in range(len(duels)):
        
        #start a while loop to simulate attacks while both mages still live (until someone croaks)
        while duels.R4_hrts[n] and duels.R6_hrts[n] > 0:
            
            #deduct health points by damage points (simulate attacks)
            duels.R4_hrts[n] = duels.R4_hrts[n] - duels.R6_dmg[n]
            duels.R6_hrts[n] = duels.R6_hrts[n] - duels.R4_dmg[n]
            
        #for the sake of the lesson here, we will just see who has a greater value of health by the time one or both
        #mages reach negative health
        if duels.R4_hrts[n] > duels.R6_hrts[n]:
            R4_wins += 1
            
        
        elif duels.R6_hrts[n] > duels.R4_hrts[n]:
            R6_wins += 1
     
        #if R4 = R6, add a tally to the draws
        else:
            draws += 1
        
    #if R4 wins more duels, declare the winner
    if R4_wins > R6_wins:
        print(f'R4-6SD wins with {R4_wins} victories.')
        print(f'R6-4SD perishes with {R6_wins}.')
        if draws == 1:
            print(f'There was one glorious instance of simultaenous destruction.')
        else:
            print(f'There were {draws} glorious instances of simultaneous destruction.')
        
    #if R6 wins more duels, declare the winner    
    elif R6_wins > R4_wins:
        print(f'R6-4SD wins with {R6_wins} victories')
        print(f'R4-6SD perishes with {R4_wins}')
        if draws == 1:
            print(f'There was one glorious instance of simultaenous destruction.')
        else:
            print(f'There were {draws} glorious instances of simultaneous destruction.')
            
    #if the amount of duel wins is equal, declare a draw        
    else:
        print('Draw')
        print(f'There were {draws} draws.')
        print(f'R4-6SD had {R4_wins} wins.')
        print(f'R6-4SD had {R6_wins} wins.')


# In[ ]:


powerful_wizard(10)


# In[ ]:


powerful_wizard(10)


# In[ ]:


powerful_wizard(100)


# In[ ]:


powerful_wizard(1000)


# In[ ]:


powerful_wizard(10_000)


# In[ ]:


powerful_wizard(100_000)


# In[ ]:


powerful_wizard(1_000_000)

