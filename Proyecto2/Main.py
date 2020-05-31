from ClaseBaseDeDatosMusica import BaseMusica
from neo4j import GraphDatabase
print('''Bienvenido al Sistema que recomienda Musica''')
print("")
print('''Los Creadores Juan Marroquin Y Carlos Raxtum le damos la bienvenida
Esperamos le guste el sistema de recomendacion

A continuacion el menu''')
cat=''
while cat!='Salir':
    cat=input('''
1. Crear Usuario
2. Login
3. Eliminar Datos de la base de Datos
4. Ver Las Canciones Disponible
5. Recomendar canciones similares a una Cancion que uste ponga?
6. Mostrar Grafo de relaciones
7. Fin de programa

Ingrese la funcion que desea usar:  ''')
    if cat=='6':
        print("")
        print("Gracias por hacer uso del sistema que recomineda Musica")
        break
    if cat=='1':
        print("")
        print("Cerga")
    if cat=='2':
        print("")
        print("2")
    if cat=='3':
        print("")
        print("3")
    if cat=='4':
        print("")
        print("pp")
    if cat=='5':
        print("")
        cancion = (input("Ingrese la cancion: "))
        n = BaseMusica()
        print(n.RecomendarCancion(cancion))
    else:
        print("")
        print("Porvafor seleccionar una opcion valida")
        
        