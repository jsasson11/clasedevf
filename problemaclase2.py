 
#encuentra los multiplos de 3 y 5 por debajo del 1000 y despues dame la sumatoria
#n=0
#f=0
#while n <1000:
#    if n%3==0 or n%5==0:   #el % saca el residuo de una division
#        f+=n  #+= "agregar" ....0 +=n cuando n=1 entonces lo suma..suma la variable.
#        print n, "es multiplo de 3 o de 5"
#    n=n+1
#print "la suma de los multiplos es:",f

#print()
#''' jdjdjd
#'''

#operadores de python
#variables definidas camelcase para tener mejor legibilidad empiezan con minuscula y la segunda con mayus
#numeroUno  numero_uno

num_uno=5
num_dos=10
print (num_uno/num_dos) #division normal .5
print (num_uno//num_dos) #division perfecta...te regresa namas el entero 1
num_uno != num_dos #desigual a 
num_uno==5 and num_uno<10 #el and se tienen que cumplir todas las condiciones que le exiges
num_uno==5 or num_uno<4 #or solo necesita que se cumpla 1 de cualquiera de las condiciones que estoy poniendo....si no se cumple ninguna condicion regresa false

miArreglo=[1,2,"paco",True] #array o arreglo es una lista...valores u objetos
miArreglo[2] #paco
len(miArreglo) #es el largo que tiene, la longitud
miArreglo[2]="javier" #es para cambiar paco a javier
miArreglo.append("nuevo valor papa") #agregar valor o variable
miArreglo.append(num_uno)
del miArreglo[2] #eliminar el valor
miArreglo.insert(0,"lo meti en 0") #la diferencia entre append es que aqui le dices en que valor lo quieres meter
#es una funcion que pide dos argumentos..en que indice lo quieres agregar y el valor
#los arreglos pueden hacer un inception...podemos tener un arreglo dentro de otro arreglo
miArreglo=[] #aqui limpie el arreglo
miArreglo=["a","b"] #una sola dimension
miArreglo.append([1,2]) #estas metiendo un arreglo porque el 1 y 2 estan entre corchetes
miArreglo[2] #aqui te regresa el arreglo porque esta en subindice 2
miArreglo[2][1] #aqui estoy llamando al arreglo que esta en el subindice 2 osea el [1,2] y despues sobre ese arreglo accedo al subindice 1...osea te regresa el numero 2
