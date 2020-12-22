import time

enfermeiro_list = []
medico_list = []
doente_list = []
livro_list = []
cama_list = []
cadeira_list = []
mesa_list = []

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
	print('------------------------------')
	for x in list_dictionary:
		print(x['name'],' ',x['cathegory'])

	
