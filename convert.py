import os
import pandas as pd

df = pd.DataFrame(columns=['text', 'summary'])
with open('output.tsv') as f:
    for line in f.readlines():
        strs = line.split('\t')
        df = df.append({'text': strs[3], 'summary': strs[0]+' '+strs[1]+' '+strs[2]}, ignore_index=True)

df = df.sample(frac=1)

num = len(df)
df[:int(num*0.8)].to_csv('train.csv', sep=',', index=False)
df[:int(num*0.2)].to_csv('dev.csv', sep=',', index=False)
