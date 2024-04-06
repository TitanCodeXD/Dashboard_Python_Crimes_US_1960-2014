{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# **CÓDIGO PARA PEGAR OS DADOS DE DASHBOARD E GRÁFICOS E EXIBIR**"
      ],
      "metadata": {
        "id": "3i9NRiQeBkA1"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fIhF8oUaBbsB",
        "outputId": "0b6e0c6b-c278-4fec-8345-72bce425eb87"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.1/8.1 MB\u001b[0m \u001b[31m17.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m207.3/207.3 kB\u001b[0m \u001b[31m17.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.8/4.8 MB\u001b[0m \u001b[31m30.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m83.0/83.0 kB\u001b[0m \u001b[31m6.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m4.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[K\u001b[?25h\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m \u001b[0m\u001b[35msaveError\u001b[0m ENOENT: no such file or directory, open '/content/package.json'\n",
            "\u001b[K\u001b[?25h\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[34;40mnotice\u001b[0m\u001b[35m\u001b[0m created a lockfile as package-lock.json. You should commit this file.\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m \u001b[0m\u001b[35menoent\u001b[0m ENOENT: no such file or directory, open '/content/package.json'\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m\u001b[35m\u001b[0m content No description\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m\u001b[35m\u001b[0m content No repository field.\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m\u001b[35m\u001b[0m content No README data\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m\u001b[35m\u001b[0m content No license field.\n",
            "\u001b[0m\n",
            "+ localtunnel@2.0.2\n",
            "added 22 packages from 22 contributors and audited 22 packages in 2.624s\n",
            "\n",
            "3 packages are looking for funding\n",
            "  run `npm fund` for details\n",
            "\n",
            "found 1 \u001b[93mmoderate\u001b[0m severity vulnerability\n",
            "  run `npm audit fix` to fix them, or `npm audit` for details\n",
            "\u001b[K\u001b[?25hSENHA/Enpoint IP para o túnel local: 34.139.213.187\n"
          ]
        }
      ],
      "source": [
        "!pip install -q streamlit\n",
        "!npm install localtunnel\n",
        "\n",
        "import urllib\n",
        "\n",
        "print(\"SENHA/Enpoint IP para o túnel local:\",urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip(\"\\n\"))\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "%%writefile app.py\n",
        "\n",
        "import streamlit as st\n",
        "from graficos import *\n",
        "\n",
        "st.set_page_config(layout='wide')\n",
        "st.title(\"Dashboard de Crimes nos Estados Unidos 1960 - 2014  :gun: :mag:\")\n",
        "\n",
        "st.sidebar.title('Filtro de Ano :round_pushpin:')\n",
        "filtro_ano = st.sidebar.multiselect(\n",
        "'Ano',\n",
        "df['Ano'].unique(),\n",
        ")\n",
        "if filtro_ano:\n",
        "  df = df[df['Ano'].isin(filtro_ano)]\n",
        "\n",
        "\n",
        "aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs(['Dataset', 'Crimes por Ano','Porcentagem de Crimes por todo o Período em Décadas', 'Crimes Violentos','População x Crimes','Década mais perigosa'])\n",
        "\n",
        "\n",
        "colunas_para_exibir = ['Ano', 'Populacao', 'Total', 'Violento', 'Propriedade', 'Homicidio', 'Estupro', 'Roubo_Residencia', 'Assalto_Agravante',\n",
        "                       'Furto_Residencia', 'Furto_Roubo_Geral', 'Roubo_Veiculo']\n",
        "\n",
        "def gerar_graficos_pizza1(df_decadas):\n",
        "    for decada, dados_decada in df_decadas.iterrows():\n",
        "        labels = ['Propriedade', 'Homicidio', 'Estupro', 'Roubo_Residencia',\n",
        "                  'Assalto_Agravante', 'Furto_Residencia', 'Furto_Roubo_Geral', 'Roubo_Veiculo']\n",
        "        sizes = dados_decada[[col + '_Porcentagem' for col in labels]].tolist()\n",
        "        fig = px.pie(names=labels, values=sizes)\n",
        "        fig.update_traces(textinfo='percent+label')\n",
        "        fig.update_layout(title=f'Porcentagem dos Crimes na Década de {decada.left.year}s', height=700, width=1100)\n",
        "        st.plotly_chart(fig)\n",
        "\n",
        "def gerar_graficos_pizza_violentos(df_decadas_violentos):\n",
        "    for decada, dados_decada in df_decadas_violentos.iterrows():\n",
        "        labels = ['Homicidio', 'Estupro', 'Roubo_Residencia', 'Assalto_Agravante']\n",
        "        sizes = dados_decada.tolist()\n",
        "        fig = px.pie(names=labels, values=sizes)\n",
        "        fig.update_traces(textinfo='percent+label')\n",
        "        fig.update_layout(title=f'Porcentagem dos Crimes Violentos na Década de {decada.left.year}s', height=700, width=1100)\n",
        "        st.plotly_chart(fig)\n",
        "\n",
        "with aba1:\n",
        "  st.markdown(\"### Algumas informações sobre determinadas colunas específicas:\")\n",
        "  st.markdown(\"- **Violento**: Total de Crimes violentos naquele Ano (Soma de Homicídio, Estupro, Roubo_Residência e Assalto_Agravante)\")\n",
        "  st.markdown(\"- **Propriedade**: Total de Crimes à Propriedade (Soma de Furto_Residencial, Furto_Roubo_Geral, Roubo_Veículo)\")\n",
        "  st.markdown(\"- **Total**:  Total de Crimes no Geral naquele Ano (Soma de Violento e Propriedade)\")\n",
        "  st.dataframe(df[colunas_para_exibir])\n",
        "\n",
        "with aba2:\n",
        " coluna1, coluna2, coluna3 = st.columns(3)\n",
        " with coluna1:\n",
        "      st.metric('Crimes violentos por ano', format_number(df['Violento'].sum()))\n",
        "      df_crimes_violentos_por_ano\n",
        " with coluna2:\n",
        "      st.metric('Crimes de Propriedade por Ano', format_number(df['Propriedade'].sum()))\n",
        "      df_crimes_propriedade_por_ano\n",
        " with coluna3:\n",
        "      st.metric('Total de Crimes por ano', format_number(df['Total'].sum()))\n",
        "      df_crimes_por_ano\n",
        "\n",
        "with aba3:\n",
        "  gerar_graficos_pizza1(df_decadas)\n",
        "\n",
        "with aba4:\n",
        "  gerar_graficos_pizza_violentos(df_decadas_violentos)\n",
        "\n",
        "with aba5:\n",
        "  st.plotly_chart(grafico_crimes_populacao, use_container_width=True)\n",
        "\n",
        "with aba6:\n",
        "  st.plotly_chart(grafico_crimes_por_decada, use_container_width=True)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZgCis0k5Bqld",
        "outputId": "d7b42c57-8a27-44c2-eca7-575504994763"
      },
      "execution_count": 90,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app.py &>/content/logs.txt & npx localtunnel --port 8501"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Rpq3Pe5UCKdB",
        "outputId": "e72411ad-c419-4f8c-d1bb-d07cf9864d1d"
      },
      "execution_count": 91,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[K\u001b[?25hnpx: installed 22 in 3.184s\n",
            "your url is: https://every-cases-yawn.loca.lt\n",
            "^C\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "34.139.213.187"
      ],
      "metadata": {
        "id": "i-S8E_CqSrAe"
      }
    }
  ]
}
