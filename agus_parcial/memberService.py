from repository import Repository


class MemberService():
    lista = Repository.membersList

    def add_member(self, member):
        finalKey = -1
        for legajo in Repository.membersList:
            finalKey = legajo
        finalKey = finalKey + 1
        Repository.membersList[finalKey] = member.__dict__
        return finalKey

    def update_member(self, legajo, member):
        legajo_existe = True
        for i in Repository.membersList:
            if i == legajo:
                legajo_existe = True
                break
        if legajo_existe:
            Repository.membersList[legajo] = member.__dict__
        raise ValueError

    def delete_member(self, legajo):
        legajo_existe = True
        for i in Repository.membersList:
            if i == legajo:
                legajo_existe = True
                break
        if legajo_existe:
            del Repository.membersList[legajo]
        raise ValueError
