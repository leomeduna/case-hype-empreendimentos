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
    coluna_limpa = coluna_series.astype(str).str.replace('.', '', regex=False)

    coluna_limpa = coluna_limpa.str.replace(',', '.', regex=False)

    coluna_final_numerica = pd.to_numeric(coluna_limpa, errors='coerce')

    return coluna_final_numerica

orcamento_colunas_para_converter = ['custo_insumo', 'qtde_insumo', 'total_orcado']
realizado_colunas_para_converter = ['qtde_realizado', 'valor_unit_realizado', 'valor_total_realizado']

for col in orcamento_colunas_para_converter:
    df_orcamento[col] = conversao_coluna_str_to_float(df_orcamento[col])

for col in realizado_colunas_para_converter:
    df_realizado[col] = conversao_coluna_str_to_float(df_realizado[col])

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
total_orcado_p_categoria = df_orcamento.groupby(by='categoria')['total_orcado'].sum().sort_values(ascending=False)
total_orcado_p_categoria

plt.figure(figsize=(10, 6))

sns.barplot(
    x=total_orcado_p_categoria.values,
    y=total_orcado_p_categoria.index,
    color='green'
)
plt.tight_layout()
plt.title("Soma de Custos por Categoria")
plt.show()

# %%
total_orcado_p_grupo_orc = df_orcamento.groupby(by='grupo_orcamentario')['total_orcado'].sum().sort_values(ascending=False)
top_20_custo_p_grupo = total_orcado_p_grupo_orc.head(20)

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
total_orcado_p_desc_item = df_orcamento.groupby(by='descricao_item')['total_orcado'].sum().sort_values(ascending=False)
top_20_total_orcado_p_desc_item = total_orcado_p_desc_item.head(20)

plt.figure(figsize=(14, 8))

sns.barplot(
    x=top_20_total_orcado_p_desc_item.values,
    y=top_20_total_orcado_p_desc_item.index,
    color='green'
)
plt.tight_layout()
plt.title("Top 20 Itens mais Custosos")
plt.show()

# %%
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
colunas_para_converter_realizado = [' ValorUnitRealizado ', ' Qtd Realizada ', ' ValorTotalRealizado ']

for col in colunas_para_converter_realizado:
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
total_realizado_p_categoria = df_realizado.groupby(by='categoria')['valor_total_realizado'].sum().sort_values(ascending=False)
total_realizado_p_categoria

plt.figure(figsize=(10, 6))

sns.barplot(
    x=total_realizado_p_categoria.values,
    y=total_realizado_p_categoria.index,
    color='green'
)
plt.tight_layout()
plt.title("Realizado - Soma de Custos por Categoria")
plt.show()

# %%
total_realizado_p_desc_item = df_realizado.groupby(by='descricao_item')['valor_total_realizado'].sum().sort_values(ascending=False)
realizado_top_20_total_orcado_p_desc_item = total_realizado_p_desc_item.head(20)

plt.figure(figsize=(14, 8))

sns.barplot(
    x=realizado_top_20_total_orcado_p_desc_item.values,
    y=realizado_top_20_total_orcado_p_desc_item.index,
    color='green'
)
plt.tight_layout()
plt.title("Realizado - Top 20 Itens mais Custosos")
plt.show()

# %%
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

# %%
realizado_agregado_categoria = df_realizado.groupby('descricao_item').agg(
    qtde_realizado=('qtde_realizado', 'sum'),
    valor_unit_realizado=('valor_unit_realizado', 'mean'),
    valor_total_realizado=('valor_total_realizado', 'sum')
).reset_index()

orcamento_agregado_item = df_orcamento.groupby('descricao_item').agg(
    qtde_insumo=('qtde_insumo', 'sum'),
    custo_insumo=('custo_insumo', 'mean'), 
    total_orcado=('total_orcado', 'sum')
).reset_index()

sumario_desc_item = pd.merge(realizado_agregado_categoria, orcamento_agregado_item, on='descricao_item', how='outer')

sumario_desc_item['desvio_qtde'] = sumario_desc_item['qtde_realizado'] - sumario_desc_item['qtde_insumo']
sumario_desc_item['desvio_custo_unit'] = sumario_desc_item['valor_unit_realizado'] - sumario_desc_item['custo_insumo']
sumario_desc_item['desvio_total'] = sumario_desc_item['valor_total_realizado'] - sumario_desc_item['total_orcado']

sumario_desc_item.sort_values(by='desvio_total', ascending=False) 

# %%
realizado_agregado_categoria = df_realizado.groupby('categoria').agg(
    qtde_realizado=('qtde_realizado', 'sum'),   
    valor_unit_realizado=('valor_unit_realizado', 'sum'), 
    valor_total_realizado=('valor_total_realizado', 'sum')
).reset_index()

orcamento_agregado_categoria = df_orcamento.groupby('categoria').agg(
    qtde_insumo=('qtde_insumo', 'sum'),
    custo_insumo=('custo_insumo', 'sum'), 
    total_orcado=('total_orcado', 'sum')
).reset_index()

sumario_desc_categoria = pd.merge(realizado_agregado_categoria, orcamento_agregado_categoria, on='categoria', how='outer')

sumario_desc_categoria = sumario_desc_categoria.fillna(0)

sumario_desc_categoria['desvio_qtde'] = sumario_desc_categoria['qtde_insumo'] - sumario_desc_categoria['qtde_realizado']
sumario_desc_categoria['desvio_custo_unit'] = sumario_desc_categoria['custo_insumo'] - sumario_desc_categoria['valor_unit_realizado']
sumario_desc_categoria['desvio_total'] = sumario_desc_categoria['total_orcado'] - sumario_desc_categoria['valor_total_realizado']
sumario_desc_categoria['desvio_perc_qtde'] =  (sumario_desc_categoria['qtde_insumo'] - sumario_desc_categoria['qtde_realizado']) / sumario_desc_categoria['qtde_insumo']
sumario_desc_categoria['desvio_perc_custo_unit'] =  (sumario_desc_categoria['custo_insumo'] - sumario_desc_categoria['valor_unit_realizado']) / sumario_desc_categoria['custo_insumo']
sumario_desc_categoria['desvio_perc_total'] =  (sumario_desc_categoria['total_orcado'] - sumario_desc_categoria['valor_total_realizado']) / sumario_desc_categoria['total_orcado']


sumario_desc_categoria.sort_values(by='desvio_total', ascending=False) 

# %%
sumario_desc_item.to_parquet("sumario_descricao_item.parquet", index=False)
sumario_desc_categoria.to_parquet("sumario_categoria.parquet", index=False)