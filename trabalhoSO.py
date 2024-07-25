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
		# processo.append(splited_line[0])
		data.append(splited_line[0])
		splited_line = splited_line[1].split(',')
		data.append(splited_line[0].replace(' ', ''))
		data.append(splited_line[1])
		data.append(splited_line[2])
		dataset.append(data)
		# tempo_entrada.append(splited_line[0].replace(' ', ''))
		# tempo_execucao.append(splited_line[1])
		# prioridades.append(splited_line[2])
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
	
	print(f"turn around: {soma}/{n} = {soma/n}")
	return float(soma/n)

# #LEITURA DAS DEADLINES
def lerDeadlines():
	del deadlines[:]
	for x in range(0,n):
		print ("Informe a Deadline do processo ", x+1, ": ")
		deadlines.append(input())
		pass


#Variáveis
# processo = []
# tempo_execucao = []
# tempo_entrada = []
# prioridades = []
deadlines = []

# #LÊ OS TEMPOS DE EXECUÇÃO E DE ENTRADA PARA CADA PROCESSO
# for x in range(1,n+1):
# 	print ("Tempo de entrada do processo ", x, ": ")
# 	tempo_entrada.append(float(input()))
# 	print ("Tempo de execução do processo ", x, ": ")
# 	tempo_execucao.append(float(input()))

#SOLICITA AO USUARIO QUE INFORME O ALGORITMO DE ESCALONAMENTO DESEJADO
def menu():
	print ("Selecione o algoritmo de escalonamento\n (1) FIFO\n (2) Gerar Gráfico (Nao funciona ainda)\n (0) Sair")
	escolha = int(input("Escolha: "))
	while escolha != 0:
		if escolha == 1:
			print ("============ FIFO ============")
			print ("TURN AROUND MEDIO: ", fifo())
			print ("==============================")
			break
		elif escolha == 2:
			quantum = float(input("Insira o valor do quantum: "))
			lerDeadlines()
			arquivo = open('resultados.json', 'w')
			saida = {'labels': ["FIFO",  "Round Robin", ],'datasets': [{'data': [fifo()]}]}
			json.dump(saida, arquivo, indent=2)
			arquivo.close()
			#Criar arquivo aqui
			break
		else:
			print ("Comando Inválido")
			break


# menu()
# cmd = int(input ("Escolha: "))
# #ENQUANDO A ESCOLHA FOR DIFERENTE DE 0, EXECUTA O RESPECTIVO ALGORITMO, ABRE O GRÁFICO OU RETORNA COMANDO INVALIDO
# while cmd != 0:
# 	if cmd == 1:
# 		print ("============ FIFO ============")
# 		print ("TURNAROUND MEDIO: ", fifo())
# 		print ("==============================")
# 		pass
# 	elif cmd == 2:
# 		quantum = float(input("Insira o valor do quantum: "))
# 		lerDeadlines()
# 		arquivo = open('resultados.json', 'w')
# 		saida = {'labels': ["FIFO",  "Round Robin", ],'datasets': [{'data': [fifo()]}]}
# 		json.dump(saida, arquivo, indent=2)
# 		arquivo.close()
# 		#Criar arquivo aqui
# 		pass
# 	else:
# 		print ("Comando Inválido")
# 		pass
# 	menu()
# 	cmd = int(input ("Escolha: "))

try:
	print(f"Lendo o arquivo: {sys.argv[1]}")
	df = ler_arquivo(sys.argv[1])
	n= len(df)
except IndexError:
	print("Please inform the file path")
	exit(1)

menu()



