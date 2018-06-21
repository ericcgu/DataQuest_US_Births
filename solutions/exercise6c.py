'''
Find a way to combine the CDC data with the SSA data, which you can find here. Specifically, brainstorm ways to deal with the overlapping time periods in the datasets.
'''
import pandas as pd
import glob

def merge_csv(file_prefix):
    files = glob.glob(file_prefix) 
    df = pd.concat((pd.read_csv(f, header = 0) for f in files))
    df_deduplicated = df.drop_duplicates()
    df_deduplicated.to_csv("data/US-births-Merged.csv")

merge_csv('data/US_births_*.csv')    

