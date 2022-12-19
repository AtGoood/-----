
import json          

def main() :
    try :
        with open( "sample.json" ) as f :
            j = json.load( f )
    except :
        print( "JSON load or parse error" )
        return
    print( type(j), j )           
    print( "------------------------------" )
    for k in j :                 
        print( k, j[k],          
            type( j[k] ) )     
    print( "------------------------------" )
    for v in j.values() :        
        print( v )             
    print( "--------------------------" )
    for k,v in j.items() :        
        print( k, ':', v )
    print( "----------------------------" )
    j["newItem1"] = "New item 1"  
    j["d"] = 321                  
    j["newItem2"] = "Привет"     
    print(                       
        json.dumps( j,            
            indent = 4,          
            ensure_ascii = False 
    ) )
    try :
        with open( "sample2.json", "w" ) as f :
            json.dump( j, f )    
    except :
        print( "File write error" )
    else :
        print( "File write OK" ) 
    


if __name__ == "__main__" :
    main()
