import notas.nota as modelo

class Acciones:
    
    def crear(self, usuario):
        print(" Crea una nota ")
        titulo = input("Titulo de la nota: ")
        descripcion = input("Descripcion de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print("Nota guardada con exito")
        else:
            print("Hubo un error al guardar la nota")
    
    def mostrar(self, usuario):
        print(" ** LISTA DE NOTAS ** ")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        
        for nota in notas:
            print("*******")
            print(f"Titulo: {nota[2]}")
            print(f"Descripcion: {nota[3]}")

    def borrar(self, usuario):
        print(" ** BORRAR NOTAS ** ")
        titulo = input("Introduce el titulo de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f" Nota: {nota.titulo} eliminada con exito")
        else:
            print("Hubo un error al eliminar la nota, intenta de nuevo")