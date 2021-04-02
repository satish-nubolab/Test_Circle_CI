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
        self.assertEqual(30, p.process_input(10, 20, 'add'))
