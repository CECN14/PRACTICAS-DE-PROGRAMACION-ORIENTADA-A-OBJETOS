#CARLOS ENRIQUE CORONA NUÑEZ
#INGENIERIA EN SISTEMAS COMPUTACIONALES
#UMB SAN JOSE DEL RINCON

class Persona:
    """
    Esta clase es para una persona
    """
    nombre= ""
    apellido=""
    edad=None
    direccion=""
    correo=""

persona1 = Persona()
persona1.nombre="Carlos Enrique"
persona1.apellido="Corona Nuñez"
persona1.edad=18
persona1.direccion="Manzan 4, La Magdalena Cruz Blanca"
persona1.correo="coronanunezcarlosenrique@gmail.com"

persona2 = Persona()
persona2.nombre="Carlos"
persona2.apellido="Corona Miguel"
persona2.edad=47
persona2.direccion="Chabacano 3 , La Magdalena COlonia"
persona2.correo="coronamiguelcarlos@gmail.com"

print(persona1.nombre)
print(persona1.apellido)
print(persona1.direccion)
print(persona1.correo)

print(persona2.nombre)
print(persona2.apellido)
print(persona2.direccion)
print(persona2.correo)

class Mascota :
    """
    Esta clase es para una mascota
    """
    especie=""
    raza=""
    color=""
    nombre=""
    edad=None

mascota1=Mascota()
mascota1.especie="Perro"
mascota1.raza="pug"
mascota1.color="cafe"
mascota1.nombre="Ramon"
mascota1.edad=15

mascota2=Mascota()
mascota2.especie="Perro"
mascota2.raza="Pastor Aleman"
mascota2.color="blanco"
mascota2.nombre="Milo"
mascota2.edad=5

print(mascota1.especie)
print(mascota1.raza)
print(mascota1.color)
print(mascota1.nombre)
print(mascota1.edad)

print(mascota2.especie)
print(mascota2.raza)
print(mascota2.color)
print(mascota2.nombre)
print(mascota2.edad)

