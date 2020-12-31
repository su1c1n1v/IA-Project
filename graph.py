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
	
# add_node ------------------------------------------------------------ #
def add_nodes(node1,node2,points,graph):
	graph.add_edge(node1,node2,limits=points[:],weight=0)
# --------------------------------------------------------------------- #
# Search_Room --------------------------------------------------------- #
def searchRoomInGraph(localList,weight,graph):
	if len(localList) > 1:
		if graph.has_edge(localList[-1],localList[-2]):
			return
		else:
			add_nodes(localList[-1],localList[-2],weight,graph)
			print(graph.edges())
# --------------------------------------------------------------------- #
# Show all edges ------------------------------------------------------ #
def show_edges(graph):
	sp = dict(net.all_pairs_dijkstra_path(graph))
	print('Grafo ',graph.edges())
	for node in graph.nodes():
		print('|--------',node,'--------|')
		for edge in graph[node]:
			print('	Edge:',edge,graph[node][edge])
# --------------------------------------------------------------------- #
# The new shortest path ----------------------------------------------- #
def create_graph_distance_two_nodes(position,local_points,local,graph):
	graph2 = graph.copy()
	for node in graph2[position[-1]]:
		point1 = graph2[position[-1]][node][0]['limits']
		point2 = local_points[0]							
		cost = distance_two_points(point1,point2)
		graph2[position[-1]][node][0]['weight'] = cost
		print(position[-1],node,cost)	
	for node in graph2.nodes():
		if node != position[-1]:
			for edge1 in graph2[node]:
				point1 = graph2[node][edge1][0]['limits']
				if(len(graph2[node]) > 1):
					for edge2 in graph2[node]:
						if(edge2 != edge1 and edge1 != position[-1]):
							point2 = graph2[node][edge2][0]['limits']
							print('Center:',node,'|Node 1:',edge1,'|Node 2:',edge2)	
							cost = distance_two_points(point1,point2)
							graph2.add_edge(node,edge2,limit=point2,weight=cost,comming=edge1)
							graph2[node][edge2][0]['weight'] = cost
							graph2[node][edge2][0]['comming'] = edge1
	search_path_two_nodes(graph2,local_points,position,local)
# --------------------------------------------------------------------- #
# Search the best path for two nodes ---------------------------------- #
def search_path_two_nodes(graph,local_points,position,local):
	for node in graph[position[-1]]:
		point1 = graph[position[-1]][node][0]['limits']
		point2 = local_points[0]							
		cost = distance_two_points(point1,point2)
		graph[position[-1]][node][0]['weight'] = cost
		graph[position[-1]][node][0]['comming'] = 'local'
	sp = dict(net.all_pairs_shortest_path(graph))
	path = sp[position[-1]][local]
	distance_two_nodes(graph,path)
# --------------------------------------------------------------------- #
# Distance between two nodes ------------------------------------------ #
def distance_two_nodes(graph,path):
	distance = 0
	for pos in range(len(path)):
		if(pos+1 < len(path)):
			if(pos == 0):
				distance = distance + graph[path[pos]][path[pos+1]][0]['weight']
				if(len(path) == 3):
					for keys in graph[path[pos]][path[pos+1]]:
						if(graph[path[pos]][path[pos+1]][keys]['comming'] == path[pos+2]):
							distance = distance + graph[path[pos]][path[pos+1]][keys]['weight']
							break
					print('Distance:',distance,'\nTime:',distance/245.6,'\nPath:',path)
					return	
			if(pos+2 < len(path)):
				for keys in graph[path[pos]][path[pos+1]]:
					if(graph[path[pos]][path[pos+1]][keys]['comming'] == path[pos+2]):
						distance = distance + graph[path[pos]][path[pos+1]][keys]['weight']
						break
	print('Distance:',distance,'\nTime:',distance/245.6,'\nPath:',path)
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
