# %%
# Análise inicial das bases de dados fornecidas no case. Investigar e criar notas em um Google Docs, ou um arquivo README.md
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

