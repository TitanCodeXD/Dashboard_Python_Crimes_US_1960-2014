import streamlit as st
from graficos import df, df_decadas, df_agrupado_decadas, grafico_crimes_por_decada

st.set_page_config(layout='wide')
st.title("Dashboard de Crimes nos Estados Unidos 1960 - 2014  :gun: :mag:")

st.sidebar.title('Filtro de Ano :round_pushpin:')
filtro_ano = st.sidebar.multiselect(
    'Ano',
    df['Ano'].unique(),
)
if filtro_ano:
    df = df[df['Ano'].isin(filtro_ano)]

aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs(['Dataset', 'Crimes por Ano', 'Porcentagem de Crimes por todo o Período em Décadas',
                                             'Crimes Violentos', 'População x Crimes', 'Década mais perigosa'])

colunas_para_exibir = ['Ano', 'Populacao', 'Total', 'Violento', 'Propriedade', 'Homicidio', 'Estupro', 'Roubo_Residencia',
                       'Assalto_Agravante', 'Furto_Residencia', 'Furto_Roubo_Geral', 'Roubo_Veiculo']

def gerar_graficos_pizza1(df_decadas):
    for decada, dados_decada in df_decadas.iterrows():
        labels = ['Propriedade', 'Homicidio', 'Estupro', 'Roubo_Residencia',
                  'Assalto_Agravante', 'Furto_Residencia', 'Furto_Roubo_Geral', 'Roubo_Veiculo']
        sizes = dados_decada[[col + '_Porcentagem' for col in labels]].tolist()
        fig = px.pie(names=labels, values=sizes)
        fig.update_traces(textinfo='percent+label')
        fig.update_layout(title=f'Porcentagem dos Crimes na Década de {decada.left.year}s', height=700, width=1100)
        st.plotly_chart(fig)

def gerar_graficos_pizza_violentos(df_decadas_violentos):
    for decada, dados_decada in df_decadas_violentos.iterrows():
        labels = ['Homicidio', 'Estupro', 'Roubo_Residencia', 'Assalto_Agravante']
        sizes = dados_decada.tolist()
        fig = px.pie(names=labels, values=sizes)
        fig.update_traces(textinfo='percent+label')
        fig.update_layout(title=f'Porcentagem dos Crimes Violentos na Década de {decada.left.year}s', height=700, width=1100)
        st.plotly_chart(fig)

with aba1:
  st.markdown("### Algumas informações sobre determinadas colunas específicas:")
  st
