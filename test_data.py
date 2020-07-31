import pandas as pd
df = pd.read_csv('test_data.csv', header=None)
df.columns = ['label', 'text']
dataset = df[['text', 'label']].values.tolist()
    