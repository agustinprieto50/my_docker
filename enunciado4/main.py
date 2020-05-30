from person import Person
from personService import PersonService


if __name__ == '__main__':
    personService = PersonService()

    # creamos un menu
    counter = 1
    while counter != 0:
        counter += 1
        print('\nOpciones: ')
        print('\n1. Agregar una persona')
        print('2. Actualizar datos de una persona')
        print('3. Borrar persona')
        print('4. Mostrar lista')
        opcion = int(input('\nElija una opcion: '))

        # agregamos una persona
        if opcion == 1:
            p1 = Person()
            p1._name = str(input('Nombre: '))
            p1._surname = str(input('Apellido: '))
            p1._age = int(input('Edad: '))
            p1 = Person.get_person(p1)
            personService.add_person(p1)
            print('\nPersona agregada con exito.')

        # actualizamos datos de una persona
        if opcion == 2:
            print('\n1. Modificar nombre')
            print('2. Modificar apellido')
            print('3. Modificar edad')
            key = int(input('\nElija la key de la persona que desea modificar: '))
            opcionUpdate = int(input('Elija lo que desea modificar: '))

            if opcionUpdate == 1:
                new_name = str(input('\nNuevo nombre: '))
                personService.update_person_name(key, new_name)
            elif opcionUpdate == 2:
                new_surname = str(input('Nuevo apellido: '))
                personService.update_person_surname(key, new_surname)
            elif opcionUpdate == 3:
                new_age = str(input('Nueva edad: '))
                personService.update_person_age(key, new_age)

        # eliminamos una persona del diccionario
        if opcion == 3:
            key_delete = int(input('Ingrese la key de la persona que desea borrar: '))
            personService.delete_person(key_delete)
            print(personService.lista)

        # mostramos la lista
        if opcion == 4:
            print(personService.get_personList())
        
        if opcion == 5:
            break
