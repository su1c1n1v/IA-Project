import time
import networkx as net
import graph  as gph

enfermeiro_list = []
medico_list = []
doente_list = []
livro_list = []
cama_list = []
cadeira_list = []
mesa_list = []

# Init Variables ------------------------------------------------------ #
position = ['Corredor 2']
local_point = [[100,100]]
#graph = net.Graph()
graph = net.MultiGraph()
#gph.init_graph(graph)
speed = 245.6
# --------------------------------------------------------------------- #

def get_objects(obj):
	cathegory = obj[0].split("_")[0]
	dc = create_dictionary(obj)
	
	if(cathegory == 'enfermeiro'):
		if dc not in enfermeiro_list:
			enfermeiro_list.append(dc)
		show_dictionary(enfermeiro_list)
		
	elif cathegory  == 'medico':
		if dc not in medico_list:
			medico_list.append(dc)
		show_dictionary(medico_list)
		
	elif cathegory  == 'livro':
		if dc not in livro_list:
			livro_list.append(dc)
		show_dictionary(livro_list)
		
	else:
		print('nada')		
			
def create_dictionary(obj):
	dc_objets = {
		'name': obj[0],
		'cathegory':obj[0].split("_")[0],
		'local':'empty'
	}
	return dc_objets
		
def show_dictionary(list_dictionary):
	"""
	print('------------------------------')
	for x in list_dictionary:
		print(x['name'],' ',x['cathegory'])
		"""

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
		

	
def getActuallyPosition():
	return position

def call_shortest_path():
	path = gph.create_graph_distance_two_nodes(position,local_point,'Escadas',graph)
# Add Room or Object in the graph ------------------------------------- #
def refresh_graph(posicao):
	gph.searchRoomInGraph(getActuallyPosition(),posicao,graph)
# --------------------------------------------------------------------- #
def show_edges():
	gph.show_edges(graph)
