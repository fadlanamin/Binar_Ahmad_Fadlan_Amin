import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('raw_data_text.db')

data_raw = pd.read_csv('data.csv', encoding='latin-1')
data_raw.to_sql('raw_data_text', conn, if_exists='replace', index=False )


#Data Visualition for #of tweet that are abusive or hate speech
Hate_Speech = data_raw['HS'].sum()
Abusive = data_raw['Abusive'].sum()
Negative_Tweet = Hate_Speech + Abusive

#Sum of Tweet where doesn't contain Abusive and Hatespeech aspect
Positive_Tweet = """
SELECT COUNT(Tweet) as Positive_Tweet
FROM raw_data_text
WHERE HS=0
AND Abusive=0
"""
positive_tweet = pd.read_sql(Positive_Tweet, conn) #Results = 5860

#Bar Chart for Tweets Comparison 
y = (5860, Hate_Speech, Abusive ) #5860 from query results
print(y)
x = ('Positive_Tweet', 'Hate_Speech', 'Abusive')
label_coord = range(len(x))
plt.bar(label_coord, y)
plt.xticks(label_coord, x)

#To add label value on the bar chart
for i,v in enumerate(y):
    plt.text(i, v, str(v), ha = "center")
plt.show()

