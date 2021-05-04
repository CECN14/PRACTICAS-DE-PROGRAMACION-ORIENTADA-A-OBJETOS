#CARLOS ENRIQUE CORONA NUÑEZ
# INGENIERIA EN SISTEMAS COMPUTACIONALES
# UMB SAN JOSE DEL RINCON

#=========MATRICES QUE SE USAN========
#SUMA DE MATRICES
a= [[30, 10, 50],
    [21, 18, 35],
    [12, 22, 11]]

b= [[87, 90, 50],
    [11, 32, 41],
    [10, 76, 13]]
def suma_matrices(m1,m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[1][j]+ m2[i][j])
                return m3
            else:
                return None
c = suma_matrices(a, b)
if c == None:
    print("No se pueden sumar las matrices")
else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
            print("]")
