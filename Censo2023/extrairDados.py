import pandas as pd
import json

# Carregar os dados do CSV
file_path = "microdados_ed_basica_2023.csv"
df = pd.read_csv(file_path, delimiter=";", encoding="latin1", low_memory=False)

# Filtrar apenas os dados da Paraíba (UF = 'PB') e selecionar colunas específicas
df_pb = df[df["SG_UF"] == "PB"][["NO_ENTIDADE", "SG_UF", "NO_MUNICIPIO", "NO_MESORREGIAO", "NO_MICRORREGIAO", "QT_MAT_BAS"]]

# Renomear colunas para melhor entendimento
df_pb.rename(columns={
    "NO_ENTIDADE": "Nome da Escola",
    "SG_UF": "UF",
    "NO_MUNICIPIO": "Município",
    "NO_MESORREGIAO": "Mesorregião",
    "NO_MICRORREGIAO": "Microrregião",
}, inplace=True)

# Salvar os dados filtrados em um arquivo JSON
json_file_path = "censo_pb.json"
df_pb.to_json(json_file_path, orient="records", lines=True, force_ascii=False)

print(f"Dados da Paraíba foram salvos em {json_file_path}")
