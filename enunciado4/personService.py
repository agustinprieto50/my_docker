from repository import Repository


class PersonService:
    lista = Repository.person

    def get_personList(self):
        return Repository.person

    # Agrega una persona en el dicionario person, definido en Repository
    def add_person(self, person):
        lastKey = -1
        for key in Repository.person:
            lastKey = key
        lastKey = lastKey + 1
        Repository.person[lastKey] = person

    # Actualiza datos de una person del diccionario person
    def update_person_name(self, key, name):
        new_name = {'_name': name.upper()}
        self.lista[key].update(new_name)
        print(self.lista)

    def update_person_surname(self, key, surname):
        new_surname = {'_surname': surname.upper()}
        self.lista[key].update(new_surname)
        print(self.lista)

    def update_person_age(self, key, age):
        # modifica la edad
        new_age = {'_age': age}
        self.lista[key].update(new_age)
        print(self.lista)

    # Elimina persona segun key del dic person
    def delete_person(self, key):
        del self.lista[key]
