import pandas as pd


df = pd.read_csv('hh_results.csv')
print(df.to_string(max_rows=20, max_cols=8))
