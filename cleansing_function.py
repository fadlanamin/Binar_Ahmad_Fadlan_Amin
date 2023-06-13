""" 
Function untuk membersihkan data text
"""
import re
import pandas as pd
import sqlite3

conn = sqlite3.connect('raw_data.db')

#Import of Abusive Words, Alay Words and Clean Alay Words
data_abusive = pd.read_sql('Select word from abusive', conn)
data_alay_word = pd.read_sql('Select alay_word from alay', conn)
data_alay_clean = pd.read_sql('Select formal_word from alay', conn)


#Change Abusive and Alay into Lists and Adjust the special characters for RegEx Pattern
df_abusive_list = data_abusive.values.tolist()
df_dict = str(df_abusive_list).replace('[','').replace(']','').replace(',','|').replace("'","")

df_alay_words = data_alay_word.values.tolist()
df_alay = str(df_alay_words).replace('[','').replace(']','').replace(',','|').replace("'","")

df_formal_words = data_alay_clean.values.tolist()
df_formal = str(df_formal_words).replace('[','').replace(']','').replace(',','|').replace("'","")


def text_cleansing(text):
    # Bersihkan tanda baca (selain phuruf dan angka)
    clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # yg lain
    clean_text = clean_text.lower()
   
    # Masking abusive words with xxx 
    clean_text = re.sub(df_dict, ' xxx', text) 

    # Replacing alay words with its formal words
    clean_text = re.sub(df_alay, df_dict, text)

    return clean_text



def cleansing_files(file_upload):
    # Read csv file upload, jika error dengan metode biasa, gunakan encoding latin-1
    try:
        df_upload = pd.read_csv(file_upload)
    except:
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