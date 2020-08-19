class Employee():
    def __init__(self, name=None, surname=None, pay=None):
        self._name = name
        self._surname = surname
        self._pay = pay
        self._email = self._name + "." + self._surname + "" + "@email.com"  
        self._fullname = "%s %s" % (self._name, self._surname)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def pay(self):
        return self._pay

    @pay.setter
    def pay(self, pay):
        self._pay = pay

    def apply_raise(self):
        self._pay = float(self._pay * 1.05)
