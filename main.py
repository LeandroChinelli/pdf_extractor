from text_modeling import ExtractionPDF, FilePath, Constants
import os
import pandas as pd

files_obj = FilePath()
files = files_obj.get_files()

df_fatura = pd.DataFrame()
df_categories = pd.read_csv('places_categories.csv', sep=';')

for file in files:
    extractor = ExtractionPDF()
    df = extractor.extract_pdf(file[0])
    df['fatura'] = file[1][:6]
    df_fatura = pd.concat((df_fatura, df))

df_fatura = df_fatura[~df_fatura['places'].str.contains(Constants.TOTAL_VALUE)]

payment_condition = (df['places'].str.contains(f'{Constants.REGULAR_PAYMENT}|{Constants.ONLINE_PAYMENT}'))
df.loc[payment_condition, 'values'] *= -1
df_fatura = df_fatura.merge(df_categories, on='places', validate='m:1')

df_fatura.to_csv('faturas.csv', index=False)
