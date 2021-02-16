"""
PROYECTO PYTHON MYSQL
- Abrir un menu
    Opcion 1 Login:
        Inicias Sesion con correo y password
            Se abre un menu
                1-Crear Nota
                2-Mostrar notas
                3-Borrar Nota
                4-Salir

    Opcion 2 Registro:
        Registrarse con nombre, appelidos, correo y password
"""
from usuarios import acciones

while True:
    print("""
    *** BIENVENIDO ***
        -- MENU --
    Opcion 1: Login
    Opcion 2: Registro
    Opcion 3: Salir
    """)
    try:
        hazEl = acciones.Acciones()
        accion = int(input("Que acciones escoges? "))

        if accion == 1:
            hazEl.login()
        elif accion == 2:
            hazEl.registro()
        elif accion == 3:
            print("Saliendo del progama...")
            break
        else:
            print("Opcion no valida")
    except ValueError:
        print("Introduce los datos correctamente")
    except Exception as e:
        print("Hay algun error: ", e)