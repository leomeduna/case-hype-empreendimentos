# %%
# Importando as bibliotecas
import pandas as pd
import numpy as np

# %%
# Lendo os arquivos
df_orcamento = pd.read_csv("C:/case_hype/data/Base_Orcamento.csv",encoding='latin1', sep=';')
df_realizado = pd.read_csv("C:/case_hype/data/Base_Realizado.csv",encoding='latin1', sep=';')

# %%
# Boas práticas usando snake_case 
df_orcamento = df_orcamento.rename(columns={
    'Obra': 'obra',
    'Grupo Orçamentário': 'grupo_orcamentario',
    'Cód. Estruturado': 'cod_estruturado',
    'Cód. Item': 'cod_item',
    'Descrição Item': 'descricao_item',
    'Unid.': 'unid',
    'Categoria': 'categoria',
    ' Qtde. Insumo ': 'qtde_insumo',
    ' Custo Insumo ': 'custo_insumo',
    ' Total Orçado ': 'total_orcado'
})

# %%
df_realizado = df_realizado.rename(columns={
    'Obra': 'obra',
    'Grupo Orçamentário': 'grupo_orcamentario',
    'Cód. Estruturado': 'cod_estruturado',
    'Cód. Item': 'cod_item',
    'Descrição Item': 'descricao_item',
    'Unid.': 'unid',
    'Categoria': 'categoria',
    ' Qtd Realizada ': 'qtde_realizado',
    ' ValorUnitRealizado ': 'valor_unit_realizado',
    ' ValorTotalRealizado ': 'valor_total_realizado',
    'Cód. Fornecedor': 'cod_fornecedor',
    'Fornecedor': 'fornecedor',
    'Cód. Pedido': 'cod_pedido',
    'Cód. Contrato': 'cod_contrato'
})

# %%
def conversao_coluna_str_to_float(coluna_series: pd.Series) -> pd.Series:
    # Removendo o separador de milhares (o ponto '.')
    # Usando .astype(str) para garantir que seja string antes de aplicar .str
    coluna_limpa = coluna_series.astype(str).str.replace('.', '', regex=False)

    # Substituindo o separador decimal (a vírgula ',') por um ponto '.'
    coluna_limpa = coluna_limpa.str.replace(',', '.', regex=False)

    # Converter para um numérico
    coluna_final_numerica = pd.to_numeric(coluna_limpa, errors='coerce')

    return coluna_final_numerica

# --- Aplicando a função às colunas:
orcamento_colunas_para_converter = ['custo_insumo', 'qtde_insumo', 'total_orcado']
realizado_colunas_para_converter = ['qtde_realizado', 'valor_unit_realizado', 'valor_total_realizado']

for col in orcamento_colunas_para_converter:
    df_orcamento[col] = conversao_coluna_str_to_float(df_orcamento[col])

for col in realizado_colunas_para_converter:
    df_realizado[col] = conversao_coluna_str_to_float(df_realizado[col])

# %%
# Passando Data NF para um tipo datetime ao invés de object
df_realizado['Data NF'] = pd.to_datetime(df_realizado['Data NF'])


# %%
# Salvando arquivos para mandar para o PBI, arquivos .parquet tem uma performance muito mais eficiênte e leve/otimizada. Bem melhor que o Script do Python
# onde ocorre várias inconsistências e dores de cabeça. 
df_orcamento.to_parquet("base_orcamento.parquet", index=False)
df_realizado.to_parquet("base_realizado.parquet", index=False)

