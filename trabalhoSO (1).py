import json #IMPORTA O JSON PARA ESCREVER AS SAÍDAS DO GRÁFICO JAVASCRIPT

#FUNÇÃO DO ALGORITMO FIFO
def fifo ():
	entradas = list(tmpEnt)
	tempos = list(tmpExe)
	for j in range(0,n):
		for i in range(0,n-1):
			if entradas[i]>entradas[i+1]:
				Aux = entradas[i+1]
				entradas[i+1] = entradas[i]
				entradas[i] = Aux
				Aux = tempos[i+1]
				tempos[i+1] = tempos[i]
				tempos[i] = Aux
	soma = 0
	relogio = 0
	for x in range(0,n):
		relogio += tempos[x]
		pass
	return float(soma/n)

#LEITURA DAS DEADLINES
def lerDeadlines():
	del deadlines[:]
	for x in range(0,n):
		print ("Informe a Deadline do processo ", x+1, ": ")
		deadlines.append(input())
		pass

#LÊ A QUANTIDADE DE PROCESSOS E CRIA AS LISTAS DE TEMPO DE EXECUÇÃO E TEMPO DE ENTRADA PARA CADA PROCESSO
n = int(input ("Informe o numero de processos: "))
tmpExe = []
tmpEnt = []
deadlines = []

#LÊ OS TEMPOS DE EXECUÇÃO E DE ENTRADA PARA CADA PROCESSO
for x in range(1,n+1):
	print ("Tempo de entrada do processo ", x, ": ")
	tmpEnt.append(float(input()))
	print ("Tempo de execução do processo ", x, ": ")
	tmpExe.append(float(input()))

#SOLICITA AO USUARIO QUE INFORME O ALGORITMO DE ESCALONAMENTO DESEJADO
def menu():
	print ("Selecione o algoritmo de escalonamento\n (1) FIFO\n (2) Gerar Gráfico (Nao funciona ainda)\n (0) Sair")

menu()
cmd = int(input ("Escolha: "))
#ENQUANDO A ESCOLHA FOR DIFERENTE DE 0, EXECUTA O RESPECTIVO ALGORITMO, ABRE O GRÁFICO OU RETORNA COMANDO INVALIDO
while cmd != 0:
	if cmd == 1:
		print ("============ FIFO ============")
		print ("TURNAROUND MEDIO: ", fifo())
		print ("==============================")
		pass
	elif cmd == 2:
		quantum = float(input("Insira o valor do quantum: "))
		lerDeadlines()
		arquivo = open('resultados.json', 'w')
		saida = {'labels': ["FIFO",  "Round Robin", ],'datasets': [{'data': [fifo()]}]}
		json.dump(saida, arquivo, indent=2)
		arquivo.close()
		#Criar arquivo aqui
		pass
	else:
		print ("Comando Inválido")
		pass
	menu()
	cmd = int(input ("Escolha: "))
	