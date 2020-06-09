from repository import Repository


class BookService:
    def get_bookList(self):
        return Repository.booksList

    def add_book(self, book):
        lastKey = -1
        for bookKey in Repository.booksList:
            lastKey = bookKey
        lastKey = lastKey + 1
        Repository.booksList[lastKey] = book.__dict__
        return lastKey

    def update_book(self, bookKey, book):
        if bookKey not in Repository.booksList:
            raise ValueError
        Repository.booksList[bookKey]['_name'] = book.name
        Repository.booksList[bookKey]['_authorName'] = book.authorName
        Repository.booksList[bookKey]['_memberLegajo'] = book.memberLegajo

    def assign_book(self, id_book, member_legajo):
        if id_book not in Repository.booksList:
            raise ValueError

        if member_legajo not in Repository.membersList:
            raise ValueError

        Repository.booksList[id_book]['_memberLegajo'] = member_legajo

    def delete_member(self, bookKey):
        if bookKey not in Repository.booksList:
            raise ValueError
        del Repository.booksList[bookKey]
