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

    # def insertion_sort_precio(self, lista, orden):
    #     if orden == str('ascendente'):
    # # We start from 1 since the first element is trivially sorted
    #         for index in range(1, len(lista)):
    #             currentValue = lista[index]["_precio"]
    #             currentPosition = index

    #             while currentPosition > 0 and lista[currentPosition - 1]
    #                   > currentValue:
    #                 lista[currentPosition] = lista[currentPosition - 1]
    #                 currentPosition = currentPosition - 1

    def insertion_sort_precio(self, lista, tipo_orden):
        if tipo_orden == str("ascendente"):
            largo_indice = range(1, len(lista))
            for i in largo_indice:
                sort = lista[i]

                while i > 0 and lista[i-1]["_precio"] > sort["_precio"]:
                    lista[i], lista[i-1] = lista[i-1], lista[i]
                    i = i-1

            return lista

        if tipo_orden == str("descendente"):
            largo_indice = range(0, len(lista))
            for i in largo_indice:
                sort = lista[i]

                while i > 0 and lista[i-1]["_precio"] < sort["_precio"]:
                    lista[i], lista[i-1] = lista[i-1], lista[i]
                    i = i-1

            return lista
