#Se importa la libreria networkx como nx
import networkx as nx
#Se importa la libreria pyplot de matplotlib como plt
import matplotlib.pyplot as plt

class grafos:
    def __init__(self):
        print("Diagrama generado en la imagen")
    def Diagrama(self):      
        #Se crea un grafo vacio
        G=nx.Graph()
        pos = nx.spring_layout(G)
        #Se crean los nodos:
        #Nodo Generos
        G.add_node("Idioma")

        #Se crean los nodos de los idiomas.
        G.add_nodes_from((["Ingles","Español"]))

        #Se crean los nodos de los generos
        G.add_nodes_from(["Hip Hop","Indie","Pop","Reggaeton","Rock","Trap","Trova"])

        #Se crean los nodos de los artistas
        G.add_nodes_from((["Rels B","Tame Impala", "Morat","Coldplay","Piso 21","Bad Bunny",
                           "J Balvin","KAROL G", "Limp Bizkit", "The Doors", "Red Hot Chili Peppers", "Eagles",
                           "Creedence Clearwater Revival","Radiohead","El Cuarteto De Nos","La Vela Puerca","Leiva",
                           "Anuel AA","Arcangel","Joaquín Sabina"]))

        #Se crean los nodos de las canciones
        G.add_nodes_from((["Take A Look Around","The Less I Know The Better", "Fix You","¿CÓMO TE VA, QUERIDA?",
                           "Break on Through (To the Other Side)","Break on Through (To the Other Side)",
                           "Una Vida Para Recordar","Amor Con Hielo", "No Me Ame", "Si Veo a Tu Mamá",
                           "Rojo", "Snow (Hey Oh)","Can't Stop","Yellow","The Scientist","Hotel California",
                           "Have You Ever Seen The Rain","Creep","Tusa","Amarillo", "Pirueta",
                           "Ya No Sé Que Hacer Conmigo","Zafar","Quién Me Ha Robado el Mes de Abril",
                           "Peor para el Sol", "Mi Pequeño Chernóbil"]))

        #Se crean los nodos de los años
        G.add_nodes_from((["1988","2019", "2015","2016","2005","2000","2002","2020", "2000", "2006", "2004",
                           "2002", "1970","1976", "1992"]))

        #Se crean los enlaces de los tipos de idiomas a idioma
        G.add_edge("Ingles","Idioma")
        G.add_edge("Español","Idioma")
        #Se crean los nodos de los tipos de generos a idiomas

        G.add_edge("Rock","Ingles")
        G.add_edge("Rock","Español")
        G.add_edge("Indie","Ingles")
        G.add_edge("Indie","Español")
        G.add_edge("Hip Hop","Ingles")
        G.add_edge("Hip Hop","Español")
        G.add_edge("Reggaeton","Ingles")
        G.add_edge("Reggaeton","Español")
        G.add_edge("Rock","Ingles")
        G.add_edge("Rock","Español")
        G.add_edge("Pop","Ingles")
        G.add_edge("Pop","Español")
        G.add_edge("Trap","Ingles")
        G.add_edge("Trap","Español")
        G.add_edge("Trova","Ingles")
        G.add_edge("Trova","Español")

        #Se crean los nodos de los tipos de artistas a idioma                  
        G.add_edge("Rels B","Hip Hop")
        G.add_edge("Tame Impala","Indie")
        G.add_edge("Morat","Pop",)
        G.add_edge("Coldplay","Pop")
        G.add_edge("Coldplay","Rock")
        G.add_edge("Piso 21","Reggaeton")
        G.add_edge("Bad Bunny","Reggaeton")
        G.add_edge("J Balvin","Reggaeton")
        G.add_edge("KAROL G","Reggaeton")
        G.add_edge("Limp Bizkit","Rock")
        G.add_edge("The Doors","Rock")
        G.add_edge("Red Hot Chili Peppers","Rock")
        G.add_edge("Creedence Clearwater Revival","Rock")
        G.add_edge("Eagles","Rock")
        G.add_edge("Radiohead","Rock")
        G.add_edge("El Cuarteto De Nos","Rock")
        G.add_edge("La Vela Puerca","Rock")
        G.add_edge("Leiva","Rock")
        G.add_edge("Anuel AA","Trap")
        G.add_edge("Arcangel","Trap")
        G.add_edge("Joaquín Sabina","Trova")

        #Se crean los nodos de los tipos de disco a artsta                  
        G.add_edge("¿CÓMO TE VA, QUERIDA?","Rels B")
        G.add_edge("The Less I Know The Better","Tame Impala")
        G.add_edge("Amor Con Hielo","Morat")
        G.add_edge("Fix You","Coldplay")
        G.add_edge("Yellow","Coldplay")
        G.add_edge("The Scientist","Coldplay")
        G.add_edge("Una Vida Para Recordar","Piso 21")
        G.add_edge("Si Veo a Tu Mamá","Bad Bunny")
        G.add_edge("Rojo","J Balvin")
        G.add_edge("Amarillo","J Balvin")
        G.add_edge("Tusa","KAROL G")
        G.add_edge("Take A Look Around","Limp Bizkit")
        G.add_edge("Break on Through (To the Other Side)","The Doors")
        G.add_edge("Snow (Hey Oh)","Red Hot Chili Peppers")
        G.add_edge("Can't Stop","Red Hot Chili Peppers")
        G.add_edge("Have You Ever Seen The Rain","Creedence Clearwater Revival")
        G.add_edge("Hotel California","Eagles")
        G.add_edge("Creep","Radiohead")
        G.add_edge("Ya No Sé Que Hacer Conmigo","El Cuarteto De Nos")
        G.add_edge("Zafar","La Vela Puerca")
        G.add_edge("Mi Pequeño Chernóbil","Leiva")
        G.add_edge("No Me Ame","Anuel AA")
        G.add_edge("Pirueta","Arcangel")
        G.add_edge("Peor para el Sol","Joaquín Sabina")
        G.add_edge("Quién Me Ha Robado el Mes de Abril","Joaquín Sabina")

        #Se crean los nodos de los tipos de cancion a artusta                  
        G.add_edge("¿CÓMO TE VA, QUERIDA?","Rels B")
        G.add_edge("The Less I Know The Better","Tame Impala")
        G.add_edge("Amor Con Hielo","Morat")
        G.add_edge("Fix You","Coldplay")
        G.add_edge("Yellow","Coldplay")
        G.add_edge("The Scientist","Coldplay")
        G.add_edge("Una Vida Para Recordar","Piso 21")
        G.add_edge("Si Veo a Tu Mamá","Bad Bunny")
        G.add_edge("Rojo","J Balvin")
        G.add_edge("Amarillo","J Balvin")
        G.add_edge("Tusa","KAROL G")
        G.add_edge("Take A Look Around","Limp Bizkit")
        G.add_edge("Break on Through (To the Other Side)","The Doors")
        G.add_edge("Snow (Hey Oh)","Red Hot Chili Peppers")
        G.add_edge("Can't Stop","Red Hot Chili Peppers")
        G.add_edge("Have You Ever Seen The Rain","Creedence Clearwater Revival")
        G.add_edge("Hotel California","Eagles")
        G.add_edge("Creep","Radiohead")
        G.add_edge("Ya No Sé Que Hacer Conmigo","El Cuarteto De Nos")
        G.add_edge("Zafar","La Vela Puerca")
        G.add_edge("Mi Pequeño Chernóbil","Leiva")
        G.add_edge("No Me Ame","Anuel AA")
        G.add_edge("Pirueta","Arcangel")
        G.add_edge("Peor para el Sol","Joaquín Sabina")
        G.add_edge("Quién Me Ha Robado el Mes de Abril","Joaquín Sabina")

        #Se crean los nodos de los tipos de cancion y año                
        G.add_edge("2019","¿CÓMO TE VA, QUERIDA?")
        G.add_edge("2015","The Less I Know The Better")
        G.add_edge("2016","Amor Con Hielo")
        G.add_edge("2005","Fix You")
        G.add_edge("2000","Yellow")
        G.add_edge("2002","The Scientist")
        G.add_edge("2019","Una Vida Para Recordar")
        G.add_edge("2020","Si Veo a Tu Mamá")
        G.add_edge("2020","Rojo")
        G.add_edge("2020","Amarillo")
        G.add_edge("2019","Tusa")
        G.add_edge("2000","Take A Look Around")
        G.add_edge("2000","Break on Through (To the Other Side)")
        G.add_edge("2006","Snow (Hey Oh)")
        G.add_edge("2002","Can't Stop")
        G.add_edge("1970","Have You Ever Seen The Rain")
        G.add_edge("1976","Hotel California")
        G.add_edge("1992","Creep")
        G.add_edge("2006","Ya No Sé Que Hacer Conmigo")
        G.add_edge("2004","Zafar")
        G.add_edge("2020","Mi Pequeño Chernóbil")
        G.add_edge("2019","No Me Ame")
        G.add_edge("2020","Pirueta")
        G.add_edge("1992","Peor para el Sol")
        G.add_edge("1988","Quién Me Ha Robado el Mes de Abril")


    # #recomendar al usuario
    # val = input("Ingrese un genero a escuchar")
    # for node in G:
    #     if (val == G.nodes("Hip Hop") or G.nodes("Indie") or G.nodes("Pop")or G.nodes("Reggaeton")
    #     or G.nodes("Rock") or G.nodes("Trap")or G.nodes("Trova")):
    #         print(G.nodes())
    #     else: 
    #         print("valor no encontrado")
        
        #Se dibuja el grafo
        nx.draw(G, with_labels=True)

        #Se muestra en pantalla
        plt.show()

        #Se vuelve a dibujar el grafo y se salva en un archivo png.
        nx.draw(G, with_labels=True)
        plt.savefig("networkx1.png")
        
        # #Se muestra información de los nodos (cantidad, nodos)
        print ("A continuacion se le msotrara todas las relaciones y los nodos del grafo:")
        print ("")
        print ("Nodos:")
        print ("Numero de nodos: ", G.number_of_nodes())
        print (G.nodes())
        #SE muestra información de los enlaces (cantidad, enlaces)
        print ("Enlaces:")
        print ("Numero de Enlaces: ", G.number_of_edges())
        print (G.edges())
        # 
        print ("Aristas:")
        print (G.edges())

#val = grafos()
#val.Diagrama()












