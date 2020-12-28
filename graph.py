import time
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

def initGraph():

	
	# ---------------------- #
	graph.add_edge('Corredor 1','Corredor 2',weight=[[180,30],[180,70]])
	graph.add_edge('Corredor 1','Escadas',weight=[[180,30],[180,70]])
	graph.add_edge('Corredor 1','Corredor 3',weight=[[540,30],[540,135]])
	graph.add_edge('Corredor 2','Corredor 4',weight=[[30,305],[85,305]])
	graph.add_edge('Corredor 3','Corredor 4',weight=[[565,305],[635,305]])
	
	
	'''
	# ------como acessar os pesos------ #
	print('Grafo ',graph.edges())
	print('Grafo ',graph['Corredor 1']['Corredor 2']['weight'])
	for node in graph.nodes():
		print('|',node,'--------|')
		for edge in graph[node]:
			print('Edge: ',edge,'\nPeso:',graph[node][edge]['weight'])
		print('|------------|')
		
	'''
	
# ------------------------------------------------------ #		
