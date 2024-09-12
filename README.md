# Documentação do Projeto - Algoritmos de Escalonamento (FIFO & Round-Robin)
## 1 - Descrição geral

Este projeto implementa os algoritmos de escalonamento de tarefas FIFO (First In First Out) e Round-Robin, utilizando a linguagem Python. O objetivo é simular a execução de processos com base nesses algoritmos e calcular o turnaround time para cada processo, visualizando os resultados graficamente.

- FIFO: executa os processos na ordem de chegada.

- Round-Robin: executa os processos em ciclos, com um tempo fixo de quantum para cada processo.


## 2 - Ambiente de desenvolvimento

Sistema operacional: Ubuntu 22.04.4 LTS
Linguagem: Python 3.10
Bibliotecas: 
Random: Geração de números aleatórios para criação de processos.
Sys: Utilização de parâmetros passados pelo terminal.
Matplotlib: Utilizada para visualização gráfica dos processos e seus tempos de execução. 
	Instalação de dependências:

`pip install matplotlib`

3 - Estrutura de diretórios
O trabalho possui a seguinte estrutura de diretórios:

├── gerarProcesso.py #Código para gerar processos aleatórios

├── Process.py #Define a classe Process e suas funcionalidades

├── trabalhoSO.py #Implementação dos algoritmos FIFO e Round-Robin

├── processos.txt #Arquivo de entrada gerado com os processos

## 4 - Arquivos principais

### 4.1 - gerarProcesso.py

**Descrição**: Este script gera processos aleatórios com tempos de entrada e tempos de execução aleatórios.

**Execução**: 

`python3 gerarProcesso.py`

**Durante a execução**: Durante a execução serão solicitadas as seguintes informações:

**Quantos processos deseja criar**: O número de processos que o usuário quer gerar.

**Qual o tempo de entrada limite**: O tempo máximo de entrada dos processos.

**Qual o tempo de execução limite**: O tempo máximo que um processo pode levar para terminar.

**Saídas**: o código gera X processos, e seus tempo de entrada, execução e prioridade (a prioridade é descartável nesses algoritmos, mas para uma possível melhoria já foi implementado essa funcionalidade). Os dados gerados são escritos no arquivo processos.txt, e possuem o seguinte formato:

`Processo X: tempo de entrada,tempo de execução,prioridade`

### 4.2 - Process.py

**Descrição**: Define a classe Process, que encapsula os atributos e métodos dos processos.
**Funções**:

**__init__**: Construtor que define nome, tempo de execução, tempo de entrada, prioridade, entre outros atributos.

**start_t**: Adiciona o tempo atual no vetor start

**end_t**: Adiciona o tempo atual no vetor end

**quantum**: Reduz o tempo restante de execução com base no valor do quantum.

**get_tempo**: Retorna o tempo restante do processo.

**__str__**:  Retorna as informações dos valores das variáveis

### 4.3 - trabalhoSO.py

É o corpo do trabalho, este é o arquivo principal, onde os algoritmos estão. Para executar o código:  
		
`python3 trabalhoSO.py`

Desta forma o arquivo padrão (processos.txt) será utilizado, caso queira utilizar algum arquivo importado, mas que esteja no formato especificado: 
		
`python3 trabalhoSO.py nome_arquivo.txt`

**Fluxo de execução**: Após a leitura do arquivo, o usuário deverá escolher qual algoritmo deseja executar:

**FIFO**: 
Este algoritmo organiza os processos em uma lista ordenada pelo tempo de chegada. Cada processo é executado até a execução até a conclusão, sem preempção.
**Passos**:

- Ordena-se os processos pelo tempo de entrada de cada processo
- Inicializa os vetores de entradas, tempos e processos,  
- Looping para adicionar os processos ordenados nesses vetores. 
- Cria-se variáveis para a soma e tempo atual como zero e vetores de tempos finais e iniciais. 
- Para cada processo:
    - Atualizar o tempo atual e adicionar os tempos finais e de início do próximo processo
    - Atualizar a soma para fazer o turnaround
- Calcular as durações dos processos
- Mostrar o gráfico com os tempos de execuções dos processos
- Retornar o valor de turnaround

**Round-Robin**: 
Neste algoritmo, os processos recebem um quantum de CPU, executando em ciclos até que todos sejam concluídos.

**Passos**:

- O usuário deverá digitar um valor para o quantum
- Organiza os processos em uma lista de processos ativos
- Enquanto houver processos a serem processados:
    - Se o tamanho de vetor dos processos ativos for menor que o vetor de processos:
        - Se o tempo de início do processo for menor que o tempo atual e o processo ainda não foi definido com ativo:
            - Adiciona o processo no vetor de processos ativos
        - Para cada processo:
            - Se o tempo restante do processo for maior que o quantum:
                - Reduzir o tempo restante com base no quantum
            - Se o restante for menor que o quantum, mas maior que zero
                - Será reduzido somente o tempo faltante
- Calcular as durações dos processos
- Mostrar o gráfico com os tempos de execuções dos processos
- Retornar o valor de turnaround

## 5 - Referências

O projeto foi desenvolvido inteiramente com base nos conceitos e algoritmos discutidos ao longo da disciplina de Sistemas Operacionais, ministrada pelo Professor Eduardo Pagani Julio da Universidade Federal de Juiz de Fora (UFJF). Todo código foi criado de forma independente, sem consulta a fontes externas, utilizando apenas o conhecimento adquirido nas aulas.

Além disso, os conceitos de escalonamento de processos como FIFO e Round-Robin são amplamente discutidos em diversos materiais acadêmicos e livros de referência na área de sistemas operacionais, como:

TANENBAUM, ANDREW S.; MODERNOS, Sistemas Operacionais. edição. 3.

## 6 - Grupo do trabalho
Alvaro Domingues de Freitas - 
André Luiz Casarim Leite - 
Gabriel Evaristo Carlos - 201965034B
Guilherme Soares Frias - 
