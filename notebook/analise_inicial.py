# %%
# Análise inicial das bases de dados fornecidas no case. Investigar e criar notas em um Google Docs, ou um arquivo README.md
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %%
df_orcamento = pd.read_csv("C:/case_hype/data/Base_Orcamento.csv",encoding='latin1', sep=';')
df_realizado = pd.read_csv("C:/case_hype/data/Base_Realizado.csv",encoding='latin1', sep=';')
# %%
# Primeiros Passos:
# 1. Entender cada variável;
# 2. Criar notas sobre cada variável;
# 3. Por último, criar premissas/hipóteses para responder com as análises;
# %%
print(df_realizado.columns.value_counts().sum())
print(df_orcamento.columns.value_counts().sum())
# realizado: 16 colunas
# orçamento: 11 colunas 

# --------------------------------------------------------------------------------------------------

## Análise Inicial Base_Orcamento
# %%
# Analisando a distribuição de frequência da variável 'Grupo Orçamentário'
df_orcamento['Grupo Orçamentário'].value_counts().sort_values(ascending=False).head(20)
# %%
# Analisando a distribuição de frequência da variável 'Descrição Item'
df_orcamento['Descrição Item'].value_counts().sort_values(ascending=False).head(20)    
# %%
# Analisando a distribuição de frequência da variável 'Unid.' 
analise_unid = df_orcamento.groupby(by='Unid.')['Descrição Item'].value_counts()
pd.DataFrame(analise_unid)   
# exportando para analise rapida no excel
#analise_unid.to_excel("analise_unid.xlsx",index=True)
# %%
# Frequência da variável 'Categoria'
df_orcamento['Categoria'].value_counts().sort_values(ascending=False)    
# %%
# Analisando o agrupamento da variável Categoria para tentar encontrar padrão com a variável Unid.
categoria_unid = df_orcamento.groupby(by='Categoria')['Unid.'].value_counts()
pd.DataFrame(categoria_unid)
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
# Análise descritiva da variável ' Qtde. Insumo '
print(df_orcamento[' Qtde. Insumo '].describe())
print(df_orcamento[' Custo Insumo '].describe())
print(df_orcamento[' Total Orçado '].describe())

# %%
# Histograma para análise e após iremos dividir em bins...
plt.figure(figsize=(10, 6))

sns.histplot(
    x=df_orcamento[' Qtde. Insumo ']
)
plt.tight_layout()
plt.title("Histograma de Demanda")
plt.xlabel("Faixas de Demandas")
plt.ylabel("Frequências de Demandas")
plt.xlim(0, 5000)
plt.ylim(0, 800)
plt.show()
# %%
# Histograma para análise e após iremos dividir em bins...
plt.figure(figsize=(10, 6))

sns.histplot(
    x=df_orcamento[' Custo Insumo ']
)
plt.tight_layout()
plt.title("Histograma de Custo")
plt.xlabel("Faixas de Custo")
plt.ylabel("Frequências de Custo")
plt.xlim(0, 5000)
plt.ylim(0, 1000)
plt.show()
# %%
# Histograma para análise e após iremos dividir em bins...
plt.figure(figsize=(10, 6))

sns.histplot(
    x=df_orcamento[' Total Orçado ']
)
plt.tight_layout()
plt.title("Histograma de Total Orçado")
plt.xlabel("Faixas de Total Orçado")
plt.ylabel("Frequências de Total Orçado")
plt.xlim(0, 100000)
plt.ylim(0, 1000)
plt.show()
# %%
# Boxplot das variáveis numéricas
#sns.boxplot(
#    x=df_orcamento[' Qtde. Insumo ',
#                   ' Custo Insumo ',
#                   ' Total Orçado '],
#    data=df_orcamento,
#    color='orange'
#
#)

# -------------------------------------------------------------------------------------------------

## Análise Inicial Base_Realizado
# %%
