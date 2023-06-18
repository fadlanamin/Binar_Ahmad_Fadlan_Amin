import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_venn as vplt
import sqlite3

conn = sqlite3.connect('raw_data_text.db')

data_raw = pd.read_csv('data.csv', encoding='latin-1')
data_raw.to_sql('raw_data_text', conn, if_exists='replace', index=False )


#Sum of Tweet that are abusive
Abusive_Tweet = """
SELECT COUNT(Tweet) as HS_Tweet
FROM raw_data_text
WHERE Abusive=1
"""
Abusive_Tweet = pd.read_sql(Abusive_Tweet, conn) #Result = 5043

#Sum of Tweet that are hate speech
HS_Tweet = """
SELECT COUNT(Tweet) as HS_Tweet
FROM raw_data_text
WHERE HS=1
"""
HS_Tweet = pd.read_sql(HS_Tweet, conn) #Result 5561



#Sum of Tweet where doesn't contain Abusive and Hatespeech aspect
Abusive_HS_Tweet = """
SELECT COUNT(Tweet) as Abusive_HS_Tweet
FROM raw_data_text
WHERE HS=1
AND Abusive=1
"""
Abusive_HS_Tweet = pd.read_sql(Abusive_HS_Tweet, conn) #Results = 3295

#Venn Diagram of Abusive and Hate Speech tweets
v = vplt.venn2(subsets={'10':5043, '01':5561, '11':3295 }, set_labels=('Abusive_Tweets','HS_Tweet'))
plt.show

