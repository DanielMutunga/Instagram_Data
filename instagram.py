#import pandas and matplotlib libraries.
import matplotlib.pyplot as plot
import pandas as pd
import random

#Load the dataset into your program
data = pd.read_csv('Instagram-Users.csv')

data['time'] = pd.to_datetime(data['time'])

#We visualise our data according to how followers have grown over time and per country.

#Follower growth per time
follower_growth = data.groupby('time')['followers'].sum()
#Follower growth per country
country_distribution = data['country'].value_counts()

# Visualize follower growth over time
plt.figure(figsize=(12, 6))
plt.plot(follower_growth.index, follower_growth.values)
plt.xlabel('Date')
plt.ylabel('Total followers')
plt.title('A plot Showing Instagram Follower Growth Over Time')
plt.grid(True)
plt.show()

# Visualize the distribution of users by country
plt.figure(figsize=(10, 6))
country_distribution.plot(kind='bar')
plt.xlabel('country')
plt.ylabel('Number of Users')
plt.title('A plot showing the Distribution of Instagram Users by Country')
plt.xticks(rotation=45)
plt.show()

