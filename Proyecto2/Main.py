from ClaseBaseDeDatosMusica import BaseMusica
from Grafo import grafos
from neo4j import GraphDatabase
from User import Usuario

def menu2():
    print("Bienvenido!")
    print("\n1. Eliminar Datos de la base de Datos\n2. Ver Las Canciones Disponible\n3. Recomendar canciones similares a una Cancion que uste ponga?\n4. Mostrar Grafo de relaciones")
    cat1 = input("Eleccion a realizar: ")
    if cat1=='1':
        print("")
        print("2")
    elif cat1=='2':
        print("")
        print("pp")
    elif cat1=='3':
        print("")
        cancion = (input("Ingrese la cancion: "))
        n = BaseMusica()
        print(n.RecomendarCancion(cancion))
    elif cat1=='4':
        print("")
        #from Grafo import grafos
        s = grafos()
        print(s.Diagrama())
    else:
        print("")
        print("No reconozco tu eleccion!")



print('''Bienvenido al Sistema que recomienda Musica''')
print("")
print('''Los Creadores Juan Marroquin y Carlos Raxtum le damos la bienvenida
Esperamos le guste el sistema de recomendacion

Eliga una accion!''')

cat=''
n1 = Usuario()
while cat!='Salir':
    cat=input('''
1. Crear Usuario
2. Login
3. Fin de programa

Ingrese la funcion que desea usar:  ''')
    if cat=='3':
        print("")
        print("Gracias por hacer uso del sistema que recomineda Musica")
        break
    elif cat=='1':
        id= (input("Ingrese el nombre de Usuario que quiere usar: "))
        pas = (input("Ingrese su nuevo password: "))
        n1.CrearUser(id,pas)
    elif cat=='2':
        id= (input("Ingrese el nombre de Usuario: "))
        pas = (input("Ingrese su nuevo password: "))
        n1.login(id,pas)
        if(n1.boolean == True):
            menu2()
    else:
        print("")
        print("No reconozco tu eleccion!")
        
        
        
        
