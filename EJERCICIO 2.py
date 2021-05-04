#CARLOS ENRIQUE CORONA NUÑEZ
#INGENIERIA EN SISTEMAS COMPUTACIONALES
#UMB SAN JOSE DEL RINCON

class Automovil:
    """
    Esta clase es para autos
    """
    marca= ""
    modelo=""
    color=""
    potencia=""
    kilometraje=""
    combustible=""
    Velocidad=""

auto1 = Automovil()
auto1.marca="Mustang"
auto1.modelo="1963"
auto1.color="rojo"
auto1.potencia="200 caballos de fuerza"
auto1.kilometraje="003898"
auto1.combustible="20 litros"
auto1.velocidad="200 km/h"

print(auto1.marca)
print(auto1.modelo)
print(auto1.color)
print(auto1.potencia)
print(auto1.kilometraje)
print(auto1.combustible)
print(auto1.velocidad)

class CompaniaTelefonica:
    """
    Esta clase es para una compania telefonica
    """
    nombre=""
    tarifa_por_minuto=None
    tarifa_por_sms=None

compania1=CompaniaTelefonica()
compania1.nombre="Telecel"
compania1.tarifa_por_minuto=1.98
compania1.tarifa_por_sms=.88

compania2=CompaniaTelefonica()
compania2.nombre="Movistar"
compania2.tarifa_por_minuto=1.73
compania2.tarifa_por_sms=.63

print(compania1.nombre)
print(compania1.tarifa_por_minuto)
print(compania1.tarifa_por_sms)

print(compania2.nombre)
print(compania2.tarifa_por_minuto)
print(compania2.tarifa_por_sms)

class Celular:
    """
    Esta clase es para celulares
    """
    marca=""
    modelo=""
    color=""
    compania_telefonica=""
    saldo=None

celular1=Celular()
celular1.marca="Samsung"
celular1.modelo="J8 2018"
celular1.color="negro"
celular1.compania_telefonica="Telcel"
celular1.saldo=120

celular2=Celular()
celular2.marca="Xiami"
celular2.modelo="Redmi Note 8s"
celular2.color="Blanco"
celular2.compania_telefonica="Telcel"
celular2.saldo=200

print(celular1.marca)
print(celular1.modelo)
print(celular1.color)
print(celular1.compania_telefonica)
print(celular1.saldo)

print(celular2.marca)
print(celular2.modelo)
print(celular2.color)
print(celular2.compania_telefonica)
print(celular2.saldo)

class Alumno:
    nombre=""
    grado=""
    grupo=""
    promedio_general=None

alumno1=Alumno()
alumno1.nombre="Angel Edgar Corona Nuñez"
alumno1.grado="2do grado"
alumno1.grupo="B"
alumno1.promedio_general=9.6

alumno2=Alumno()
alumno2.nombre="Carlos Enrique Corona Nuñez"
alumno2.grado="1er grado"
alumno1.grupo="A"
alumno2.promedio_general=9.3

print(alumno1.nombre)
print(alumno1.grado)
print(alumno1.grupo)
print(alumno1.promedio_general)

print(alumno2.nombre)
print(alumno2.grado)
print(alumno2.grupo)
print(alumno2.promedio_general)

class Materia:
    nombre=""
    clave_de_asignatura=None
    criterios_de_evaluacion=""

materia1=Materia()
materia1.nombre="MATEMATICAS"
materia1.clave_de_asignatura=32
materia1.criterios_de_evaluacion="trabajos en clase, proyecto, examen"

materia2=Materia()
materia2.nombre="INGLES"
materia2.clave_de_asignatura=34
materia2.criterios_de_evaluacion="proyecto, video, examen, participacion"

print(materia1.nombre)
print(materia1.clave_de_asignatura)
print(materia1.criterios_de_evaluacion)

print(materia2.nombre)
print(materia2.clave_de_asignatura)
print(materia2.criterios_de_evaluacion)





