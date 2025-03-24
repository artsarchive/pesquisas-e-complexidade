import random 
import time

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def GerarVetor (size, limit, seq):
    random.seed(0)
    dados = []

    for i in range (size): 
        dados.append(random.randint(1, limit)) 
    
    return dados

def PesquisaLinear1 (number, dados):
    posicao = -1     
    found = False
    tam = len(dados)
    i = 0 

    while (i < tam) and (not(found)):
        if (dados[i] == number): 
            found = True
            posicao = i 
        i += 1

    result = [number, found, posicao, 0, 0]

    return result

def PesquisaLinear2 (number, dados):
    instrs = 4
    t = time.time() 

    found = False
    posicao = -1
    tam = len(dados)
    i = 0

    while (i < tam) and (not(found)):
        if (dados[i] == number): 
            found = True
            posicao = i
            instrs += 2
        i += 1
        instrs += 4
    
    t = time.time() - t
    result = [number, found, posicao, t, instrs] 

    return result

tam = 1000000
lim = 1000000
seq = 2
 
number = 794773

dados = GerarVetor (tam, lim, seq)
print(" Tamanho da lista: " + str(len(dados)))
print(" Lista: ")
print(dados[0:20])

posicao = 100000 # modificável 
chave = dados[posicao] 
print(" Valor e posição: " + str(number) + " - " + str(posicao))

print("\n Pesquisa Linear 1: ")
resultado1 = PesquisaLinear1(number, dados)
print(resultado1) 

print("\n Pesquisa Linear 2: ")
resultado2 = PesquisaLinear2(number, dados)
print(resultado2)

posicoes = [271591, 304882, 718546, 953722, 717312, 840963, 890963, 890594, 933231, 194746, 683682, 241759, 698547, 154309, 911455, 236101]

lstresults = []

for posicao in posicoes: 
    number = dados[posicao]
    result = PesquisaLinear2 (number, dados)
    lstresults.append(result)

df = pd.DataFrame(lstresults, columns = ['Chave', 'Existe', 'Posicao', 'Tempo', 'Instrucoes'])

sns.set_style("white")
plt.figure(figsize = (10, 10))

graf_linha = sns.lineplot(data = df, x = "Posicao", y = "Instrucoes", color = "red", marker = "*", markersize = 10, markers = "True")

plt.show()

