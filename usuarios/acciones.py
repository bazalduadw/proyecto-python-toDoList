import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("*** REGISTRATE ***")
        nombre = input("Ingresa tu primer nombre: ")
        apellidos = input("Ingresa tus apellidos: ")
        email = input("Ingresa tu correo electronico: ")
        password = input("Ingresa una contrasena: ")
        print("* Registrando... *")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Usuario {registro[1].nombre} registrado con exito! Tu correo es {registro[1].email} ")
        else:
            print("Registro no completado, intenta de nuevo...")

    def login(self):
        print("*** INICIA SESION ***")

        try:

            email = input("Ingresa tu correo electronico: ")
            password = input("Ingresa tu contrasena: ")
            print("* Iniciando Sesion... *")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"""
                    * Bienvenido *
                Datos de la cuenta:
                    Usuario: {login[1]}
                    Correo: {login[3]}
                    Cuenta creada en: {login[5]}  
                """)
                self.proximasAcciones(login)

        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print("Error al iniciar sesion")
    
    def proximasAcciones(self, usuario):
        print("""
        *** ACCIONES DISPONIBLES ***
            -- MENU --
        Opcion 1: Crear Nota
        Opcion 2: Mostrar Notas
        Opcion 3: Eliminar Notas
        Opcion 4: Salir del programa
        """)

        accion = int(input("Que accion quieres hacer: "))
        hazEl = notas.acciones.Acciones()

        if accion == 1:
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == 2:
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == 3:
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 4:
            print("Saliendo del programa...")
            exit()
        
            

    