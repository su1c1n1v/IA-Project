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

def work(posicao, bateria, objetos):
	main.actuallyLocation(posicao)
	main.refresh_graph(posicao)
	main.search_room_category()
	if objetos != []:
		main.get_objects(objetos,posicao)
  	
def resp1():
	main.show_edges()
	
def resp2():
	# What is this room ?
	print(main.search_room_category())

def resp3():
	#What is the closest 'sala dos enfermeiros'?
	path = main.shortest_path_enfermaria()
	if(path == 'None'):
		print(path)
	else:
		print('Distance:',path[0][0],'Time:',path[0][1],'Path:',path[0][2])
	
def resp4():
	# How much time is it to reach in 'medico'
    main.call_shortest_path('medico')

def resp5():
	# How much time is it to reach in the 'escadas'?
    main.call_shortest_path('Escadas')

def resp6():
    pass

def resp7():
    pass

def resp8():
    pass
