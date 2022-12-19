
#
x = "12"
    
print( x + str(1) )    
print( int(x) + 1 )    

x = 12                
print( x + 1 )

print( int(x) + 1 )

x = int( input( "Введите х = " ) )
if x < 10 :
    print( "x < 10" )
elif x < 20 :
    print( "10 - 20" )
elif x < 30 :
    print( "20 - 30" )
else :
    print( "other" )

if x > 10 and x < 20 :
    print( "10..20" )
elif x > 20 or x < 10 :
    print( "<10 or >20" )


