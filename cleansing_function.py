""" 
Function untuk membersihkan data text
"""
import re
import pandas as pd
import sqlite3

conn = sqlite3.connect('raw_data.db')

#Import of Abusive Words and change into Lists and adjust the special characters for regexx pattern
data_abusive = pd.read_sql('Select word from abusive', conn)
df_abusive_list = data_abusive.values.tolist()
df_dict_abusive = str(df_abusive_list).replace('[','').replace('[','').replace(']','').replace(',','|').replace("'","")

# Import of alay words and change ino dictionary to lookup the formal words
# Alay words is used as key to lookup the formal words as value
data_alay_word = pd.read_sql('Select * from alay', conn)
df_alay = dict(zip(data_alay_word['alay_word'],data_alay_word['formal_word']))

def text_cleansing(text):
    # Non-alphabet and numbers cleansing
    clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Lower text
    clean_text = clean_text.lower()
   
    # Masking abusive words with xxx 
    clean_text = re.sub(f'\{df_dict_abusive}\S+', ' xxx', clean_text)

    # Replacing alay words with its formal words
    clean_text = " ".join(df_alay.get(word, word) for word in clean_text.split())

    return clean_text

def cleansing_files(file_upload):
    # Read csv file upload gunakan encoding latin-1
    df_upload = pd.read_csv(file_upload, encoding="latin-1")
    print("Read dataframe from Upload success!")
    # Ambil hanya kolom pertama saja 

    df_upload = pd.DataFrame(df_upload.iloc[:,0])
    # Rename kolom menjadi "raw_text"

    df_upload.columns = ["raw_text"]

    # Bersihkan text menggunakan fungsi text_cleansing    

    # Simpan di kolom "clean_text"
    df_upload["clean_text"] = df_upload["raw_text"].apply(text_cleansing)
    print("Cleansing text success!")
    return df_upload