






class fruits():
 
    def __init__(self):
        
        self.__date= "2022/12/11"
        self._seller="ahmed"
        self.manager="mohmmed"
    
    def __del__(self):
      None

    def type(self):
        pass

 
class i(fruits):
 
    # from abstract method
    def type(self):
        print("fruit")

class potatos(i): 
     def type(self): 
       print("Vegetable") 

     def color(self):
        print("brown")
    
class bannana(i): 
     def type(self): 
       print("Fruit") 

     def color(self):
        print("Yellow")
    
      
def func(obj): 
       obj.type() 
     
        
obj_t = potatos() 
obj_a = bannana() 
func(obj_t) 
func(obj_a)

