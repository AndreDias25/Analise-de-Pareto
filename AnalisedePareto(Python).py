#3 bibliotecas: 

import collections                    #collections para contar as repetições(duplicata) de strings 
from itertools import groupby         #groupby para ordenar strings de forma decrescente pela repetição
import pandas as pd                   #pandas para geração de tabela indentada dos dados

#Entrada do arquivo .txt

print("Ocorrencias:\n")
Ocorrencias = []
Entrada = open("Professor_notas.txt", "r")         #Cria-se uma lista que recebe uma abertura do arquivo e todas as
Ocorrencias = Entrada.readlines()        #suas linhas
#print(Ocorrencias)


#Contagem das duplicatas

print("\nNumero de repeticoes:\n")               #A biblioteca collections faz a contagem das repetições
repeticoes = collections.Counter(Ocorrencias)    # de strings(ocorrências)
print(repeticoes)


Entrada.close()

#Contagem dos valores das ocorrências

total = sum(map(lambda repeticoes:float(repeticoes),repeticoes.values()))
print("\nSoma de ocorrencias:",total,"\n")

#Ordenação decrescente dos nomes das ocorrências.

Nomes = []
results = {value: len(list(freq)) for value, freq in groupby(sorted(Ocorrencias))} 
for i in sorted(results, key = results.get, reverse=True):
    Nomes.append(i) 

print("Nomes:",Nomes)

#Ordenação decrescente dos valores de ocorrências

listateste = []
listateste = repeticoes.values()

ocorrencias = []

ocorrencias.extend(listateste)

ocorrencias.sort(reverse=True)
print("Ocorrencias:",ocorrencias) 

#Percentual das ocorrências

frequencia = []

 
for item1 in ocorrencias:
    item1 = (item1/total)*100
    item1 = round(item1, 2) 
    frequencia.append(item1)

print("Frequencia:",frequencia) 

#Percentual acumulado das ocorrências

acumulada = []

item2 = 0
item3 = 0
for item3 in frequencia:
    item3 = item3 + item2
    item2 = item3
    item3 = round(item3, 2)
    acumulada.append(item3) 

print("Frequencia Acumulada:",acumulada,"\n")

#Criação da tabela

print("=====================================ANALISE DE PARETO(TABELA)=====================================")

table = pd.DataFrame()
table["Nomes"] = Nomes
table["Ocorrencias"] = ocorrencias
table["fr(%)"] = frequencia
table["Fac(%)"] = acumulada
print(table)

print("\n===================================TOTAL DAS OCORRENCIAS:",total,"====================================")

