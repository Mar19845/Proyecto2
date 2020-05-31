class Usuario:
    id = ""
    pas = ""
    boolean = 0
    def __init__(self):
        print("creado")
    def CrearUser(self, id, pas):
        self.id = id
        self.pas = pas
        self.boolean = 1
        print("Usuario",id, "ha sido creado")

    def login(self, id, pas):
        print (self.id)
        if self.id == id and self.pas == pas and boolean == 1:
            print ("Login success!")
        else:
            print("No se encuentra ese Usario")

log = Usuario()
#log.CrearUser("Peru","123")
log.login(input("Enter Login ID: "),
          input("Enter password: "))