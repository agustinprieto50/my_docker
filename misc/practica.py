import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("Ryan", "Ermita", 9999999)

    def test_email(self):
        self.assertEqual("Ryan.Ermita@email.com", self.employee._email)

    def test_fullname(self):
        self.assertEqual("Ryan Ermita", self.employee._fullname)

    def test_apply_raise(self):
        self.assertEqual(9999999, self.employee._pay)
        self.employee.apply_raise()
        self.assertEqual(float(10499998.950000001), self.employee._pay)


if __name__ == "__main__":
    unittest.main()