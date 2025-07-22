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
# Ajustando a variável Qtde. Insumo para o tipo float, para depois analisar de forma descritiva 
df_orcamento[' Qtde. Insumo '] = df_orcamento[' Qtde. Insumo '].str.replace('.', '', regex=False)

print("Após remover o separador de milhares (ponto):")
print(df_orcamento[' Qtde. Insumo '])

df_orcamento[' Qtde. Insumo '] = df_orcamento[' Qtde. Insumo '].str.replace(',', '.', regex=False)

print("\nApós substituir a vírgula por ponto decimal:")
print(df_orcamento[' Qtde. Insumo '])

df_orcamento[' Qtde. Insumo '] = pd.to_numeric(df_orcamento[' Qtde. Insumo '], errors='coerce')

print("\nDataFrame Após Conversão Final:")
print(df_orcamento)
print("Dtype Final:", df_orcamento[' Qtde. Insumo '].dtype)
# %%
# Análise descritiva da variável ' Qtde. Insumo '
df_orcamento[' Qtde. Insumo '].describe()

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


