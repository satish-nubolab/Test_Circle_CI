from hello import app
import unittest
from src.sample import Person

with app.test_client() as c:
    print("****************************Hello Circle CI***************************")
    response = c.get('/')
    assert response.data == b'Hello World!'


class Test(unittest.TestCase):
    def test_first(self):
        p = Person('abc')
        self.assertEqual(100, p.process_input(10, 10, 'multiple'))

    def test_sec(self):
        p = Person('abc')
        self.assertEqual(30, p.process_input(10, 20, 'add'))

    def test_third(self):
        p = Person('abc')
        self.assertEqual(5, p.process_input(100, 20, 'divide'))

    def test_fourth(self):
        p = Person('abc')
        self.assertEqual(30, p.process_input(50, 20, 'subtract'))

    def test_fifth(self):
        p = Person('abc')
        self.assertEqual(120, p.process_input(100, 20, 'add'))

    def test_sixth(self):
        p = Person('abc')
        self.assertEqual(200, p.process_input(100, 100, 'add'))

    def test_seventh(self):
        p = Person('abc')
        self.assertEqual(210, p.process_input(10, 200, 'add'))

    def test_eighth(self):
        p = Person('a')
        self.assertEqual("Invalid Input", p.process_input(10, 0, 'divide'))
