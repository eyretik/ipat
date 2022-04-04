#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:





# In[ ]:





# In[17]:


# Dataset from taxi journeys in Peru, with driver ratings, passenger ratings, coordinates, and a couple of other details. 

# journey_id - unique id of the trip
# user_id - user id
# driver_id - id of driver
# taxi_id - id of car
# icon - trip type
# start_type - type of order (asap, reserved, delayed)
# start_at - trip start time
# start_lat - user's home location, latitude
# start_lon - user's home location, longitude
# end_at - trip end time
# end_lat is the user's final location, latitude
# end_lon - your final location, longitude
# end_state - order status
# driver_start_lat - initial location of the driver, latitude
# driver_start_lon - initial location of driver, longitude
# arrived_at - arrival time of driver
# source - platform, from which the order was made
# driver_score - client's evaluation of the driver
# rider_score - driver's evaluation of the client


# In[87]:


taxi = (
    pd.read_csv('~//OneDrive//Karpov_courses//Data_Analist//Lessons_codes//Lesson_3//3_taxi_peru.csv',
                sep = ';',
                parse_dates = ['start_at', 'end_at', 'arrived_at'])
)


# In[19]:


# 3.9 Check from which platform the most orders were made. Answer with a % value, rounded to integers.


# In[20]:


taxi.groupby('source', as_index = False).aggregate({'journey_id':'count'})


# In[21]:


(
    taxi
    .source
    .value_counts(normalize = True)
    .mul(100)
    .round()
    .max()
)
# Answer - 42


# In[22]:


sns.countplot(taxi['icon'])


# In[29]:


# 3.12 Use sns.countplot and the hue parameter to visualise the distribution of the variable 
# end_state (final order state) by platform (source).
# In other words, plot the platform on the x-axis and use order state as the colour.

sns.countplot(data = taxi, x = 'source', hue = 'end_state')


# In[63]:


# Check how the drivers' scores (driver_score) are distributed. Follow the steps below to prepare the data:

# Calculate the frequency of occurrence of each of the scores
# Convert to percentages and round to 2 decimal places (.mul(100).round(2))
# Reset the indexes
# Rename the columns to driver_score and percentage
# Sort by driver_score in ascending order (0 to 5)
# Write the result to driver_score_counts


driver_score_counts = (
    taxi
    .driver_score
    .value_counts(normalize = True)
    .mul(100)
    .round(2)
    .reset_index()
    .rename(columns={"index":"driver_score", "driver_score" : 'percentage'})
    .sort_values('driver_score', ascending = True)
)


# In[84]:


ax = sns.barplot(x='driver_score', y='percentage', data=driver_score_counts, color='gray', alpha=0.5)
ax.set(xlabel='Driver score', ylabel='Percentage')
sns.despine()  # убрать часть рамки графика
plt.show()


# In[85]:


# 3.15 Do the same steps for rider_score (drivers' evaluations of customers), remembering to graph it.
# How does it differ from the distribution of the drivers' estimates?

rider_score_counts = (
    taxi
    .rider_score
    .value_counts(normalize = True)
    .mul(100)
    .round(2)
    .reset_index()
    .rename(columns={"index":"rider_score", "rider_score" : 'percentage'})
    .sort_values('rider_score', ascending = True)
)
ax = sns.barplot(x='rider_score', y='percentage', data=rider_score_counts, color='magenta', alpha=0.5)
ax.set(xlabel='Rider score', ylabel='Percentage')
sns.despine()  # убрать часть рамки графика
plt.show()


# In[ ]:




