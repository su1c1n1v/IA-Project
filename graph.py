import time
import math
import networkx as net

person_list = []
graph = net.Graph()

# Create Node ------------------------------------------ #

	#Criar nodo
	#graph.add_node('Sala 5')
	
	#Adicionar vertices a dois nodos
	#graph.add_edge('nome do nodo1','nome do nodo2',weight=[coordenadas do objeto])
	
	#Printar o nodo ou vertice
	#print(graph.edges()) #printa todos os vertices
	#print(graph.nodes()) #printa todos os nodos
	
	
# initial ------------------------------------------------------------- #
def init_graph():
	add_nodes('Corredor 1','Corredor 2',[[180,30],[180,70]])
	add_nodes('Corredor 1','Escadas',[[180,30],[180,70]])
	add_nodes('Corredor 1','Corredor 3',[[540,30],[540,135]])
	add_nodes('Corredor 2','Corredor 4',[[30,305],[85,305]])
	add_nodes('Corredor 3','Corredor 4',[[565,305],[635,305]])
# --------------------------------------------------------------------- #
# add_node ------------------------------------------------------------ #
def add_nodes(node1,node2,points):
	graph.add_edge(node1,node2)
	graph[node1][node2]['limits'] = points
# --------------------------------------------------------------------- #
# Search_Room --------------------------------------------------------- #
def searchRoomInGraph(localList,weight):
	if localList[-1] not in graph:
		graph.add_edge(localList[-1],localList[-2],weight=[weight])
		localList.clear()
# --------------------------------------------------------------------- #
# Show all edges ------------------------------------------------------ #
def showEdges():
	sp = dict(net.all_pairs_shortest_path(graph))
	print('Grafo ',graph.edges())
	for node in graph.nodes():
		print('|',node,'--------|')
		for edge in graph[node]:
			print(edge,'\n--Points:',graph[node][edge]['limits'],'\n--Shortest:',sp[node][edge])
		print('|------------------|')
# --------------------------------------------------------------------- #
# The shortest path --------------------------------------------------- #
def shortest_path(position,local_points):
	sp = dict(net.all_pairs_shortest_path(graph))
	graph_list = []
	print('Node:',position[-1])
	for edge in graph[position[-1]]:
		print('edge:',edge)
		x1 = 0
		y1 = 0
		x2 = 0
		y2 = 0
		
		if(graph[position[-1]][edge]['limits'][0][0] < local_points[0][0]):
			x1 = graph[position[-1]][edge]['limits'][0][0]
			x2 = local_points[0][0]
		else:
			x1 = local_points[0][0]
			x2 = graph[position[-1]][edge]['limits'][0][0]
		#-------------------------------------------------------------------
		if(graph[position[-1]][edge]['limits'][0][1] < local_points[0][1]):
			y1 = graph[position[-1]][edge]['limits'][0][1]
			y2 = local_points[0][1]
		else:
			y1 = local_points[0][1]
			y2 = graph[position[-1]][edge]['limits'][0][1]
		
		cost = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
		print(edge,'\nCusto:',cost)
# --------------------------------------------------------------------- #		
