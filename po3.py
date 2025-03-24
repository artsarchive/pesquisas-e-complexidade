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

def PesquisaBinaria (dados_ord, alvo):
    instr = 0
    t = time.time() 

    found = False
    posicao = -1
    chave = -1

    low = 0 
    high = len(dados_ord) - 1

    while low <= high: 
        instr += 1
        mid = (low + high) // 2

        if (dados_ord[mid] == alvo): 
            found = True
            posicao = mid
            chave = dados_ord[mid]
            break
        elif (dados_ord[mid] < alvo): 
            low = mid + 1
        else: 
            high = mid - 1

    tempo = time.time() - t

    result = [chave, found, posicao, tempo, instr]

    return result
    # chave, boolean, posição, tempo, instruções

tam = 1000000
lim = 1000000
seq = 2

dados = GerarVetor (tam, lim, seq)

print(" Tamanho da lista: " + str(len(dados)))
print(" Lista: ")
print(dados[0:20])

dados_ord = sorted(dados) 
print(dados_ord[1:100])

posicao = 100000
chave = dados_ord[posicao]
print(" Valor e posição: " + str(chave) + " - " + str(posicao))

result = PesquisaBinaria (dados_ord, chave)
print(result)

# anotar os dados conforme as posicoes, praticidade ne pai
posicoes = [271591, 304882, 718546, 953722, 717312, 840963, 890963, 890594, 933231, 194746, 683682, 241759, 698547, 154309, 911455, 236101]

lstresults = []

for posicao in posicoes: 
    chave = dados[posicao]
    result = PesquisaBinaria (dados_ord, chave)
    lstresults.append(result)

df = pd.DataFrame(lstresults, columns = ['Chave', 'Existe', 'Posicao', 'Tempo', 'Instrucoes'])

sns.set_style("white")
plt.figure(figsize = (10, 10))

graf_linha = sns.lineplot(data = df, x = "Posicao", y = "Instrucoes", color = "red", marker = "*", markersize = 10, markers = "True")

plt.show()
