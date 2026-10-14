import pandas as pd

df = pd.read_csv(r"C:\Users\alan.mello\Downloads\funcionarios.csv")

df = df[df["ativo"] == True]

df["Salario_maior_5000"] = df["salario"].apply(lambda x: "Possui" if x > 5000 else "Não possui")


df = df.rename(columns={"ativo":"EMPREGADOS"})


print(df)