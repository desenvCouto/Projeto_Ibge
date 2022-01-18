#Importa biblioteca pandas
import pandas as pd

#Transforma a planilha em dados
data = pd.read_excel("secoes_ibge.xlsx")

#Realiza leitura das colunas e coloca o padrão lower
data['Secção'] = data['Secção'].str.lower()
data['Divisão'] = data['Divisão'].str.lower()

#Realiza leitura das colunas e remove os acentos
data['Secção'] = data['Secção'].str.normalize('NFKD').str.encode('ascii',errors='ignore').str.decode('utf-8')
data['Divisão'] = data['Divisão'].str.normalize('NFKD').str.encode('ascii',errors='ignore').str.decode('utf-8')

#Insere as informações tratadas na planilha novamente, acrescentando ID para vincula dos itenspy
data.to_excel("secoes_ibge.xlsx",
            sheet_name='Plan1')  
