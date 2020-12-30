import time
import math
import networkx as net

# Create Node ------------------------------------------ #

	#Criar nodo
	#graph.add_node('Sala 5')
	
	#Adicionar vertices a dois nodos
	#graph.add_edge('nome do nodo1','nome do nodo2',weight=[coordenadas do objeto])
	
	#Printar o nodo ou vertice
	#print(graph.edges()) #printa todos os vertices
	#print(graph.nodes()) #printa todos os nodos
	
	
# initial ------------------------------------------------------------- #
def init_graph(graph):
	add_nodes('Corredor 1','Corredor 2',[180,50],graph)
	add_nodes('Corredor 1','Escadas',[180,50],graph)
	add_nodes('Corredor 1','Corredor 3',[540,80],graph)
	add_nodes('Corredor 2','Corredor 4',[57,305],graph)
	add_nodes('Corredor 3','Corredor 4',[600,305],graph)
# --------------------------------------------------------------------- #
# add_node ------------------------------------------------------------ #
def add_nodes(node1,node2,points,graph):
	graph.add_edge(node1,node2)
	graph[node1][node2]['limits'] = points
# --------------------------------------------------------------------- #
# Search_Room --------------------------------------------------------- #
def searchRoomInGraph(localList,weight,graph):
	if localList[-1] not in graph:
		add_nodes(localList[-1],localList[-2],weight,graph)
		localList.clear()
# --------------------------------------------------------------------- #
# Show all edges ------------------------------------------------------ #
def showEdges(graph):
	sp = dict(net.all_pairs_dijkstra_path(graph))
	print('Grafo ',graph.edges())
	for node in graph.nodes():
		print('|--------',node,'--------|')
		for edge in graph[node]:
			print('	Edge:',edge)
# --------------------------------------------------------------------- #
# The shortest path --------------------------------------------------- #
def shortest_path(position,local_points,local,graph):
	sp = dict(net.all_pairs_shortest_path(graph))
	for node in graph[position[-1]]:
		point1 = graph[position[-1]][node]['limits']
		point2 = local_points[0]							
		cost = distance_two_points(point1,point2)
		graph[position[-1]][node]['weight'] = cost	
	for node in graph.nodes():
		if node != position[-1]:
			for edge1 in graph[node]:
				point1 = graph[node][edge1]['limits']
				if(len(graph[node]) > 1):
					for edge2 in graph[node]:	
						if(edge2 != edge1 and edge2 != position[-1] and edge1 != position[-1]):
							point2 = graph[node][edge2]['limits']
							cost = distance_two_points(point1,point2)
							graph[node][edge2]['weight'] = cost
	print('Distancia ate escada:',sp[position[-1]][local])
	return sp[position[-1]][local]
# --------------------------------------------------------------------- #
# The distance between two points ------------------------------------- #		
def distance_two_points(point1,point2):
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
