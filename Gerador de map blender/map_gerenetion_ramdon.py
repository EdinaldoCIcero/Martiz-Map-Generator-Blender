from bge import logic, events
from random import randint
from pprint import pprint, pformat
from ast import literal_eval



class MapGeneration():
	def __init__(self , assets_map_objects ):

		self.map_assets = assets_map_objects 
		self.new_map 	= []

		pass

	def makerCols(self  , size_x , numb_index_assets ):
		lis = []

		for i in range( size_x ):
			ran = randint(0 , numb_index_assets )

			lis.append( self.map_assets[ran] )

		return lis
		pass

	def finalNewMap(self , sizes , numb_index_assets ):
		row = []

		for rows in range( sizes[1]) :
			cols = self.makerCols( size_x = sizes[0] , numb_index_assets = numb_index_assets )
			row.append( cols )

		return row
		pass


	def objectsMap(self, matiz_map , object_map , object_size ,  simbol_object_map ):
		scene = logic.getCurrentScene()

		for i in scene.objects:
		    if "terreno" in i :
		      i.endObject()
		      pass

		for row_index , row in enumerate( matiz_map ):
		    for col_index , col in enumerate( row ):
		      pos_x = col_index * object_size
		      pos_y = row_index * object_size

		      if col == simbol_object_map :
		        cube = scene.addObject( object_map )
		        cube.worldPosition.x = pos_x 
		        cube.worldPosition.y = pos_y
