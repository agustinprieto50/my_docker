from repository import Repository


class BookService():
    def add_book(self, book):
        lastKey = -1
        for legajo in Repository.booksList:
            lastKey = legajo
        lastKey = lastKey + 1
        Repository.booksList[lastKey] = book.__dict__
        return lastKey

    def update_book(self, idbook, book):
        legajo_existe = True
        for i in Repository.membersList:
            if i == idbook:
                legajo_existe = True
                break
        if legajo_existe:
            Repository.booksList[idbook] = book.__dict__
        raise ValueError

    def assign_book(self, idbook, member):
        legajo_existe = True
        for i in Repository.membersList:
            if i == idbook:
                legajo_existe = True
                break
        if legajo_existe:
            Repository.booksList[idbook]['_memberLegajo'] = member
        raise ValueError

    def delete_book(self, idbook):
        legajo_existe = True
        for i in Repository.membersList:
            if i == idbook:
                legajo_existe = True
                break
        if legajo_existe:
            del Repository.booksList[idbook]
        raise ValueError
