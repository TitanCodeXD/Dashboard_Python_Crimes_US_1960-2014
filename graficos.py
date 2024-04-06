# -*- coding: utf-8 -*-
"""Graficos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Assfw_i8etnNNLwRDgp-Q80YMGOW1xhA

# Código Para gerar os gráficos e dashboards
"""

import pandas as pd
import plotly.express as px

# Carregando a nossa base de dados, como está em csv, não precisaremos importar json, apenas o pandas para essa leitura.
caminho_arquivo = "US_Crime_Rates_1960_2014 1.csv"
df = pd.read_csv(caminho_arquivo)

#print(df)

### Análise inicial, mostrando a base de dados e explicações iniciais.

#Exibindo logo de início o total de crimes por todo o período
total_crimes = "{:,}".format(df['Total'].sum())
#print("Total de crimes:", total_crimes)

df['Ano'] = df['Ano'].dt.strftime('%Y')
#print(df)



display(df) #Display na base de dados para vizualização inicial

# Definir função para formatar números
def format_number(value):
    if value < 1000:
        return f'{value}'
    elif value < 1000000:
        return f'{value/1000:.1f} mil'
    else:
        return f'{value/1000000:.1f} milhões'

# Total Crimes formatada
#print("Total de crimes formatado:", format_number(total_crimes))

# prints de teste
#print("Primeiras linhas do DataFrame:")
#print(df.head())

# Total de Crimes violentos por ano
df_crimes_violentos_por_ano = df.groupby('Ano')[['Violento']].sum()
#print("Total de crimes violentos (Soma de Homicídio, Estupro, Roubo_Residência e Assalto_Agravante) por ano:")
#print(df_crimes_violentos_por_ano.applymap('{:,.0f}'.format))

# Total de Crimes de propriedade por ano
df_crimes_propriedade_por_ano = df.groupby('Ano')[['Propriedade']].sum()
#print("Total de crimes de propriedade (Soma de Furto_Residencial, Furto_Roubo_Geral, Roubo_Veículo) por ano:")
#print(df_crimes_propriedade_por_ano.applymap('{:,.0f}'.format))

# Total de Crimes por ano
df_crimes_por_ano = df.groupby('Ano')[['Total']].sum()
#print("Total de crimes por ano:")
#print(df_crimes_por_ano.applymap('{:,.0f}'.format))

# Convertendo a coluna 'Ano' para o tipo datetime
df['Ano'] = pd.to_datetime(df['Ano'], format='%Y')

# Calcular a soma de crimes para cada ano
df['Total_Crimes'] = df[['Propriedade', 'Homicidio', 'Estupro', 'Roubo_Residencia',
                          'Assalto_Agravante', 'Furto_Residencia', 'Furto_Roubo_Geral',
                          'Roubo_Veiculo']].sum(axis=1)

# Calcular a porcentagem de cada tipo de crime para cada ano
for col in ['Propriedade', 'Homicidio', 'Estupro', 'Roubo_Residencia',
            'Assalto_Agravante', 'Furto_Residencia', 'Furto_Roubo_Geral', 'Roubo_Veiculo']:
    df[col + '_Porcentagem'] = (df[col] / df['Total_Crimes']) * 100

# Representando por décadas, mas antes vamos usar o cut() para formatar como será lido o a coluna Ano, para ficar apenas os anos, desconsiderando dias e mees, nossa base possui apenas os anos
df['Decada'] = pd.cut(df['Ano'], bins=pd.interval_range(start=df['Ano'].min(), end=df['Ano'].max(), freq='10Y'))

# Agrupar os dados por década e calcular a média das porcentagens de cada tipo de crime
df_decadas = df.groupby('Decada').mean()

# Gráfico de pizza por década
def gerar_graficos_pizza(df_decadas):
    for decada, dados_decada in df_decadas.iterrows():
        labels = ['Propriedade', 'Homicidio', 'Estupro', 'Roubo_Residencia',
                  'Assalto_Agravante', 'Furto_Residencia', 'Furto_Roubo_Geral', 'Roubo_Veiculo']
        sizes = dados_decada[[col + '_Porcentagem' for col in labels]].tolist()
        fig = px.pie(names=labels, values=sizes)
        fig.update_traces(textinfo='percent+label')
        fig.update_layout(title=f'Porcentagem dos Crimes na Década de {decada.left.year}s')
        fig.show()

# Testando gráfico de pizza
#gerar_graficos_pizza(df_decadas);

#   ^ Comentando tudo com hashtag pois com aspas estava bugando

# Calcular a soma de crimes por década
df['Decada'] = pd.cut(df['Ano'], bins=pd.interval_range(start=df['Ano'].min(), end=df['Ano'].max(), freq='10Y'))
df_agrupado_decadas = df.groupby('Decada')['Total'].sum().reset_index()

# Converter os intervalos de década em strings
df_agrupado_decadas['Decada'] = df_agrupado_decadas['Decada'].astype(str)

# Criar o gráfico de barras
grafico_crimes_por_decada = px.bar(
    df_agrupado_decadas,
    x='Decada',
    y='Total',
    labels={'Total': 'Total de Crimes', 'Decada': 'Década'},
    title='Total de Crimes por Década'
)

# Atualizando gráfico apenas para deixar decrescente, facilitando para perceber qual década teve mais ou menos crimes
#grafico_crimes_por_decada.update_layout(xaxis={'categoryorder': 'total descending'},yaxis_title='Total de Crimes',xaxis_title='Década')

# Testando exibíção do gráfico
#grafico_crimes_por_decada.show()

# Calcular a soma de crimes e população para cada ano
df_agrupado = df.groupby('Ano').agg({'Populacao': 'sum', 'Total': 'sum'}).reset_index()

# Criar o gráfico de linha
grafico_crimes_populacao = px.line(
    df_agrupado,
    x='Ano',
    y=['Populacao', 'Total'],
    markers=True,
    range_y=(0, df_agrupado[['Populacao', 'Total']].values.max()),
    color_discrete_sequence=['blue', 'red'],
    title='Total de Crimes e População ao Longo do Tempo'
)

# Atualizar o layout do gráfico
#grafico_crimes_populacao.update_layout(yaxis_title='Quantidade',xaxis_title='Ano',legend_title='Tipo',hovermode='x unified')

# Testando exibição do gráfico
#grafico_crimes_populacao.show()
