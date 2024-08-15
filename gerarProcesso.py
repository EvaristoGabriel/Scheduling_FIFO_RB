import random
n_processos = int(input("Quantos processos deseja criar: "))
entrada_limite = int(input("Qual o tempo de entrada limite: "))
execucao_limite = int(input("Qual o tempo de execução limite: "))
arq = open("processos.txt",'w')

tempo_execucao = random.randint(0,execucao_limite)
priority = random.randint(0,n_processos/2) 
arq.write(f"Processo 1: 0,{tempo_execucao},{priority}\n")

for i in range(2,n_processos+1):
    tempo_entrada = random.randint(0,entrada_limite)
    tempo_execucao = random.randint(0,execucao_limite)
    priority = random.randint(0,n_processos/2) 
    arq.write(f"Processo {i}: {tempo_entrada},{tempo_execucao},{priority}\n")




