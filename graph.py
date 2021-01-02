import time
import math
import networkx as net

#Nesse ficheiro é onde manipulamos os grafos, e suas respectivas 
#funcionalidades. Aqui adicionamos nodos ao grafo, adicionamos um aresta
#entre dois nodos, procuramos o menor caminho entre dois nodos e o tempo
#para percorrer este caminho.
	
# add_node ------------------------------------------------------------ #
def add_nodes(node1,node2,points,graph):
	#Adiciona um aresta 'node1' com o 'node2' 
	graph.add_edge(node1,node2,limits=points[:],weight=0)
# --------------------------------------------------------------------- #
# Search_Room --------------------------------------------------------- #
def search_room_in_graph(localList,weight,graph):
	#Verifica se o node em que o agente estar atualmente já esta conectada	
	#com outra aresta dentro do grafo
	if len(localList) > 1:
		if not graph.has_edge(localList[-1],localList[-2]):
			add_nodes(localList[-1],localList[-2],weight,graph)
# --------------------------------------------------------------------- #
# Add obj in the graph in it position --------------------------------- #
def add_obj_graph(localList,obj,weight,graph):
	#Adiciona um aresta entre um 'obj' com a posiçao atual do agente
	#(que seria o node atual)
	if not graph.has_edge(localList[-1],obj):
		#print('Adicionado',obj,localList[-1])
		add_nodes(localList[-1],obj,weight,graph)
# --------------------------------------------------------------------- #
# Show all edges ------------------------------------------------------ #
def show_edges(graph):
	#Mostra na linha de comando todos os edges já adicionado no grafo 
	#(debug).
	sp = dict(net.all_pairs_dijkstra_path(graph))
	print('Grafo ',graph.edges())
	for node in graph.nodes():
		print('|--------',node,'--------|')
		for edge in graph[node]:
			print('	Edge:',edge,graph[node][edge])
# --------------------------------------------------------------------- #
# The shortest path --------------------------------------------------- #
def create_graph_distance_two_nodes(position,local_points,local,graph):
	#Função central para a manipulação do grafo (Questões 3, 4 e 5)
	
	#Esta função ajuda para encontrar o menor caminho entre dois nodos, e
	#para isso é criado um multigrafo (permite fazer dois nodos se 
	#conectarem mais de uma vez) e com ele é criado arestas que 
	#representam a distancia entre dois nodos mas levando em conta o 
	#destino, ou seja é quardado o 'weight' dos dois nodos levando em 
	#conta de onde eu estou para onde estou indo.
	#Exemplo: 
	#node1 (corredor 1)
	#node2 (corredor 2)
	#aresta1 (node1,node2,weight=100,indo=Escadas)
	#aresta2 (node1,node2,weight=300,indo=Corredor 3)
	#aresta3 (node1,node2,weight=200,indo=Sala 5)
	#Ou seja, dependedo do meu objetivo de destino o peso 'weight' tem
	#diferentes valores, com isso podemos saber qual e o menor caminho.
	
	#Parte 1:
	#Nesta parte não e criado arestas auxiliares pois, o nodo manipulado 
	#aqui e o nodo onde o agente estar, ou seja so e dado a distancia do
	#agente até as saidas do nodo.
	graph2 = graph.copy()
	for node in graph2[position[-1]]:
		point1 = graph2[position[-1]][node][0]['limits']
		point2 = local_points[0]							
		cost = distance_two_points(point1,point2)
		graph2[position[-1]][node][0]['weight'] = cost	
	#Parte 2:
	#Nesta parte que e feito os arestas auxiliares em todos os nodos
	#e suas saidas e objetivos
	for node in graph2.nodes():
		if node != position[-1]:
			for edge1 in graph2[node]:
				point1 = graph2[node][edge1][0]['limits']
				if(len(graph2[node]) > 1):
					for edge2 in graph2[node]:
						if(edge2 != edge1 and edge1 != position[-1]):
							point2 = graph2[node][edge2][0]['limits']	
							cost = distance_two_points(point1,point2)
							graph2.add_edge(node,edge2,limit=point2,weight=cost,going=edge1)
							graph2[node][edge2][0]['weight'] = cost
							graph2[node][edge2][0]['going'] = edge1
	#Apos ser criado o multigrafo já com todos as arestas auxiliares é 
	#enviado para 'search_path_two_nodes' que vai encontrar o menor path.
	return search_path_two_nodes(graph2,local_points,position,local)
# --------------------------------------------------------------------- #
# Search the best path for two nodes ---------------------------------- #
def search_path_two_nodes(graph,local_points,position,local):
	#Função auxiliar que ajuda a encontra o menor path entre dois nodos
	#para isso ser feito e utilizado a função 'all_pairs_dijkstra_path'
	#da biblioteca networkX, que tem a funcionalidade de aplicar o teorema
	#de dijkstra.
	for node in graph[position[-1]]:
		point1 = graph[position[-1]][node][0]['limits']
		point2 = local_points[0]							
		cost = distance_two_points(point1,point2)
		graph[position[-1]][node][0]['weight'] = cost
		graph[position[-1]][node][0]['going'] = 'local'
	sp = dict(net.all_pairs_dijkstra_path(graph))
	path = sp[position[-1]][local]
	#Apos ser encontrado o path, e enviado para 'distance_two_nodes' que
	#vai ajudar a somar a distancias entre esse path e o tempo que o agente
	#levará para percorrer (o tempo é uma media da velocidade por segundo).
	return distance_two_nodes(graph,path)
# --------------------------------------------------------------------- #
# Distance between two nodes ------------------------------------------ #
def distance_two_nodes(graph,path):
	#Função auxiliar que ajudara a somar os 'weight' de cada aresta do
	#path dado na função.
	distance = 0
	for pos in range(len(path)):
		if(pos+1 < len(path)):
			if(pos == 0):
				distance = distance + graph[path[pos]][path[pos+1]][0]['weight']
				if(len(path) == 3):
					for keys in graph[path[pos]][path[pos+1]]:
						if(graph[path[pos]][path[pos+1]][keys]['going'] == path[pos+2]):
							distance = distance + graph[path[pos]][path[pos+1]][keys]['weight']
							break
					return [distance,distance/245.6,path]
			if(pos+2 < len(path)):
				for keys in graph[path[pos]][path[pos+1]]:
					if(graph[path[pos]][path[pos+1]][keys]['going'] == path[pos+2]):
						distance = distance + graph[path[pos]][path[pos+1]][keys]['weight']
						break
	return [distance,distance/245.6,path]
# --------------------------------------------------------------------- #
# The distance between two points ------------------------------------- #		
def distance_two_points(point1,point2):
	#Função responsavel por aplicar o teorema de pitagora (a distancia 
	#entre dois pontos é uma linha reta: X^2 + Y^2 = z^2), recebe dois 
	#pontos e calcula sua hipotenusa entre esses dois pontos.
	#O resultado dessa função é colocado nos 'weight' dos nodos nas funções 
	#create_graph_distance_two_nodes e search_path_two_nodes.
	x1 = 0
	y1 = 0
	x2 = 0
	y2 = 0
	if(point1[0] < point2[0]):
		x1 = point1[0]
		x2 = point2[0]
	else:
		x2 = point1[0]
		x1 = point2[0]
	if(point1[1] < point2[1]):
		y1 = point1[1]
		y2 = point2[1]
	else:
		y2 = point1[1]
		y1 = point2[1]
	cost = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
	return cost
# --------------------------------------------------------------------- #
