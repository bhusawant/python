# Q.1) 
"""
import matplotlib.pyplot as plt

countries = ['United States', 'China', 'Great Britain', 'Russia', 'Germany', 'Japan']
gold_medals = [57, 48, 39, 25, 20, 10]
silver_medals = [28, 30, 21, 25, 18, 16]
fig,ax = plt.subplots(figsize=(10, 6))
width = 0.35
ind = range(len(countries))
silver_ind =[x + width for x in ind]
gold_bars = ax.bar(ind, gold_medals, width, label='Gold medals')
silver_bars = ax.bar(ind, silver_medals, width, label='Silver medals')
ax.set_xlabel('Countries')
ax.set_ylabel('Medal count')
ax.set_title('Gold and silver medals by country')
ax.set_xticks([i+width/2 for i in ind])
ax.set_xticklabels(countries)
ax.legend()
plt.show()
"""


# Q.2)
"""
import matplotlib.pyplot as plt

countries = ['United States', 'China', 'Great Britain', 'Russia', 'Germany', 'Japan']
gold_medals = [57, 48, 39, 25, 20, 10]
fig,ax = plt.subplots(figsize=(8, 8))
ax.pie(gold_medals, labels=countries, autopct='%1.1f%%', startangle=90, shadow=True)
ax.set_title('Gold medals obtained by countries in olympics 2012')
ax.legend(countries, title='Countries', loc='upper right')
plt.show()
"""


# Q.3)

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)
data = np.random.randint(0, 100, 1000)
bins = np.arange(0, 101, 5)
fig,ax = plt.subplots(figsize=(10, 6))
ax.hist(data, bins = bins, edgecolor = 'black')
ax.set_xlabel('Range')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of randomly generated data\nwith ranges [0-5, 5-10, ........, 95-100]')
plt.show()


