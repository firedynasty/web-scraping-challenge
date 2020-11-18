#https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas


import pandas as pd
import numpy as np

df = pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]})

for index, row in df.iterrows():
    print(row['c1'], row['c2'])


10 100
11 110
12 120


# This code returns that you see 10, 11, 12
# and then you see 100, 110, 120

