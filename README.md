# Case de Análise de Dados - Hype Empreendimentos

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo principal demonstrar a capacidade de transformar dados brutos de orçamentos e custos realizados de uma obra em inteligência de negócio, fornecendo insights acionáveis para otimizar a tomada de decisões, reduzir desperdícios e aumentar a eficiência operacional na Hype Empreendimentos.

## 📁 Estrutura do Repositório

O repositório está organizado de forma a facilitar a compreensão e replicação do projeto:

* **`data/`**: Contém os arquivos de dados brutos (`Base_Orcamento.csv` e `Base_Realizado.csv`) utilizados na análise.
* **`notebook/`**: Armazena o script Python responsável pela etapa de ETL (Extração, Transformação e Carga), incluindo o tratamento, limpeza e a junção das bases de dados.
* **`reports/`**: Guarda o arquivo `.pbix` do Power BI contendo o dashboard interativo desenvolvido para visualização dos dados e exploração dos insights.
* **`README.md`**: Este arquivo, que fornece uma visão geral do projeto, suas etapas e os resultados.

## 🛠️ Tecnologias Utilizadas

* **Python**: Para a etapa de tratamento e unificação dos dados. Bibliotecas como `pandas`, `numpy` e `matplotlib.pyplot` serão amplamente utilizadas.
* **Power BI**: Para a criação do dashboard interativo e as visualizações de dados.
* **Git & GitHub**: Para controle de versão e hospedagem do projeto.
 
## 📊 Resultados da Análise

Com base na análise realizada no dashboard, foram identificados insights relevantes para a gestão de custos:

- Os KPIs apontaram uma **economia de R$1.079.362** no total realizado.
- As unidades **M3 e KG** concentraram os maiores custos, somando **R$1.963.768**.
- Fornecedores com baixa frequência, como os de códigos **80 e 15**, apresentaram altos custos, sugerindo a necessidade de buscar alternativas mais econômicas.
- A categoria **Elétrica – Fios e Cabos** excedeu o orçamento em **R$53.853**, enquanto **Mão de Obra de Pintura** gerou economia expressiva de **R$407.720**.
- O **Concreto Usinado**, responsável por **28% do custo total**, e a **Locação de Equipamentos Pesados** (com apenas 15 execuções), ultrapassaram o orçamento em **R$32.377**, representando cerca de **11% do valor total**.
- A categoria **Aço e Acessórios** teve grande representatividade em volume adquirido e peso no orçamento.
- As categorias que extrapolaram o orçamento foram: **Concreto Usinado**, **Elétrica – Fios e Cabos** e **Locação de Equipamentos Pesados**.
- Em termos de quantidade adquirida, **Elétrica – Fios e Cabos** e **Aço e Acessórios** também superaram o previsto.
- Itens como **Concreto Usinado** e **Locação de Pesados**, mesmo com baixa frequência, estão entre os mais onerosos.

Os **gráficos de Pareto** revelaram que cinco categorias concentram mais de **70% dos custos**, indicando a necessidade de foco estratégico nestes itens.

### 📌 Recomendações:

1. Revisar contratos com fornecedores que apresentaram desvios significativos de custo;
2. Implementar um painel de controle contínuo para monitoramento de gastos;
3. Manter foco estratégico nas categorias mais onerosas, com controle mais rigoroso sobre itens de alto custo unitário e baixa frequência.

Apesar dos custos elevados em algumas categorias, o **cronograma de execução foi mantido**, evidenciando **eficiência na alocação dos recursos**.

## 🔗 Conecte-se Comigo

* **LinkedIn**: [linkedin.com/in/leonardo-meduna](https://www.linkedin.com/in/leonardo-meduna)
* **GitHub**: [github.com/leomeduna](https://github.com/leomeduna)