from repositorios import Repositorios


class ProductoService():

    def add_producto(self, producto):
        lastKey = -1
        for key in Repositorios.productosList:
            lastKey = key
        new = int(lastKey) + 1
        Repositorios.productosList[new] = producto.__dict__
        return new

    def delete_producto(self, num):
        if num not in Repositorios.productosList:
            raise ValueError("El producto no existe")
        else:
            del Repositorios.productosList[num]

    def get_productosList(self):
        return Repositorios.productosList

    def update_producto(self, key, producto):
        if key not in Repositorios.productosList:
            raise ValueError("El producto no existe")
        Repositorios.productosList.update({key: producto.__dict__})
