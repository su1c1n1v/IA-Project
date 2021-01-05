"""
agente.py

criar aqui as funções que respondem às perguntas
e quaisquer outras que achem necessário criar

colocar aqui os nomes e número de aluno:
40681, Vinicius Rodrigues Silva Costa
NUM2, Miguel
"""

import time
import main
import graph

bat = []
power = []
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
	"""
	if(bat == [] and len(bat) == 0 or bateria == 100):
		if(bateria == 100):
			bat.clear()
		bat.append([bateria,time.time()])
		print('Primeiro:',bat)
	if(bateria == 0.0):
		if(len(bat) == 1):
			bat.append([bateria,time.time()])
			print(bat,'Time:',(bat[1][1]-bat[0][1])/60)
	"""
  	
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
		print('Not found any "Enfermaria"!')
	else:
		print('Distance:',path[0][0],'\nTime:',path[0][1],'\nPath:',path[0][2])
	
def resp4():
	# How much time is it to reach in the closest 'medico'?
    main.call_shortest_path('medico')

def resp5():
	# How much time is it to reach in the 'escadas'?
    main.call_shortest_path('Escadas')

def resp6():
	# How much time is to the baterie to be empty?
	moving = (power[0]/100)*2.068
	stopped = (power[0]/100)*3.086
	average = (moving+stopped)/2
	print('Moving:',round(moving,2),'minutes','\nStopped:',round(stopped,2),'minutes','\nAverage:',round(average,2),'minutes')

def resp7():
	answer = main.question7()
	print('First:',answer[0],'%','\nSecond:',answer[1],'%')

def resp8():
    pass
