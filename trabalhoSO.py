import json #IMPORTA O JSON PARA ESCREVER AS SAÍDAS DO GRÁFICO JAVASCRIPT
import sys
import pandas as pd


def ler_arquivo(file_path):
	file = open(file_path)
	dataset = []	
	for line in file:
		data = []
		line = line.replace('\n', '')
		splited_line = line.split(':')
		data.append(splited_line[0])
		splited_line = splited_line[1].split(',')
		data.append(splited_line[0].replace(' ', ''))
		data.append(splited_line[1])
		data.append(splited_line[2])
		dataset.append(data)
	df = pd.DataFrame(dataset,columns=['Processos','Tempo de entrada', 'Tempo de execução', 'Prioridade'])
	df = df.astype({"Tempo de entrada": int, "Tempo de execução": int, "Prioridade": int})
	print(f"{len(dataset)} processos foram adicionados:", end='\n')
	print(df)
	return df



#FUNÇÃO DO ALGORITMO FIFO
def fifo ():
	df_ordenado = df.sort_values(by='Tempo de entrada')
	entradas = list(df_ordenado['Tempo de entrada'])
	tempos = list(df_ordenado['Tempo de execução'])
	soma = 0
	tempo_atual = 0
	print(entradas)
	for i in range(0,len(entradas)):
		tempo_atual += tempos[i]
		soma += tempo_atual - entradas[i]
	
	return float(soma/n)

def round_robin ():
	quantum = int(input("Qual o valor do quantum: "))
	df_ordenado = df.sort_values(by='Tempo de entrada')
	entradas = list(df_ordenado['Tempo de entrada'])
	tempos = list(df_ordenado['Tempo de execução'])
	tempo_final_processo = 0
	tempo_atual = 0
	i = 0
	while len(tempos) > 0:
		if entradas[i] <= tempo_atual:
			if tempos[i] > quantum:
				tempos[i] = tempos[i] - quantum
				tempo_atual += quantum
			else:
				tempo_atual += tempos[i]
				tempos[i] = 0
				tempo_final_processo += tempo_atual

			if tempos[i] <= 0:
				tempos.pop(i)
			else: 
				i+= 1
			if i == len(tempos):
				i = 0
		else: 
			i = 0
	
	return float(tempo_final_processo/n)



def menu():
	print ("Selecione o algoritmo de escalonamento\n (1) FIFO\n (2) Round-Robin\n (0) Sair")
	escolha = int(input("Escolha: "))
	while escolha != 0:
		if escolha == 1:
			print ("============ FIFO ============")
			print ("TURN AROUND MEDIO: ", fifo())
			print ("==============================")
			break
		elif escolha == 2:
			print ("============ Round-Robin ============")
			print ("TURN AROUND MEDIO: ", round_robin())
			print ("==============================")
			break
		else:
			print ("Comando Inválido")
			break

try:
	print(f"Lendo o arquivo: {sys.argv[1]}")
	path = sys.argv[1]
except IndexError:
	print("Utilizando o arquivo padrão teste 1")
	path = "teste1.txt"
	

df = ler_arquivo(path)
n= len(df)
menu()



