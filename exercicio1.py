import pandas as pd

df = pd.read_csv(r"C:\Users\alan.mello\Downloads\funcionarios - Null.csv")



df ["liquido"] = df["lucro"] - df["salario"]


df ["nome"] = df["nome"].str.upper()


df["lucro positivo"] = df["liquido"].apply(lambda x: "lucro positivo" if x > 0 else "lucro negativo")


df = df.rename(columns={"id":"ID", "nome" : "NOME", "departamento":"DEPARTAMENTO",
                         "salario" : "SALARIO", "lucro" : "LUCRO", "ativo": "ATIVO",
                           "data de nascimento" : "DATA DE NASCIMENTO", "liquido": "LUCRO LIQUIDO",
                           "lucro positivo": "LUCRO P ou N"})

print(df)
