from bge import logic, events
from random import randint
from pprint import pprint, pformat
from ast import literal_eval
from map_gerenetion_ramdon import MapGeneration



def geretMap(cont):
    own   = cont.owner
    scene = logic.getCurrentScene()
    tc    = logic.keyboard.events
    m     = logic.mouse.events
    scene = logic.getCurrentScene()
    #--------------------------------
    e = cont.sensors["e"]
    #---------------------------------
    cube_size = 2
    map_assets = [ "x" , "y", " " ]

    

    if e.positive:
      Cla     = MapGeneration( assets_map_objects = map_assets )
      New_Map = Cla.finalNewMap( sizes = [ 15 , 15 ], numb_index_assets = 2 )

      Cla.objectsMap( matiz_map       = New_Map  ,
                object_map        = "Cube" , 
                object_size       = cube_size  ,  
                simbol_object_map = "x" 
                )


