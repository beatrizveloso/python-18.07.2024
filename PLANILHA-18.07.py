import pandas as pd
excel = pd.read_excel("AULA 10 - 18_07 - PYTHON.xlsx")

# Variável 'mês' para controlar o fluxo de venda dos meses
mes = input("Qual mês você quer analisar? ")

# Retornar análise do vendedor do mês
# Ordena o mês
analise = excel.sort_values(by=f'{mes}',ascending=False)
print(analise)