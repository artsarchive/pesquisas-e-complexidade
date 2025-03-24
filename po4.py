import random
import time
import math

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Passo 1: 
def GerarVetor (size, limit):
    random.seed(0) 
    dados = []

    for i in range (size): 
        dados.append(random.randint(1, limit)) 
    
    return dados

# Passo 2: A função apresentada serve para ordenar os elementos dentro da lista. 
# Para analisarmos sua ordem de complexidade, precisamos analisar como o tempo de 
# execução ou o uso de recursos cresce em relação ao tamanho da entrada. 
# Normalmente, medimos usando o O(n), O(log n), por aí vai. 
# Percebemos que a função faz comparações com todos os elementos de um determinado 
# vetor, portanto, podemos considerar que sua ordem de complexidade seja O(log n)

# Passo 2: Respondendo as perguntas
# - A partir de uma análise breve do algoritmo, é possível notar que a função tem 
# objetivo parecido com o Bubble Sort, visando ordenar os elementos de um 
# determinado vetor.
# - A ordem de complexidade do Bubble Sort é de O(n²), em que n é o número de 
# elementos na lista; Acontece porque o algoritmo possui dois loops alinhados, em que 
# cada um percorre toda a lista.
# - Característica do problema que impacta no número de instruções: O tamanho (n) 
# certamente é o que impacta diretamente na performance do algoritmo. De acordo com o 
# conhecimento de Bubble Sort e os estudos realizados, sabemos que quanto maior for a 
# lista a ser ordenada, mais comparações e trocas serão feitas, o que é ineficiente. 
# 
# - Vamos contar as instruções usando a variável "instrs" no código.
# - Para medir o tempo, usaremos a biblioteca "time" apresentada anteriormente.
# - Para derivar a função de complexidade, vamos analisar o número de operações em 
# relação ao tamanho da entrada. 

# Ordem de complexidade: O(n²)
def OrdenarFuncao (dados): 
    last = len(dados) - 1
    instrs = 0
    t = time.time() 
    
    for i in range (last, 0, -1): 
        for j in range (0, i):
            instrs += 1
            if (dados[j] > dados[j + 1]): 
                aux = dados[j]
                dados[j] = dados[j + 1]
                dados[j + 1] = aux
                instrs += 3 

    tempo = time.time() - t
        
    rendimento = {
        'instrucoes' : instrs,
        'dados_ord' : dados,
        'tempo_execucao' : tempo
    }

    return rendimento
    
tam = 1000
lim = 1000

dados = GerarVetor (tam, lim)

print(" Tamanho da lista: " + str(len(dados)))
print(" Lista: ")
print(dados[0:20])

resultado = OrdenarFuncao (dados)

print(" Lista ordenada: " + str(resultado['dados_ord'][:20]))
print(" Instruções: " + str(resultado['instrucoes']))
print(" Tempo de execução: " + str(resultado['tempo_execucao']) + " segundos")
      
# De acordo com o estudo feito, quando o tamanho do vetor está em 1000, temos 
# cerca de 1.200.000 instruções, então: 
# (tamanho)     (instruções)
#   1000          1.200.000
#   100           12.000

posicoes = [10, 50, 100, 150, 500, 1000, 10000]

lstresults = []

for posicao in posicoes: 
    dados_teste = GerarVetor (posicao, lim)
    result = OrdenarFuncao (dados_teste)
    lstresults.append({
        'Tamanho' : posicao,
        'Instrucoes' : result['instrucoes'],
        'Tempo' : result['tempo_execucao']
    })

df = pd.DataFrame(lstresults, columns = ['Tamanho', 'Instrucoes', 'Tempo'])

sns.set_style("white")
plt.figure(figsize = (10, 6))

graf_linha = sns.lineplot(data = df, x = "Tamanho", y = "Instrucoes", color = "red", marker = "o", markersize = 8, markers = "True")

plt.grid(True)

plt.show()

# Passo 6
valores_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

linha = []
lstresults = []

for n in valores_n:
    vlog = math.log(n, 2)
    vn = n
    vn_2 = math.pow(n, 2)
    vn_3 = math.pow(n, 3)
    v2_n = math.pow(2, n)

    linha = [n, vlog, vn, vn_2, vn_3, v2_n]
    lstresults.append(linha)

print(lstresults)

df = pd.DataFrame(lstresults, columns = ['N', 'log_N', 'N_1', 'N_2', 'N_3', '2_N'])

sns.set_style("white")
plt.figure(figsize = (10, 10))

graf_linha = sns.lineplot(data = df, x = 'N', y = "log_N",
                          color = "red", marker = "*", markersize = 10,
                          markers = "True")
graf_linha = sns.lineplot(data = df, x = 'N', y = "N_1",
                          color = "blue", marker = "*", markersize = 10,
                          markers = "True")
graf_linha = sns.lineplot(data = df, x = 'N', y = "N_2",
                          color = "green", marker = "*", markersize = 10,
                          markers = "True")
graf_linha = sns.lineplot(data = df, x = 'N', y = "N_3",
                          color = "yellow", marker = "*", markersize = 10,
                          markers = "True")
graf_linha = sns.lineplot(data = df, x = 'N', y = "2_N",
                          color = "magenta", marker = "*", markersize = 10,
                          markers = "True")

plt.show()