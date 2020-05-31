class Usuario:
    id = ""
    pas = ""
    boolean = False
    MusicaFav = []
    ArtistasFav = []
    GenerosFav = []
    #iniciar el  objecto
    def __init__(self):
        print("creado")
    #metodo crear ususario
    def CrearUser(self, id, pas):
        self.id = id
        self.pas = pas
        print("Usuario",id, "ha sido creado")
    #metodo login
    def login(self, id, pas):
        print (self.id)
        if self.id == id and self.pas == pas and self.boolean == False:
            self.boolean = True
            print ("Login success!")
        else:
            boolean = False
            print("No se encuentra ese Usario")
    def ChangePassWord(self,id,pas):
        if self.id == id:
            self.pas = pas
        else:
            print("El usuario no se encuentra, no se puede cambiar la contrasena")
        
#n1 = Usuario()
#n1.CrearUser("perro","123")
#n1.login("perro","123")
#print("")
#print(n1.boolean)
