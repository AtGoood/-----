
x = 14
y = 6
print( x + y )

print( "x - y = %d, x / y = %f" % (x - y, x / y) )  
print( "x * y = %d" % (x * y) )
print( "x // y = %f" % (x // y) )  
print( "x ** y = ", x ** y, sep = '' )  
print( "x % y =", x % y )


for i in range(10) :   
    print( i, end = ', ' )   
print()  

for i in range(1, 10) :  
    print( i, end = ', ' )
print()

for i in range(1, 10, 2) :   
    print( i, end = ', ' )
print()

for i in range(10, 1, -2) :   
    print( i, end = ', ' )
print()

x = 10 if y < 5 else 20

'''
    Д.З. Использовать цикл while: реализовать ввод пользователем двух
    разных чисел (повторять запрос второго числа пока оно совпадает с первым)
    * ограничить ввод положительных чисел (на другое - повторять запрос)
'''