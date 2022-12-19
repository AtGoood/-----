

class MyClass :                   
    x = 10                     
                                   
                                    
def main() -> None :               
    obj1 = MyClass()             
    obj2 = MyClass()             
  
    MyClass.x = 15             
    print( obj1.x, obj2.x )      
    obj1.x = 20                  
    obj2.y = 30                 
    print( obj1.x, obj2.x )      
    del obj2.y                  


if __name__ == "__main__" :
    main()
