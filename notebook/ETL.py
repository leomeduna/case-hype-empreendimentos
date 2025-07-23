# %%

import pandas as pd
import numpy as np

# %%
df_orcamento = pd.read_csv("C:/case_hype/data/Base_Orcamento.csv",encoding='latin1', sep=';')
df_realizado = pd.read_csv("C:/case_hype/data/Base_Realizado.csv",encoding='latin1', sep=';')

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
    # 1. Remover o separador de milhares (o ponto '.')
    # Usar .astype(str) para garantir que seja string antes de aplicar .str
    coluna_limpa = coluna_series.astype(str).str.replace('.', '', regex=False)

    # 2. Substituir o separador decimal (a vírgula ',') por um ponto '.'
    coluna_limpa = coluna_limpa.str.replace(',', '.', regex=False)

    # 3. Converter para numérico
    coluna_final_numerica = pd.to_numeric(coluna_limpa, errors='coerce')

    return coluna_final_numerica

# --- Aplicando a função às colunas desejadas ---
orcamento_colunas_para_converter = ['custo_insumo', 'qtde_insumo', 'total_orcado']
realizado_colunas_para_converter = ['qtde_realizado', 'valor_unit_realizado', 'valor_total_realizado']

for col in orcamento_colunas_para_converter:
    df_orcamento[col] = conversao_coluna_str_to_float(df_orcamento[col])

for col in realizado_colunas_para_converter:
    df_realizado[col] = conversao_coluna_str_to_float(df_realizado[col])


# %%
analytical_base_table = df_realizado.merge(right=df_orcamento, on=['cod_estruturado', 'descricao_item'], how='left')
analytical_base_table.info()
# %%
rename_mapping = {
    'descricao_item_x': 'descricao_realizado',
    'descricao_item_y': 'descricao_orcado',
    'obra_x': 'obra_realizado',
    'obra_y': 'obra_orcado',
    'cod_item_x': 'cod_item_realizado',
    'cod_item_y': 'cod_item_orcado',
    'unid_x': 'unid_realizado',
    'unid_y': 'unid_orcado',
    'categoria_x': 'categoria_realizado',
    'categoria_y': 'categoria_orcado',
    'Tipo_x': 'tipo_realizado',
    'Tipo_y': 'tipo_orcado',   
}
analytical_base_table.rename(columns=rename_mapping, inplace=True)

# %%
analytical_base_table['desvio_abs_qtde'] = analytical_base_table['qtde_realizado'] - analytical_base_table['qtde_insumo']
analytical_base_table['desvio_abs_custo_unit'] = analytical_base_table['valor_unit_realizado'] - analytical_base_table['custo_insumo']
analytical_base_table['desvio_abs_custo_total'] = analytical_base_table['valor_total_realizado'] - analytical_base_table['total_orcado']

# %%
# Desvio percentual de quantidade
analytical_base_table['desvio_perc_qtde'] = np.where(
    analytical_base_table['qtde_insumo'] != 0,
    (analytical_base_table['qtde_realizado'] - analytical_base_table['qtde_insumo']) / analytical_base_table['qtde_insumo'],
    np.nan  
)

# Desvio percentual de custo unitário
analytical_base_table['desvio_perc_custo_unit'] = np.where(
    analytical_base_table['custo_insumo'] != 0,
    (analytical_base_table['valor_unit_realizado'] - analytical_base_table['custo_insumo']) / analytical_base_table['custo_insumo'],
    np.nan
)

# Desvio percentual de custo total
analytical_base_table['desvio_perc_custo_total'] = np.where(
    analytical_base_table['total_orcado'] != 0,
    (analytical_base_table['valor_total_realizado'] - analytical_base_table['total_orcado']) / analytical_base_table['total_orcado'],
    np.nan
)

# %%
# Eficiência de CUSTO
analytical_base_table['eficiencia_custo'] = analytical_base_table['total_orcado'] / analytical_base_table['valor_total_realizado']
# Eficiência de QUANTIDADE
analytical_base_table['eficiencia_qtde'] = analytical_base_table['qtde_insumo'] / analytical_base_table['qtde_realizado']

# %%
# "Ticket Médio" 
analytical_base_table['ticket_realizado'] = analytical_base_table['valor_total_realizado'] / analytical_base_table['qtde_realizado']
analytical_base_table['ticket_orcado'] = analytical_base_table['total_orcado'] / analytical_base_table['qtde_insumo']

# %%
analytical_base_table['eficiencia_geral'] = analytical_base_table['total_orcado'] / analytical_base_table['valor_total_realizado']

# %%
analytical_base_table.to_parquet("analytical_base_table.parquet", index=False)
