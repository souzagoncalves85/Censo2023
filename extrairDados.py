import pandas as pd

# Caminho do arquivo JSON
file_path = "censo_pb.json"

# Carregar o arquivo JSON com linhas separadas
df = pd.read_json(file_path, encoding="latin1", lines=True)

# Renomear as colunas para algo mais amigável
colunas_necessarias = {"Nome da Escola": "Nome da Escola", "QT_MAT_BAS": "Quantidade"}
df = df[list(colunas_necessarias.keys())]

# Renomear as colunas
df.rename(columns=colunas_necessarias, inplace=True)

# Tratar valores nulos (substituindo por 0)
df["Quantidade"] = df["Quantidade"].fillna(0).astype(int)

# Somar a quantidade de matrículas por escola
matriculas_por_escola = df.groupby("Nome da Escola")["Quantidade"].sum().astype(int)

# Exibir o resultado
print(matriculas_por_escola)
