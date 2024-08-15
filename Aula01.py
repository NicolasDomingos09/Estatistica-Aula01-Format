#Código escrito em estrutura tradicional para melhor entendimento

import numpy as np
import pandas as pd

#importar csv para dados
dados = pd.read_csv('CotacoesMoedasPeriodo.csv', sep = ';', encoding = 'UTF-8', header = None)

#.shape retorna tamanho
d = dados.shape
print(d, '\n')

#.columns dá a possibilidade de renomear as colunas de uma vez
dados.columns = ['datas', 'código', 'tipo', 'símbolo', 'compra', 'venda', 'ns1', 'ns2']

#.rename permite renomear algo específico
#dados = dados.rename(columns={'ns2': 'ns10'})

#.drop permite excluir um dado desejado
dados1 = dados.drop(columns = ['ns1', 'ns2'])

#usando função lambda para alterar elemento no texto/dado
dados1.compra = dados1.compra.apply(lambda x: x.replace(',', '.'))
dados1.venda = dados1.venda.apply(lambda x: x.replace(',', '.'))

#parse para float
dados1.compra.astype(float)
dados1.venda.astype(float)

#.dtypes serve para mostrar os tipos do objetivo ou variável
d = dados1.dtypes
print(d, '\n')

#head permite mostrar a estrutura atual do objeto (em formato de planilha)
d = dados1.head()
print (d, '\n')

#.to_csv salva o objeto em arquivo csv 
dados1.to_csv('dados_tratados_dolar.csv', encoding = 'iso-8859-1', index = False)