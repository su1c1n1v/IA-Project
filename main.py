import time
import networkx as net
import graph  as gph

# List of Objects ----------------------------------------------------- #
pessoa_list = []
enfermeiro_list = []
medico_list = []
doente_list = []
livro_list = []
cama_list = []
cadeira_list = []
mesa_list = []
# --------------------------------------------------------------------- #
# List of Rooms ------------------------------------------------------- #
sala_dos_enfermeiros_list = []
sala_de_espera_list = []
quarto_list = []
# --------------------------------------------------------------------- #
# Init Variables ------------------------------------------------------ #
position = ['Corredor 2']
local_point = [[100,100]]
graph = net.MultiGraph()
speed = 245.6
# --------------------------------------------------------------------- #		
# Get the list of object and put in lists ----------------------------- #		
def get_objects(object_list,local):
	for obj in object_list:
		cathegory = obj.split("_")[0]
		
		if(cathegory == 'enfermeiro'):
			if obj not in enfermeiro_list:
				enfermeiro_list.append(obj)
				pessoa_list.append(obj)
				#create node and add in the graph
				gph.add_obj_graph(getActuallyPosition(),obj,local,graph)
				#print(enfermeiro_list)
			
		elif cathegory  == 'medico':
			if obj not in medico_list:
				medico_list.append(obj)
				pessoa_list.append(obj)
				gph.add_obj_graph(getActuallyPosition(),obj,local,graph)
				#print(medico_list)
			
		elif cathegory  == 'livro':
			if obj not in livro_list:
				livro_list.append(obj)
				gph.add_obj_graph(getActuallyPosition(),obj,local,graph)
				#print(livro_list)
				
		elif cathegory  == 'cama':
			if obj not in cama_list:
				cama_list.append(obj)
				gph.add_obj_graph(getActuallyPosition(),obj,local,graph)
				#print(cama_list)
				
		elif cathegory  == 'cadeira':
			if obj not in cadeira_list:
				cadeira_list.append(obj)
				gph.add_obj_graph(getActuallyPosition(),obj,local,graph)
				#print(cadeira_list)
				
		elif cathegory  == 'mesa':
			if obj not in mesa_list:
				mesa_list.append(obj)
				gph.add_obj_graph(getActuallyPosition(),obj,local,graph)
				#print(mesa_list)
				
		elif cathegory  == 'doente':
			if obj not in doente_list:
				doente_list.append(obj)
				pessoa_list.append(obj)
				gph.add_obj_graph(getActuallyPosition(),obj,local,graph)
				#print(doente_list)
# --------------------------------------------------------------------- #	
# Location ------------------------------------------------------------ #
def actuallyLocation(pos):
	local_point.clear()
	local_point.append(pos)
	x = pos[0]
	y = pos[1]
	
	if(x >= 30 and x <= 85 and y >= 90 and y <= 305):
		position = 'Corredor 2'
		getPosition(position)
	elif(x >= 30 and x <= 180 and y >= 30 and y <= 90):
		position = 'Escadas'
		getPosition(position)
	elif(x >= 565 and x <= 635 and y >= 30 and y <= 305):
		position = "Corredor 3"
		getPosition(position)
	elif(x >= 180 and x <= 540 and y >= 30 and y <= 70 or x >= 110 and x <= 540 and y >= 90 and y <= 135):
		position = "Corredor 1"
		getPosition(position)
	elif(x >= 30 and x <= 770 and y >= 330 and y <= 410):
		position = "Corredor 4"
		getPosition(position)
	elif(x >= 130 and x <= 235 and y >= 180 and y <= 235):
		position = "Sala 5"
		getPosition(position)
	elif(x >= 280 and x <= 385 and y >= 180 and y <= 285):
		position = "Sala 6"
		getPosition(position)
	elif(x >= 430 and x <= 520 and y >= 180 and y <= 285):
		position = "Sala 7"
		getPosition(position)
	elif(x >= 680 and x <= 770 and y >= 30 and y <= 85):
		position = "Sala 8"
		getPosition(position)
	elif(x >= 680 and x <= 770 and y >= 130 and y <= 185):
		position = "Sala 9"
		getPosition(position)
	elif(x >= 680 and x <= 770 and y >= 230 and y <= 285):
		position = "Sala 10"
		getPosition(position)
	elif(x >= 30 and x <= 235 and y >= 455 and y <= 570):
		position = "Sala 11"
		getPosition(position)
	elif(x >= 280 and x <= 385 and y >= 455 and y <= 570):
		position = "Sala 12"
		getPosition(position)
	elif(x >= 430 and x <= 570 and y >= 455 and y <= 570):
		position = "Sala 13"
		getPosition(position)
	elif(x >= 615 and x <= 770 and y >= 455 and y <= 570):
		position = "Sala 14"
		getPosition(position)
# --------------------------------------------------------------------- #		
def getPosition(pos):
	if(pos != position[-1]):
		position.append(pos)
# --------------------------------------------------------------------- #		
def getActuallyPosition():
	return position
# --------------------------------------------------------------------- #	
def call_shortest_path(node):
	if(node == 'medico'):
		medicos = []
		if(len(medico_list) >= 1):
			for medico in medico_list:
				path = gph.create_graph_distance_two_nodes(position,local_point,medico,graph)
				if(medicos == []):
					medicos = path[:]
				else:
					if(path[0] < medicos[0]):
						medicos = path[:]
			print('Distance',medicos[0],'\nTime',medicos[1],'\nPath',medicos[2])
		else:
			print('None')
	else:
		if(node in graph.nodes()):
			path = gph.create_graph_distance_two_nodes(position,local_point,node,graph)
			print('Distance',path[0],'\nTime',path[1],'\nPath',path[2])
		else:
			print('None')
# --------------------------------------------------------------------- #	
# Search the category of this room ------------------------------------ #
def search_room_category():
	mesa = []
	cadeira = []
	cama = []
	for node in graph.edges(position[-1]):
		category = node[1].split("_")[0]
		if(category == 'cama'):
			cama.append(node[1])
		elif(category == 'mesa'):
			mesa.append(node[1])
		elif(category == 'cadeira'):
			cadeira.append(node[1])
	if(len(cama) >= 1):	
		if(position[-1] not in quarto_list):
			quarto_list.append(position[-1])
			if(position[-1] in sala_de_espera_list):
				sala_de_espera_list.remove(position[-1])
			if(position[-1] in sala_dos_enfermeiros_list):
				sala_dos_enfermeiros_list.remove(position[-1])
		return 'Node: ' + position[-1] + ' Category: Quarto'		
	elif(len(mesa) >= 1 and len(cama) == 0 and len(cadeira) >= 1):
		#print('Node:',position[-1],'Category: Sala de Enfermeiros')
		if(position[-1] not in sala_dos_enfermeiros_list):
			sala_dos_enfermeiros_list.append(position[-1])
			if(position[-1] in sala_de_espera_list):
				sala_de_espera_list.remove(position[-1])
		return 'Node: ' + position[-1] + ' Category: Sala de Enfermeiros'
	elif(len(cadeira) > 2 and len(mesa) == 0):
		#print('Node:',position[-1],'Category: Sala de Espera')
		if(position[-1] not in sala_de_espera_list):
			sala_de_espera_list.append(position[-1])
		return 'Node: ' + position[-1] + ' Category: Sala de Espera'
	else:
		return 'Node: ' + position[-1] + ' Category: none'
# --------------------------------------------------------------------- #	
# Add Room or Object in the graph ------------------------------------- #
def refresh_graph(posicao):
	gph.searchRoomInGraph(getActuallyPosition(),posicao,graph)
# --------------------------------------------------------------------- #
def show_edges():
	gph.show_edges(graph)
# --------------------------------------------------------------------- #	
def show_all_rooms_categories():
	for node in quarto_list:
		print('Quarto:',node)	
	for node in sala_de_espera_list:
		print('Sala de Espera:',node)
	for node in sala_dos_enfermeiros_list:
		print('Sala dos Enfermeiros:',node)
		
def shortest_path_enfermaria():
	enfermaria = []
	if(len(sala_dos_enfermeiros_list) >= 1):
		for node in sala_dos_enfermeiros_list:
			path = gph.create_graph_distance_two_nodes(position,local_point,node,graph)
			if(enfermaria == []):
				enfermaria.append(path)
			else:
				if(enfermaria[-1][0] > path[0]):
					enfermaria.clear()
					enfermaria.append(path)
		return enfermaria
	else:
		return 'None'
# --------------------------------------------------------------------- #
# Question 1 ---------------------------------------------------------- #
def get_penult_person():
	if(pessoa_list == []):
		return 'Not found anyone!'
	elif(len(pessoa_list) >= 2):
		return 'Penult: ' + pessoa_list[-2] + '!'
	else:
		return 'Only found 1 person!' +'\nPerson: ' + pessoa_list[0]
		
