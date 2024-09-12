import sys
import matplotlib.pyplot as plt
from Process import Process

def ler_arquivo(file_path):
	file = open(file_path)	
	processes = []
	for line in file:
		line = line.replace('\n', '')
		splited_line = line.split(':')
		name = splited_line[0]
		splited_line = splited_line[1].split(',')
		start_time= splited_line[0].replace(' ', '')
		execution_time = splited_line[1]
		priority = splited_line[2]
		processes.append(Process(name, start_time, execution_time, priority))
	return processes



#FUNÇÃO DO ALGORITMO FIFO
def fifo ():
	sorted_list = sorted(processes, key=lambda p: p.start_time)
	entradas = []
	tempos = []
	processos = []
	for process in sorted_list:
		entradas.append(process.start_time)
		tempos.append(process.execution_time)
		processos.append(process.name)

	soma = 0
	tempos_fim = []
	tempos_inicio = [0]
	tempo_atual = 0
	for i in range(0,len(entradas)):
		tempo_atual += tempos[i]
		tempos_fim.append(tempo_atual)
		tempos_inicio.append(tempo_atual)
		soma += tempo_atual - entradas[i]
	tempos_inicio.pop(len(tempos_inicio)-1)
	# Calculando a duração dos processos
	duracoes = [fim - inicio for inicio, fim in zip(tempos_inicio, tempos_fim)]
	# # Criando o gráfico
	plt.figure(figsize=(10, 6))
	print(duracoes,processos,tempos_inicio)
	plt.barh(processos, duracoes, left=tempos_inicio)

	# Adicionando rótulos e título
	plt.xlabel('Tempo')
	plt.ylabel('Processos')
	plt.title('Mapeamento de Processos')

	plt.show()
	return float(soma/n)

def round_robin ():
	quantum = int(input("Qual o valor do quantum: "))
	sorted_process = sorted(processes, key=lambda p: p.start_time)
	tempo_atual = 0.0
	processos_ativos = []
	while True:
		if len(processos_ativos) <= len(sorted_process):
			for process in sorted_process:
				# Adicionando novos processos ao looping, 
				if process.start_time <= tempo_atual and process.name not in processos_ativos or process.start_time <= tempo_atual+quantum and process.name not in processos_ativos:
					processos_ativos.append(process.name)
		for processo in processos_ativos:
			for process in sorted_process:
				if process.name == processo and process.get_tempo() > 0:
					if process.get_tempo() >= quantum:
						process.quantum(quantum)
						process.start_t(tempo_atual)
						tempo_atual += quantum
						process.end_t(tempo_atual)

					else:
						aux = process.get_tempo()
						process.quantum(aux)
						process.start_t(tempo_atual)
						tempo_atual += aux
						process.end_t(tempo_atual)


		cont_zerados = 0
		for process in sorted_process:
			if process.get_tempo() == 0:
				cont_zerados += 1
		
		if cont_zerados == len(sorted_process):
			break
	plt.figure(figsize=(10, 6))
	for i, process in enumerate(processes):
		for start, end in zip(process.start, process.end):
			plt.barh(process.name, end - start, left=start, height=0.5, label=process.name)

	# Adicionando rótulos e título
	plt.xlabel('Tempo')
	plt.ylabel('Processos')
	plt.title('Mapeamento de Processos')

	plt.show()
	tempo_final = 0
	for process in sorted_process:
		tempo_final += (process.end[-1] - process.start_time) 

	return float(tempo_final/n)



def menu():
	escolha = -1
	while escolha != 0:
		print ("Selecione o algoritmo de escalonamento\n (1) FIFO\n (2) Round-Robin\n (0) Sair")
		escolha = int(input("Escolha: "))
		if escolha == 1:
			print ("============ FIFO ============")
			print ("TURN AROUND MEDIO: ", fifo())
			print ("==============================")
		elif escolha == 2:
			print ("============ Round-Robin ============")
			print ("TURN AROUND MEDIO: ", round_robin())
			print ("==============================")
		elif escolha == 0:
			print ("Saindo ...")
		else:
			print ("Comando Inválido")

try:
	print(f"Lendo o arquivo: {sys.argv[1]}")
	path = sys.argv[1]
except IndexError:
	print("Utilizando o arquivo padrão teste 1")
	path = "processos.txt"
	

processes = ler_arquivo(path)
for process in processes:
    print(f'Nome: {process.name}, Tempo de execução: {process.execution_time}, Tempo em que o processo é incluído na fila: {process.start_time}, Prioridade: {process.priority}')

n= len(processes)
menu()


