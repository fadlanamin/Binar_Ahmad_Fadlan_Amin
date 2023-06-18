import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('raw_data_text.db')

data_raw = pd.read_csv('data.csv', encoding='latin-1')
data_raw.to_sql('raw_data_text', conn, if_exists='replace', index=False )

#Sum of Tweets that contain Abusive and Hatespeech aspect

Negative_Tweet = """
SELECT COUNT(Tweet) as Negative_Tweet
FROM raw_data_text
WHERE HS=1
OR Abusive=1
"""

Negative_Tweet = pd.read_sql(Negative_Tweet, conn) ##Results = 7309
print(Negative_Tweet)


#Sum of Tweets that doesn't contain Abusive and Hatespeech aspect

Positive_Tweet = """
SELECT COUNT(Tweet) as Positive_Tweet
FROM raw_data_text
WHERE HS=0
AND Abusive=0
"""
positive_tweet = pd.read_sql(Positive_Tweet, conn) #Results = 5860

#Pie Chart Comparison of Negative and Positive Tweets 
values_tweet = [5860, 7309]
label_tweet = ['Positive Tweet', 'Negative_Tweet']
plt.pie(values_tweet, labels=label_tweet, autopct='%1.1f%%')
plt.title('Positive and Negative Tweet Comparison')
plt.show

