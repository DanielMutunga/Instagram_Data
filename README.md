# Lux Dev Week 1 Assignment.

### Let's say you are a product Data Scientist at instagram, How would you measure the success of the Instagram TV product?
###This is how I could go about it

- ***Step 1:*** Set up my envornment. This includes downloading and installing softwares like Visual Studio Code, Jupyter notebook and Anacoda

- ***Step 2:*** Get random data from [Mockaroo](https://www.mockaroo.com/)

- ***Step 3:*** Load the data into visual studio code.

```
data = pd.read_csv('Instagram-Users.csv')
```
- ***Step 4:*** Import pandas and matplotlib

```
import matplotlib.pyplot as plot
import pandas as pd
import random
```
- ***Step 5:*** Visualise the data according to how followers have grown over time and per country

```
follower_growth = data.groupby('time')['followers'].sum()
country_distribution = data['country'].value_counts()
```
- ***Step 6:*** Visualize follower growth over time

```
plt.figure(figsize=(12, 6))
plt.plot(follower_growth.index, follower_growth.values)
plt.xlabel('Date')
plt.ylabel('Total followers')
plt.title('A plot Showing Instagram Follower Growth Over Time')
plt.grid(True)
plt.show()
```
- ***Step 7:*** Visualize the distribution of users by country

```
plt.figure(figsize=(10, 6))
country_distribution.plot(kind='bar')
plt.xlabel('country')
plt.ylabel('Number of Users')
plt.title('A plot showing the Distribution of Instagram Users by Country')
plt.xticks(rotation=45)
plt.show()
```
