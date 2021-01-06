"""
agente.py

criar aqui as funções que respondem às perguntas
e quaisquer outras que achem necessário criar

colocar aqui os nomes e número de aluno:
40681, Vinicius Rodrigues Silva Costa
28732, Miguel Tavares Frias
"""

import time
import main
import graph

power = []
print('In the beginning the agent dont know his location and any information about his world!')
def work(posicao, bateria, objetos):
	#Função que auxilia na atualização da posição do agente
	main.actually_location(posicao)
	#Função que auxilia na atualização do grafo
	main.refresh_graph(posicao)
	#Função que auxilia na atualização da categoria das salas
	main.search_room_category()
	#Atualiza o a gente de quanta bateria ainda possui (Questão 6)
	if(power == []):
		power.append(bateria)
	else:
		power.clear()
		power.append(bateria)
	if objetos != []:
		main.get_objects(objetos,posicao)
  	
def resp1():
	# What is the penult person found?
	print(main.get_penult_person())
	
def resp2():
	# What is this room ?
	print(main.search_room_category())

def resp3():
	#What is the closest 'sala dos enfermeiros'?
	path = main.shortest_path_enfermaria()
	if(path == 'Not found any "Sala de enfermeiro"!'):
		print(path)
	else:
		print('Distance:',round(path[0][0],2),'\nTime:',round(path[0][1],2),'\nPath:',path[0][2])
	
def resp4():
	# How much time is it to reach in the closest 'medico'?
    main.call_shortest_path('medico')

def resp5():
	# How much time is it to reach in the 'escadas'?
    main.call_shortest_path('Escadas')

def resp6():
	# How much time is to the baterie to be empty?
	
	#Para responder essa questão foi feito varios testes com a bateria,
	#primeiro testamos quanto tempo a bateria dura com o agente parado 
	#(3.086 min), segundo testamos quanto tempo a bateria dura com o 
	#agente se movimentando (2.068 min), apos isso fazemos uma media 
	#aritmetica dos dois valores dando um resultado estimado de que o 
	#agente ficará metade do tempo se movimentando, e a outra metade 
	#parado (media aritmética).
	moving = (power[0]/100)*2.068
	stopped = (power[0]/100)*3.086
	average = (moving+stopped)/2
	print('Moving:',round(moving,2),'minutes','\nStopped:',round(stopped,2),'minutes','\nAverage:',round(average,2),'minutes')

def resp7():
	answer = main.question7()
	print('Indenpendent:',round(answer[0],2),'%','\nCondicional Probability',round(answer[1],2),'%')

def resp8():
	answer = main.question8()
	print('Indenpendent:',round(answer[0],2),'%','\nCondicional Probability',round(answer[1],2),'%')
