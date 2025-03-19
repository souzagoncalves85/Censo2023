import pandas as pd
import json

# Caminho do arquivo JSON de entrada
file_path = "censo_pb.json"

# Carregar o arquivo JSON com linhas separadas
df = pd.read_json(file_path, encoding="latin1", lines=True)

# Selecionar e renomear as colunas desejadas
colunas_necessarias = {
    "NO_REGIAO": "regiao",
    "NO_UF": "uf",
    "NO_MUNICIPIO": "municipio",
    "NO_MESORREGIAO": "mesorregiao",
    "NO_MICRORREGIAO": "microrregiao",
    "NO_ENTIDADE": "escola",
    "QT_MAT_BAS": "quantidade"
}

# Filtrar as colunas desejadas e renomear
df = df[list(colunas_necessarias.keys())].rename(columns=colunas_necessarias)

# Filtrar apenas registros da UF "PB"
df = df[df["uf"] == "PB"]

# Tratar valores nulos na coluna "quantidade"
df["quantidade"] = df["quantidade"].fillna(0).astype(int)

# Somar a quantidade de matrículas por escola dentro da Paraíba
df = df.groupby(["regiao", "uf", "municipio", "mesorregiao", "microrregiao", "escola"], as_index=False)["quantidade"].sum()

# Caminho do arquivo JSON de saída
output_file = "censo_pb_formatado.json"

# Salvar o resultado como JSON bem estruturado
df.to_json(output_file, orient="records", indent=4, force_ascii=False)

print(f"Arquivo JSON gerado com sucesso: {output_file}")
