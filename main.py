#UMB SAN JOSE DEL RINCON
#INGENIERIA EN SISTEMAS COMPUTACIONALES
#DOCENTE: EDUARDO BECERRIL
#ALUMNO: CARLOS ENRIQUE CORONA NUÑEZ

#EJERCICIO 1:

class Persona:

 nombre=""
 edad=None          #ATRIBUTOS DE LA CLASE
 DNI=""


persona1 = Persona()
persona1.nombre=input("Escribe tu nombre:")
persona1.edad=input("Ingresa tu edad:")          #ALMACENAMIENTO DE DATOS
edad=int(persona1.edad)
persona1.DNI=input("Ingresa tu DNI:")

mostrar=print("Nombre:"+persona1.nombre+",", "Edad:"+persona1.edad+"años"+",","DNI:"+persona1.DNI) #METODO MOSTRAR DATOS

def esmayor():
    edad=False                                 #METODO PARA DEFINIR SI LA PERSONA ES MENOR O MAYOR DE EDAD
if edad >=18:
    print("La persona es mayor de edad")
else:
    print("La persona es menor de edad")

