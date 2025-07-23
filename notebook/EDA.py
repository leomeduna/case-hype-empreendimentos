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
plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df_orcamento[['qtde_insumo', 'custo_insumo', 'total_orcado']],
    color='orange'
)
plt.tight_layout()
plt.ylim(0, 70000)
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

# %%
# --------------------------------------------------------------------------------

## Base Realizado
# %%
colunas_para_converter_2 = [' ValorUnitRealizado ', ' Qtd Realizada ', ' ValorTotalRealizado ']

for col in colunas_para_converter_2:
    df_realizado[col] = conversao_coluna_str_to_float(df_realizado[col])

df_realizado.info()

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
    ' ValorTotalRealizado ': 'valor_total_realizado'
})

# %%
df_realizado[['obra', 'cod_estruturado', 'cod_item', 'descricao_item']].nunique()
df_realizado[['qtde_realizado', 'valor_unit_realizado', 'valor_total_realizado']].head(10)

# %%
# Análise de Soma de valor_total_realizado por categoria
realizado_custo_p_categoria = df_realizado.groupby(by='categoria')['valor_total_realizado'].sum().sort_values(ascending=False)
realizado_custo_p_categoria

plt.figure(figsize=(10, 6))

sns.barplot(
    x=realizado_custo_p_categoria.values,
    y=realizado_custo_p_categoria.index,
    color='green'
)
plt.tight_layout()
plt.title("Realizado - Soma de Custos por Categoria")
plt.show()

# %%
# Análise de Soma de total_valor_realizado por descricao_item
realizado_custo_p_item = df_realizado.groupby(by='descricao_item')['valor_total_realizado'].sum().sort_values(ascending=False)
realizado_top_20_custo_p_item = realizado_custo_p_item.head(20)

plt.figure(figsize=(14, 8))

sns.barplot(
    x=realizado_top_20_custo_p_item.values,
    y=realizado_top_20_custo_p_item.index,
    color='green'
)
plt.tight_layout()
plt.title("Realizado - Top 20 Itens mais Custosos")
plt.show()

# %%
# Gerando Histogramas ou Box Plots para qtde_realizado, total_valor_unit e valor_total_realizado.
plt.figure(figsize=(10, 6))

sns.boxplot(
    data=np.log10(df_realizado[['qtde_realizado', 'valor_unit_realizado', 'valor_total_realizado']]),
    color='orange'
)
plt.tight_layout()
#plt.ylim(0, 70000)
plt.title("Realizado - Boxplots das Variáveis de Demanda e Custo")
plt.show()

# %%
plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df_realizado[['qtde_realizado', 'valor_unit_realizado', 'valor_total_realizado']],
    color='orange'
)
plt.tight_layout()
plt.ylim(0, 40000)
plt.title("Realizado - Boxplots das Variáveis de Demanda e Custo")
plt.show()

# %%
realizado_variaveis = ['qtde_realizado', 'valor_unit_realizado', 'valor_total_realizado']

for var in realizado_variaveis:
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df_realizado, x=var, kde=True, bins=50, color='green')
    plt.title(f'Distribuição da variável: {var}')
    plt.xlabel(var)
    plt.ylabel('Frequência')
    plt.tight_layout()
    plt.show()

# %%
df_realizado['Data NF'] = pd.to_datetime(df_realizado['Data NF'])

# %%
plt.figure(figsize=(10, 6))

sns.lineplot(
    data=df_realizado,
    x=df_realizado['Data NF'].dt.date,
    y=df_realizado['valor_total_realizado'],
    color='blue'
)
plt.tight_layout()
plt.title("Valor Total Realizado ao Longo do tempo")
plt.show()

# %%
df_realizado[['qtde_realizado','valor_unit_realizado', 'valor_total_realizado']].describe()

# %%
top_20_fornecedores = df_realizado['Cód. Fornecedor'].value_counts().sort_values(ascending=False).head(20)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=top_20_fornecedores.values,
    y=top_20_fornecedores.index,
    color='blue'
)
plt.tight_layout()
plt.title("Top 20 Fornecedores - Maior Frequência")
plt.show()

# Talvez o 42 venda concreto usinado...

# %%
fornecedores_mais_caros = df_realizado.groupby(by='Fornecedor')['categoria'].sum().sort_values(ascending=False)
fornecedores_mais_caros

plt.figure(figsize=(10, 6))

sns.barplot(
    x=fornecedores_mais_caros.values,
    y=fornecedores_mais_caros.index,
    color='blue'
)
plt.tight_layout()
plt.title("Top Fornecedores mais caro (1° Concreto Usinado)")
plt.show()

# %%
filtro = df_realizado['categoria'] == "Concreto Usinado"
df_filtrado = df_realizado[filtro]

print((df_filtrado['valor_total_realizado'].sum() / df_realizado['valor_total_realizado'].sum()) * 100)

# Aproximadamente 28% do Custo Total Realizado se oriunda da categoria Concreto Usinado, mesmo sendo o item mais caro