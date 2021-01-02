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
corredor_list = ['Corredor 1','Corredor 2','Corredor 3','Corredor 4']
# --------------------------------------------------------------------- #
# Init Variables ------------------------------------------------------ #
position = ['Corredor 2']
local_point = [[100,100]]
graph = net.MultiGraph()
speed = 245.6
# --------------------------------------------------------------------- #		
# Get the list of object and put in lists ----------------------------- #		
def get_objects(object_list,local):
	#Função mais importante, tem a funcionalidade de pegar os inputs 
	#recebidos pelo agente e classifica o obj podendo se 'enfermeiro',
	#'livro','medico','doente'... depois de classificar, é criado um 
	#vinculo  do objeto com a sala (criado um aresta entre a sala e o 
	#objeto)
	for obj in object_list:
		#Pega a categoria do objeto 
		cathegory = obj.split("_")[0]
		#Classifica se o objeto e uma pessoa, se for e adicionado a uma 
		#lista auxiliar que guarda as duas ultimas pessoas que o agente 
		#encontrou.
		if(cathegory == 'enfermeiro' or cathegory == 'medico'or cathegory == 'doente'):
			if(len(pessoa_list) > 2):
				pessoa_list.remove(pessoa_list[0])
			if(len(pessoa_list) == 0):
				pessoa_list.append(obj)
			else:
				if(pessoa_list[-1] != obj):
					pessoa_list.append(obj)
		#Parte de categorizar o objeto e adiciona o aresta do objeto 
		#a sala.
		if(cathegory == 'enfermeiro'):
			if obj not in enfermeiro_list:
				enfermeiro_list.append(obj)
				gph.add_obj_graph(getActuallyPosition(),obj,local,graph)
		elif cathegory  == 'medico':
			if obj not in medico_list:
				medico_list.append(obj)
				gph.add_obj_graph(getActuallyPosition(),obj,local,graph)	
		elif cathegory  == 'livro':
			if obj not in livro_list:
				livro_list.append(obj)
				gph.add_obj_graph(getActuallyPosition(),obj,local,graph)		
		elif cathegory  == 'cama':
			if obj not in cama_list:
				cama_list.append(obj)
				gph.add_obj_graph(getActuallyPosition(),obj,local,graph)				
		elif cathegory  == 'cadeira':
			if obj not in cadeira_list:
				cadeira_list.append(obj)
				gph.add_obj_graph(getActuallyPosition(),obj,local,graph)				
		elif cathegory  == 'mesa':
			if obj not in mesa_list:
				mesa_list.append(obj)
				gph.add_obj_graph(getActuallyPosition(),obj,local,graph)				
		elif cathegory  == 'doente':
			if obj not in doente_list:
				doente_list.append(obj)
				gph.add_obj_graph(getActuallyPosition(),obj,local,graph)
# --------------------------------------------------------------------- #	
# Refresh the position of the machine --------------------------------- #
def actually_location(pos):
	#Atualiza a posição do agente com o clock do 'work', a posição é 
	#determinada pelas paredes das salas que são definidas logo a baixo. 
	local_point.clear()
	local_point.append(pos)
	x = pos[0]
	y = pos[1]
	#Pontos que definem os limites de cada sala do software
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
# Refresh position  --------------------------------------------------- #		
def getPosition(pos):
	#Todo clock do work atualiza a posição do agente e guarda ela na lista
	#'position'
	if(pos != position[-1]):
		position.append(pos)
# --------------------------------------------------------------------- #
# Get the position ---------------------------------------------------- #		
def getActuallyPosition():
	#Pega a ultima coordenada do agente (a que o agente estar no momento)
	# e retorna para ser usado no agente.py
	return position
# --------------------------------------------------------------------- #	
# Call the shortest path to 'node' ------------------------------------ #
def call_shortest_path(node):
	#Tem o proposito de pegar o menor caminho de onde o agente estar para 
	#o 'node'
	
	#Questão 4: Pega todos os medicos ja vistos, e verifica qual deles 
	#tem a menor distancia. 
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
			print('Any "Medico found!"')
	else:
		if(node in graph.nodes()):
			path = gph.create_graph_distance_two_nodes(position,local_point,node,graph)
			print('Distance',path[0],'\nTime',path[1],'\nPath',path[2])
		else:
			print('There is no',node,'in the graph!')
# --------------------------------------------------------------------- #	
# Search the category of this room ------------------------------------ #
def search_room_category():
	#Questão 2: Categoriza a sala dependedo dos objetos encontrados dentro
	#da sala atual, para isso e percorrido todos os arestas da sala, e 
	#verifica se cumpre com os requisitos para ser uma 'Sala de enfermeiros',
	#'Sala de espera' ou 'quarto'.
	mesa = []
	cadeira = []
	cama = []
	#Conta quantas camas, mesas e cadeira tem na sala.
	for node in graph.edges(position[-1]):
		category = node[1].split("_")[0]
		if(category == 'cama'):
			cama.append(node[1])
		elif(category == 'mesa'):
			mesa.append(node[1])
		elif(category == 'cadeira'):
			cadeira.append(node[1])
	#Dependendo do objeto encontrado é determinado que tipo de sala o 
	#agente estar.
	if(len(cama) >= 1):	
		if(position[-1] not in quarto_list):
			quarto_list.append(position[-1])
			if(position[-1] in sala_de_espera_list):
				sala_de_espera_list.remove(position[-1])
			if(position[-1] in sala_dos_enfermeiros_list):
				sala_dos_enfermeiros_list.remove(position[-1])
		return 'Node: ' + position[-1] + ' Category: Quarto'		
	elif(len(mesa) >= 1 and len(cama) == 0 and len(cadeira) >= 1):
		if(position[-1] not in sala_dos_enfermeiros_list):
			sala_dos_enfermeiros_list.append(position[-1])
			if(position[-1] in sala_de_espera_list):
				sala_de_espera_list.remove(position[-1])
		return 'Node: ' + position[-1] + ' Category: Sala de Enfermeiros'
	elif(len(cadeira) > 2 and len(mesa) == 0):
		if(position[-1] not in sala_de_espera_list):
			sala_de_espera_list.append(position[-1])
		return 'Node: ' + position[-1] + ' Category: Sala de Espera'
	else:
		return 'Node: ' + position[-1] + ' Category: none'
# --------------------------------------------------------------------- #	
# Add Room or Object in the graph ------------------------------------- #
def refresh_graph(posicao):
	#Atualiza o grafo, e verifica se o node atual ja possui um aresta 
	#dentro do grafo, se tiver não faz nada, se não tiver, adiciona um aresta
	#o node atual com o anterior
	gph.search_room_in_graph(getActuallyPosition(),posicao,graph)
# --------------------------------------------------------------------- #
# Show all edges in the graph ----------------------------------------- #
def show_edges():
	#Mostra na linha de comando todos os arestas já adicionados no grafo
	gph.show_edges(graph)
# --------------------------------------------------------------------- #
# Show all rooms and it categories ------------------------------------ #	
def show_all_rooms_categories():
	#Mostra na linha de comando todas as salas e suas categorias já 
	#adicionado no grafo
	for node in quarto_list:
		print('Quarto:',node)	
	for node in sala_de_espera_list:
		print('Sala de Espera:',node)
	for node in sala_dos_enfermeiros_list:
		print('Sala dos Enfermeiros:',node)
# --------------------------------------------------------------------- #
# The shortest path to the closest 'enfermaria' ----------------------- #
def shortest_path_enfermaria():
	#Questão 3: Procura o menor caminho ate a sala de enfermeiro mais 
	#proxima. 
	enfermaria = []
	#Verificamos todas as salas de enfermeiro, e nos certificamos de pegar 
	#a sala mais proxima
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
		return 'Not found any "Sala de enfermeiro"!'
# --------------------------------------------------------------------- #
# Get the penult person found ----------------------------------------- #
def get_penult_person():
	#Questão 1:
	#Pega a ultima pessoa que o agente viu, que e guardado na 'pessoa_list'
	if(pessoa_list == []):
		return 'Not found anyone!'
	elif(len(pessoa_list) >= 2):
		return 'Penult: ' + pessoa_list[-2] + '!'
	else:
		return 'Only found 1 person!' + '\nPerson: ' + pessoa_list[0]
# --------------------------------------------------------------------- #
# Questão 7 ----------------------------------------------------------- #
def question7():
	#Nesta questão foi feita usando duas maneiras
	#1º sendo o livro, e a cadeira independentes
	#2º usando as salas como fator de dependencia entre os objetos, para
	#ser possivel usar redes  bayesianas
	
	#Aqui pegamos a quantidade de todas as salas e objetos para que 
	#possamos calcular sua probabilidade 
	total_espera = len(sala_de_espera_list)
	total_enfermaria = len(sala_dos_enfermeiros_list)
	total_quarto = len(quarto_list)
	total_livro = len(livro_list)
	total_cadeira = len(cadeira_list)
	total_corredor = len(corredor_list)
	total_divisoes = total_espera + total_enfermaria + total_quarto + total_corredor
	
	total_livro_sala_espera = how_much_obj_has_in_the_room(sala_de_espera_list,'livro')
	total_livro_quarto = how_much_obj_has_in_the_room(quarto_list,'livro')
	total_livro_sala_de_enfermeiros = how_much_obj_has_in_the_room(sala_dos_enfermeiros_list,'livro')
	total_livro_corredor = how_much_obj_has_in_the_room(corredor_list,'livro')
	
	total_cadeira_sala_espera = how_much_obj_has_in_the_room(sala_de_espera_list,'cadeira')
	total_cadeira_quarto = how_much_obj_has_in_the_room(quarto_list,'cadeira')
	total_cadeira_sala_de_enfermeiros = how_much_obj_has_in_the_room(sala_dos_enfermeiros_list,'cadeira')
	total_cadeira_corredor = how_much_obj_has_in_the_room(corredor_list,'cadeira')
	
	#Resolução livro e cadeira sendo independente ---------------------
	resposta1 = (total_livro/total_divisoes)*100
	
	#Resolução usando bayseana ----------------------------------------
	#Probabilidade da sala ser uma "sala de espera", vezes a chance de 
	#encontrar uma cadeira, vezes a chance de encontrar um livro
	espera = 0.0
	if(total_espera != 0 and total_livro_sala_espera != 0 and total_livro != 0):
		espera = (total_espera/total_divisoes) * 1 * (total_livro_sala_espera/total_livro)
	
	#Probabilidade da sala ser uma "Sala de enfermeiros" vezes a chance 
	#de encontrar uma cadeira, vezes a chance de encontrar um livro.
	enfermaria = 0.0
	if(total_enfermaria != 0 and total_livro_sala_de_enfermeiros != 0 and total_livro != 0):
		enfermaria = (total_enfermaria/total_divisoes) * 1 * (total_livro_sala_de_enfermeiros/total_livro)
	
	#Probabilidade da sala ser um "Quarto" vezes a chance de ter uma 
	#cadeira, vezes a chance de ter um livro no quarto 
	quarto = 0.0
	if(total_quarto != 0 and total_cadeira != 0 and total_livro_quarto != 0 and total_livro != 0):
		quarto = (total_quarto/total_divisoes) * (total_cadeira_quarto/total_cadeira) * (total_livro_quarto/total_livro)
	
	#Probabilidade da divisao ser um "Corredor" vezes a chance de ter uma 
	#cadeira, vezes a chance de ter um livro no corredor 
	corredor = 0.0
	if(total_corredor != 0 and total_cadeira != 0 and total_livro_corredor != 0 and total_livro != 0):
		corredor = (total_corredor/total_divisoes) * (total_cadeira_corredor/total_cadeira) * (total_livro_corredor/total_livro)
	
	#Resolução ultilizando bayseana
	reposta2 = (espera + enfermaria + quarto)*100
	#Retorna as duas respostas
	return [resposta1,reposta2]
# --------------------------------------------------------------------- #
# Question 8 ---------------------------------------------------------- # 
def question8():
	#Nesta questão foi feita usando duas maneiras
	#1º sendo o livro, e a cadeira independentes
	#2º usando as salas como fator de dependencia entre os objetos, para
	#ser possivel usar redes  bayesianas
	
	#Para resolver esta questão usando probabilidade condicional, e 
	#necessario que a gente pegue as chance de ser uma sala ou corredor.
	total_espera = len(sala_de_espera_list)
	total_enfermaria = len(sala_dos_enfermeiros_list)
	total_quarto = len(quarto_list)
	total_escadas = len(corredor_list)
	total_divisoes = total_quarto + total_escadas + total_espera + total_enfermaria
	
	#Pegamos a guantidade de doentes e enfermerios, com isso podemos 
	#calcular porcentage de chance de encontrar esse objetos.
	total_doente = len(doente_list)
	total_enfermeiro = len(enfermeiro_list)
	
	#Na resposta 1 como doentes e enfermeiros são independentes, não há
	#porcentagem condicional, ou seja só precisamos da chance de encontrar
	#um doente. 
	#A chance de encontrar um doente em uma divisão.
	resposta1 = (total_doente/total_divisoes)*100
	
	#Para resolver esta questão na segunda maneira, pegamos a chances de 
	#encontrar um doente em uma sala especifica, e pegamos as chances de
	#encontrar um enfermeiro em uma divisão, com isso podemos fazer um
	#calculo condicional entre encontrar um enfermeiro e um doente.
	total_doente_espera = how_much_obj_has_in_the_room(sala_de_espera_list,'doente')
	total_doente_enfermaria = how_much_obj_has_in_the_room(sala_dos_enfermeiros_list,'doente')
	total_doente_quarto = how_much_obj_has_in_the_room(quarto_list,'doente')
	total_doente_corredor = how_much_obj_has_in_the_room(corredor_list,'doente')
	
	total_enfermeiro_espera = how_much_obj_has_in_the_room(sala_de_espera_list,'enfermeiro')
	total_enfermeiro_quarto = how_much_obj_has_in_the_room(quarto_list,'enfermeiro')
	total_enfermeiro_enfermaria = how_much_obj_has_in_the_room(sala_dos_enfermeiros_list,'enfermeiro')
	total_enfermeiro_corredor = how_much_obj_has_in_the_room(corredor_list,'enfermeiro')
	
	#Calculo 1: Chance de encontrar um doente em uma sala de espera sabendo
	#que ja encontramos um enfermeiro.
	espera = 0.0
	if(total_espera != 0 and total_enfermeiro_espera != 0 and total_doente != 0 and total_doente_espera != 0):
		espera = (total_espera/total_divisoes) * (total_enfermeiro_espera/total_enfermeiro) * (total_doente_espera/total_doente)
	
	#Calculo 2: Chance de encontrar um doente em um quarto sabendo
	#que ja encontramos um enfermeiro.
	quarto = 0.0
	if(total_quarto != 0 and total_enfermeiro_quarto != 0 and total_doente != 0 and total_doente_quarto != 0):
		quarto = (total_quarto/total_divisoes) * (total_enfermeiro_quarto/total_enfermeiro) * (total_doente_quarto/total_doente)
	
	#Calculo 3: Chance de encontrar um doente em um sala de enfermeiro
	#sabendo que ja encontramos um enfermeiro.
	enfermaria = 0.0
	if(total_enfermaria != 0 and total_enfermeiro_enfermaria != 0 and total_doente != 0 and total_doente_enfermaria != 0):
		enfermaria = (total_enfermaria/total_divisoes) * (total_enfermeiro_enfermaria/total_enfermeiro) * (total_doente_enfermaria/total_doente)
	
	#Calculo 4: Chance de encontrar um doente em no corredor sabendo que 
	#ja encontramos um enfermeiro.
	corredor = 0.0
	if(total_enfermaria != 0 and total_enfermeiro_corredor != 0 and total_doente != 0 and total_doente_corredor != 0):
		corredor = (total_corredor/total_divisoes) * (total_enfermeiro_corredor/total_enfermeiro) * (total_doente_corredor/total_doente)
	
	#A soma de todas as divisões para ter um todo.
	resposta2 = (espera + enfermaria + quarto + corredor)*100
	
	#OBS: A segunda opção usa probabilidade codicional para calcular,
	#como as chances são baseadas no que é encontrado no mapa, ou seja,
	#pega quantas vezes encontramos um doente e enfermeiro no corredo, quarto,... 
	#,e em alguns casos vai ser zero, ou seja não e encontrado nenhum 
	#doente e enfermeiro juntos na mesma divisão, então as chances são zero.
	
	return [resposta1,resposta2]
# --------------------------------------------------------------------- #
# Look how much 'obj' has in this room -------------------------------- # 
def how_much_obj_has_in_the_room(list_obj,obj):
	#Função auxiliar, que tem o proposito de ajuda a contabilizar quantos
	#objetos do tipo 'obj' (dado como parametro da função, que e nome da 
	#categoria de objeto) estão interligados atraves de um aresta com a 
	#sala atual
	count = 0
	for node in list_obj:
		for edge in graph.edges(node):
			if(edge[0].split("_")[0] == obj):
				count = count + 1
			if(edge[1].split("_")[0] == obj):
				count = count + 1
	return count
