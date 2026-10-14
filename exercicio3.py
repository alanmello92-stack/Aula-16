import pandas as pd

df = pd.DataFrame({
    'categoria': ['A', 'B', 'A', 'B', 'A'],
    'vendas': [100, 200, 150, 300, 120],
    'quantidade': [1, 2, 1, 3, 2]
})

df.groupby('categoria')['quantidade'].mean()

df.groupby('categoria').sum()

df.groupby(['categoria', 'quantidade'])['vendas'].sum()

df.groupby('categoria')["vendas"].agg(['sum', 'mean', 'max', 'count'])

print(df.groupby('categoria')["vendas"].agg(['sum', 'mean', 'max', 'count']))

