from bge import logic, events
from random import randin-t


def addText(cont , text):
    own     = cont.owner
    scene   = logic.getCurrentScene()
    #-------------------------------    
    if not "Text" in scene.objects:
        add_text = scene.addObject("Text")
        
        add_text["Text"] = text
        add_text.worldPosition.x = -8.50
        add_text.worldPosition.y = +23.00
                
        add_text.localScale[0] , add_text.localScale[1] = 1.500 , 1.500
        
        
        
def Maping(cont):
    own     = cont.owner
    scene   = logic.getCurrentScene()
    #-------------------------------
    object_size     = 2 
    caracter        = "x" 
    
    
    matriz  = [
               ["x","x","x","x","x","x","x","x"],
               ["x"," "," "," "," "," "," ","x"],
               ["x"," "," "," "," "," "," ","x"],
               ["x"," "," "," "," "," "," ","x"],
               ["x"," "," "," "," "," "," ","x"],
               ["x"," "," "," "," "," "," ","x"],
               ["x"," "," "," "," "," "," ","x"],
               ["x","x","x","x","x","x"," ","x"] 
               ]
    matriz.reverse()
    
    
    for row_index ,row in enumerate( matriz ):
        for col_index, col in enumerate( row ):
            
            pos_x = col_index * object_size
            pos_y = row_index * object_size
            
            
            if col == "x":
                cube = scene.addObject( "Cube" )
                
                cube.worldPosition.x = pos_x  - 6
                cube.worldPosition.y = pos_y  - 6
    
    
       
def start(cont):
    own = cont.owner
    scene = logic.getCurrentScene()
    #----
    ---------------------------         
    addText(cont , text= "Gerando um map de cubos")
  
    Maping(cont)
    
    
    
    pass



def update(cont):
    own = cont.owner
    scene = logic.getCurrentScene()
    #--------------------------------
    pass

