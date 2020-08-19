from productoServices import ProductoService
from producto import Producto

if __name__ == "__main__":
    service = ProductoService()

    counter = 1
    while counter != 0:
        counter += 1
        print('\nOpciones: ')
        print('\n1. Agregar')
        print('2. Actualizar ')
        print('3. Borrar')
        print('4. Mostrar lista')
        opcion = int(input('\nElija una opcion: '))

        if opcion == 1:
            p1 = Producto()
            p1._descripcion = str(input('Descripcion: '))
            p1._tipo = str(input('Tipo: '))
            p1._precio = int(input('Precio: '))
            service.add_producto(p1)
            print('\nProducto agregada con exito.')

        if opcion == 2:
            key = int(input('\nElija la key de la persona que desea modificar: '))
            p2 = Producto()
            p2._descripcion = str(input('\nNueva descripcion: '))
            p2._tipo = str(input('\nNuevo tipo: '))
            p2._precio = int(input('\nNuevo precio: '))

            service.update_producto(key, p2)

        if opcion == 3:
            key_delete = int(input('Ingrese la key del producto que desea borrar: '))
            service.delete_producto(key_delete)
            print(service.get_productosList())

        if opcion == 4:
            print(service.get_productosList())

        if opcion == 5:
            break
