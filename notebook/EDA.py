# Análise Exploratória dos Dados em Visualizações
# pois vai para o POWER BI
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df_orcamento = pd.read_csv("C:/case_hype/data/Base_Orcamento.csv",encoding='latin1', sep=';')
df_realizado = pd.read_csv("C:/case_hype/data/Base_Realizado.csv",encoding='latin1', sep=';')

# %%
def conversao_coluna_str_to_float(coluna_series: pd.Series) -> pd.Series:
    # 1. Remover o separador de milhares (o ponto '.')
    # Usar .astype(str) para garantir que seja string antes de aplicar .str
    coluna_limpa = coluna_series.astype(str).str.replace('.', '', regex=False)

    # 2. Substituir o separador decimal (a vírgula ',') por um ponto '.'
    coluna_limpa = coluna_limpa.str.replace(',', '.', regex=False)

    # 3. Converter para numérico
    coluna_final_numerica = pd.to_numeric(coluna_limpa, errors='coerce')

    return coluna_final_numerica

# --- Aplicando a função às colunas desejadas ---
colunas_para_converter = [' Custo Insumo ', ' Qtde. Insumo ', ' Total Orçado ']

for col in colunas_para_converter:
    df_orcamento[col] = conversao_coluna_str_to_float(df_orcamento[col])

# %%
df_orcamento.columns

# %%
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
df_orcamento[['obra', 'cod_estruturado', 'cod_item', 'descricao_item']].nunique()
df_orcamento[['qtde_insumo', 'custo_insumo', 'total_orcado']].head(10)

# %%
# Análise de Soma de total_orcado por categoria
custo_p_categoria = df_orcamento.groupby(by='categoria')['total_orcado'].sum().sort_values(ascending=False)
custo_p_categoria

plt.figure(figsize=(10, 6))

sns.barplot(
    x=custo_p_categoria.values,
    y=custo_p_categoria.index,
    color='green'
)
plt.tight_layout()
plt.title("Soma de Custos por Categoria")
plt.show()

# %%
# Análise de Soma de total_orcado por grupo_orcamentario
custo_p_grupo_orc = df_orcamento.groupby(by='grupo_orcamentario')['total_orcado'].sum().sort_values(ascending=False)
top_20_custo_p_grupo = custo_p_grupo_orc.head(20)

plt.figure(figsize=(14, 8))

sns.barplot(
    x=top_20_custo_p_grupo.values,
    y=top_20_custo_p_grupo.index,
    color='green'
)
plt.tight_layout()
plt.title("Top 20 Grupos Orçamentário mais Custosos")
plt.show()

# %%
# Análise de Soma de total_orcado por descricao_item
custo_p_item = df_orcamento.groupby(by='descricao_item')['total_orcado'].sum().sort_values(ascending=False)
top_20_custo_p_item = custo_p_item.head(20)

plt.figure(figsize=(14, 8))

sns.barplot(
    x=top_20_custo_p_item.values,
    y=top_20_custo_p_item.index,
    color='green'
)
plt.tight_layout()
plt.title("Top 20 Itens mais Custosos")
plt.show()

# %%
# Gerando Histogramas ou Box Plots para Qtde. Insumo, Custo Insumo e Total Orçado.
plt.figure(figsize=(10, 6))

sns.boxplot(
    data=np.log10(df_orcamento[['qtde_insumo', 'custo_insumo', 'total_orcado']]),
    color='orange'
)
plt.tight_layout()
#plt.ylim(0, 70000)
plt.title("Boxplots das Variáveis de Demanda e Custo")
plt.show()

# %%
variaveis = ['qtde_insumo', 'custo_insumo', 'total_orcado']

for var in variaveis:
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df_orcamento, x=var, kde=True, bins=50, color='green')
    plt.title(f'Distribuição da variável: {var}')
    plt.xlabel(var)
    plt.ylabel('Frequência')
    plt.tight_layout()
    plt.show()
