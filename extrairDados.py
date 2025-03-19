import pandas as pd

# Caminho do arquivo CSV de entrada
file_path = "microdados_ed_basica_2023.csv"

# Carregar o arquivo CSV corretamente
df = pd.read_csv(file_path, encoding="latin1", delimiter=";", low_memory=False)

# Selecionar e renomear as colunas desejadas
colunas_necessarias = {
    "NO_REGIAO": "regiao",
    "SG_UF": "uf",
    "NO_MUNICIPIO": "municipio",
    "NO_MESORREGIAO": "mesorregiao",
    "NO_MICRORREGIAO": "microrregiao",
    "NO_ENTIDADE": "escola",
    "QT_MAT_BAS": "quantidade"
}

# Filtrar as colunas desejadas e renomear
df = df[list(colunas_necessarias.keys())].rename(columns=colunas_necessarias)

# Filtrar apenas registros do estado da Paraíba (SG_UF == "PB")
df = df[df["uf"] == "PB"]

# Tratar valores nulos na coluna "quantidade" e garantir que seja inteiro
df["quantidade"] = df["quantidade"].fillna(0).astype(int)

# Garantir que não há valores nulos em outras colunas essenciais
df.fillna({"regiao": "Desconhecido", "municipio": "Desconhecido",
           "mesorregiao": "Desconhecido", "microrregiao": "Desconhecido",
           "escola": "Desconhecida"}, inplace=True)

# Somar a quantidade de matrículas por escola dentro da Paraíba
df = df.groupby(["regiao", "uf", "municipio", "mesorregiao", "microrregiao", "escola"], as_index=False)["quantidade"].sum()

# Caminho do arquivo JSON de saída
output_file = "censo_pb_formatado.json"

# Salvar o resultado como JSON bem estruturado
df.to_json(output_file, orient="records", indent=4, force_ascii=False)

print(f"Arquivo JSON gerado com sucesso: {output_file}")
