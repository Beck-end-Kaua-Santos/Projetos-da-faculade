import pandas as pd
import matplotlib.pyplot as plt

file_path = '2021.xlsx'
df = pd.read_excel(file_path)


print(df.head())

df['PERCENTUAL_OCUPACAO'] = (df['OCUPADA'] / df['APROVADA']) * 100  

df_sorted = df.sort_values(by='PERCENTUAL_OCUPACAO', ascending=False).head(5)

plt.figure(figsize=(8, 5))
plt.barh(df_sorted['SIGLA_ORGAO'], df_sorted['PERCENTUAL_OCUPACAO'], color='teal')
plt.xlabel('Percentual de Ocupação (%)')
plt.ylabel('Órgão')
plt.title('Top 5 Órgãos com Maior Percentual de Ocupação')
plt.gca().invert_yaxis()  
plt.tight_layout()
plt.show()

df_vagas = df.sort_values(by='VAGA', ascending=False).head(5)

plt.figure(figsize=(8, 5))
plt.barh(df_vagas['SIGLA_ORGAO'], df_vagas['VAGA'], color='salmon')
plt.xlabel('Número de Vagas')
plt.ylabel('Órgão')
plt.title('Top 5 Órgãos com Mais Vagas Disponíveis')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

file_path = '2021.xlsx'

data = pd.read_excel(file_path)

cargos_por_orgao = data.groupby('NOME_ORGAO')[['APROVADA', 'DISTRIBUIDA', 'OCUPADA', 'VAGA']].sum().sort_values(by='APROVADA', ascending=False)


top_10_orgao = cargos_por_orgao.head(10)
plt.figure(figsize=(12,8))
top_10_orgao[['APROVADA', 'OCUPADA', 'VAGA']].plot(kind='bar', stacked=True)
plt.title('Top 10 Órgãos com Maior Quantidade de Cargos Aprovados, Ocupados e Vagas')
plt.xlabel('Órgão')
plt.ylabel('Quantidade de Cargos')
plt.xticks(rotation=75)
plt.grid(True)
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

file_path = '2021.xlsx'
df = pd.read_excel(file_path)


df['PERCENTUAL_OCUPACAO'] = (df['OCUPADA'] / df['APROVADA']) * 100


df_lowest_percentual = df.sort_values(by='PERCENTUAL_OCUPACAO', ascending=True).head(10)


df_lowest_ocupada = df.sort_values(by='OCUPADA', ascending=True).head(10)


df_lowest_vaga = df.sort_values(by='VAGA', ascending=True).head(10)


plt.figure(figsize=(10, 6))
plt.barh(df_lowest_percentual['SIGLA_ORGAO'], df_lowest_percentual['PERCENTUAL_OCUPACAO'], color='lightblue')
plt.xlabel('Percentual de Ocupação (%)')
plt.ylabel('Órgão')
plt.title('Top 10 Órgãos com Menores Percentuais de Ocupação')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
plt.barh(df_lowest_ocupada['SIGLA_ORGAO'], df_lowest_ocupada['OCUPADA'], color='lightgreen')
plt.xlabel('Cargos Ocupados')
plt.ylabel('Órgão')
plt.title('Top 10 Órgãos com Menor Número de Cargos Ocupados')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
plt.barh(df_lowest_vaga['SIGLA_ORGAO'], df_lowest_vaga['VAGA'], color='lightcoral')
plt.xlabel('Número de Vagas Disponíveis')
plt.ylabel('Órgão')
plt.title('Top 10 Órgãos com Menor Número de Vagas Disponíveis')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'tabela.xlsx'
flie_path = '2021.xlsx'
df = pd.read_excel(file_path)
df = pd.read_excel(file_path)


print(df.head())

df['PERCENTUAL_OCUPACAO'] = (df['OCUPADA'] / df['APROVADA']) * 100  

df_sorted = df.sort_values(by='PERCENTUAL_OCUPACAO', ascending=False).head(5)

plt.figure(figsize=(8, 5))
plt.barh(df_sorted['SIGLA_ORGAO'], df_sorted['PERCENTUAL_OCUPACAO'], color='teal')
plt.xlabel('Percentual de Ocupação (%)')
plt.ylabel('Órgão')
plt.title('Top 5 Órgãos com Maior Percentual de Ocupação')
plt.gca().invert_yaxis()  
plt.tight_layout()
plt.show()

df_vagas = df.sort_values(by='VAGA', ascending=False).head(5)

plt.figure(figsize=(8, 5))
plt.barh(df_vagas['SIGLA_ORGAO'], df_vagas['VAGA'], color='salmon')
plt.xlabel('Número de Vagas')
plt.ylabel('Órgão')
plt.title('Top 5 Órgãos com Mais Vagas Disponíveis')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'tabela.xlsx'

data = pd.read_excel(file_path)

cargos_por_orgao = data.groupby('NOME_ORGAO')[['APROVADA', 'DISTRIBUIDA', 'OCUPADA', 'VAGA']].sum().sort_values(by='APROVADA', ascending=False)


top_10_orgao = cargos_por_orgao.head(10)
plt.figure(figsize=(12,8))
top_10_orgao[['APROVADA', 'OCUPADA', 'VAGA']].plot(kind='bar', stacked=True)
plt.title('Top 10 Órgãos com Maior Quantidade de Cargos Aprovados, Ocupados e Vagas')
plt.xlabel('Órgão')
plt.ylabel('Quantidade de Cargos')
plt.xticks(rotation=75)
plt.grid(True)
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'tabela.xlsx'
df = pd.read_excel(file_path)


df['PERCENTUAL_OCUPACAO'] = (df['OCUPADA'] / df['APROVADA']) * 100


df_lowest_percentual = df.sort_values(by='PERCENTUAL_OCUPACAO', ascending=True).head(10)


df_lowest_ocupada = df.sort_values(by='OCUPADA', ascending=True).head(10)


df_lowest_vaga = df.sort_values(by='VAGA', ascending=True).head(10)


plt.figure(figsize=(10, 6))
plt.barh(df_lowest_percentual['SIGLA_ORGAO'], df_lowest_percentual['PERCENTUAL_OCUPACAO'], color='lightblue')
plt.xlabel('Percentual de Ocupação (%)')
plt.ylabel('Órgão')
plt.title('Top 10 Órgãos com Menores Percentuais de Ocupação')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
plt.barh(df_lowest_ocupada['SIGLA_ORGAO'], df_lowest_ocupada['OCUPADA'], color='lightgreen')
plt.xlabel('Cargos Ocupados')
plt.ylabel('Órgão')
plt.title('Top 10 Órgãos com Menor Número de Cargos Ocupados')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
plt.barh(df_lowest_vaga['SIGLA_ORGAO'], df_lowest_vaga['VAGA'], color='lightcoral')
plt.xlabel('Número de Vagas Disponíveis')
plt.ylabel('Órgão')
plt.title('Top 10 Órgãos com Menor Número de Vagas Disponíveis')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo de dados
file_path = 'tabela.xlsx'
data = pd.read_excel(file_path)

# Converter a coluna 'ANO_MES' para datetime e extrair o ano
data['ANO_MES'] = pd.to_datetime(data['ANO_MES'], format='%Y%m')
data['Ano'] = data['ANO_MES'].dt.year

def comparar_anos(df, ano1, ano2):
    dados_ano1 = df[df['Ano'] == ano1]
    dados_ano2 = df[df['Ano'] == ano2]

    # Agrupar e somar os dados por órgão
    cargos_ano1 = dados_ano1.groupby('NOME_ORGAO')[['APROVADA', 'DISTRIBUIDA', 'OCUPADA', 'VAGA']].sum()
    cargos_ano2 = dados_ano2.groupby('NOME_ORGAO')[['APROVADA', 'DISTRIBUIDA', 'OCUPADA', 'VAGA']].sum()

    # Juntar os dados para comparação
    comparacao = cargos_ano2.join(cargos_ano1, lsuffix=f'_{ano2}', rsuffix=f'_{ano1}')

    # Selecionar os 10 órgãos com mais cargos aprovados em ano2 para comparação
    comparacao_top_10 = comparacao.sort_values(by=f'APROVADA_{ano2}', ascending=False).head(10)

    # Plotar a comparação
    comparacao_top_10[[f'APROVADA_{ano2}', f'APROVADA_{ano1}']].plot(kind='bar', figsize=(14, 7))
    plt.title(f'Comparação de Cargos Aprovados entre {ano2} e {ano1} nos Top 10 Órgãos')
    plt.xlabel('Órgão')
    plt.ylabel('Quantidade de Cargos Aprovados')
    plt.xticks(rotation=75)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


