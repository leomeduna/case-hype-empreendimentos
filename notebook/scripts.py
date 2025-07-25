# %%
import pandas as pd

tabela_auxiliar = pd.read_csv("C:/case_hype/data/tabela_auxiliar.csv")
tabela_auxiliar

# %%
tabela_auxiliar = tabela_auxiliar.rename(columns={
    'Cód. Estruturado': 'cod_estruturado',
    'DescricaoItem': 'descricao_item',
    'Categoria': 'categoria'
})
tabela_auxiliar

# %%
tabela_auxiliar.to_parquet("tabela_auxiliar.parquet", index=False)