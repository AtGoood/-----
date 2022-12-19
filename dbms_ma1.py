# подключение к basedate


import mariadb        

def main( pars ) :
    try :
        connection = mariadb.connect( **pars )
    except mariadb.Error as err :
        print( err )
    else :
        print( "Connection OK" )
    return


if __name__ == "__main__" :
    pars = {
        "host":     "localhost",
        "port":     3306,
        "database": "py1911",
        "user":     "py191_user",
        "password": "pass_191",
    }
    main( pars )   
