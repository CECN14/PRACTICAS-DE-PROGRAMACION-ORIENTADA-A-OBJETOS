#UMB SAN JOSE DEL RINCON
#INGENIERIA EN SISTEMAS COMPUTACIONALES
#DOCENTE: EDUARDO BECERRIL
#ALUMNO: CARLOS ENRIQUE CORONA NUÑEZ

#EJERCICIO 2:

class Cuenta:
    titular=""
    cantidad =150

per1 = Cuenta()
per1.titular=input("Ingresa tu nombre(obligatorio):")
per1.cantidad=input("Ingresa la cantidad:")
cant1=float(per1.cantidad)

mostrar = print("Nombre del titular:" + per1.titular + ",", "Cantidad:" + per1.cantidad)

def ingresar():
  if cant1>=0:
      print("El estado de la cuenta es:"+cant1)
  else:
      print("No se puede anexar esta cantidad")
def retirar():
    if cant1>0:
        cantidad=cant1-cant1

class CuentaJoven:
    titular = ""
    cantidad = None
    bonificacion=None
    edad=None
per1 = Cuenta()
per1.titular=input("Ingresa tu nombre(obligatorio):")
per1.edad=input("Escrib tu edad")
edad=int(per1.edad)
per1.cantidad=input("Ingresa la cantidad:")
cant1=float(per1.cantidad)
per1.bonificacion=input("Ingresa la cantidad de bonificacion:")
bon=float(per1.bonificacion)

mostrar = print("Nombre del titular:" + per1.titular + ",","Edad:"+per1.edad+",", "Cantidad:" + per1.cantidad,"Bonificacion:"+per1.bonificacion)

def esTitularValido():
    if edad>=18:
        print("El titular es valido")
    else
        print("EL tttular no es valido")
def retirar():
    if cant1>0:
        cantidad=cant1-cant1
def mostrar():

