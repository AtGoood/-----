# Исключения
def throw() -> None :              
    print( "Raising TypeError" )
    raise TypeError              


def throw_value() :
    print( "Raising ValueError" )
    raise ValueError( "Error from 'throw_value()'" ) 


def no_throw() :
    print( "Normal activity" )


def main() :
    try :
       
    
        no_throw()
        pass   
    except TypeError :
        print( "Type error caught" )
    except ValueError as err :
        print( "Value error caught with msg: ", err )
    except :
        print( "Other error caught" )
    else :
        print( "Nothig caught - else block" )
    finally :
        print( "Any way finalizer" )


if __name__ == "__main__" :
    main()
