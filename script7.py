

def input_number() -> int :
    while True :
        x = input( "Enter number: " )
        try :
            x = int( x )
        except ValueError :
            print( "Input should be a numeric. ", end = '' )
        else :
            break
    
    return x


def input_positive_number() -> int :   
    '''Read number from std input, checks it to be positive numeric'''
    while True :
        x = input( "Enter number: " )
        try :
            x = int( x )
        except ValueError :
            print( "Input should be a numeric. ", end = '' )
        else :
            if x <= 0 :
                print( "Number should be positive. ", end = '' )
            else :
                break
  
    return x


def main() -> None :
    x = input_positive_number()
    print( x )


if __name__ == "__main__" :
    main()