import pandas as pd
import csv
df = pd.read_csv("sample.csv", sep = ',', header= 'infer', encoding = 'latin1')
print(df)


