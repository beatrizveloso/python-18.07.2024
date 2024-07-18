# Criar uma tabela em Python e mandar para o Excel
import pandas as pd
import numpy as np

col = "Prova01 Prova02 Prova03 Prova04".split()
lin = "Beatriz Bianca Bianca Caio Claudemir Daniel Deivid Douglas Emerson Érika Euclides Fábio Fábricio Fernando Floriano Gary Guilherme Gustavo Henrique Jessica Juan Kauê Lucas Luciano Duda Matheus Miriam Sabrina".split()
notas = np.random.randint(1,11,112).reshape(28,4)
print(notas)

dados = pd.DataFrame(data =notas,index=lin,columns=col)
print(dados)

dados.to_excel("Notas_TurmaPython.xlsx")
dados.to