import unittest
import json
import os
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_id(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base()
        self.assertEqual(b2.id, 1)
        b3 = Base(["list", 1])
        self.assertEqual(b3.id, ["list", 1])
        b4 = Base(None)
        self.assertEqual(b4.id, 2)

    def test_objects_error(self):
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_to_json_string(self):
        d1 = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        self.assertCountEqual(Base.to_json_string(d1), '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
        d2 = [{"numero1": 5, "numero2": 1}]
        self.assertCountEqual(Base.to_json_string(d2), '[{"numero1": 5, "numero2": 1}]')
        d3 = []
        self.assertCountEqual(Base.to_json_string(d3), '[]')
        self.assertTrue(type(Base.to_json_string([])) is str)
        d3 = None
        self.assertCountEqual(Base.to_json_string(d3), '[]')
        self.assertTrue(type(Base.to_json_string(None)) is str)
        d4 = [{"x": 5}]
        self.assertCountEqual(Base.to_json_string(d4), '[{"x": 5}]')
        d5 = 1234
        self.assertCountEqual(Base.to_json_string(d5), '1234')
        

    def test_from_json_string(self):
        string = '[{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]'
        j_son = Base.from_json_string(string)
        self.assertTrue(type(j_son) is list)
        self.assertEqual(len(j_son), 2)
        self.assertTrue(type(j_son[0]) is dict)
        self.assertTrue(type(j_son[1]) is dict)
        self.assertEqual([], Base.from_json_string(""))
        self.assertEqual([], Base.from_json_string(None))

    def test_create(self):
        d = Rectangle(3, 5, 1)
        d1_dictionary = d.to_dictionary()
        d1 = Rectangle.create(**d1_dictionary)
        self.assertNotEqual(d, d1)
        s = Square(3, 5, 1)
        s1_dictionary = s.to_dictionary()
        s1 = Square.create(**s1_dictionary)
        self.assertNotEqual(s, s1)

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        r3 = [r1, r2]
        Rectangle.save_to_file(r3)
        r4 = Rectangle.load_from_file()
        self.assertEqual(r3[0].__str__(), '[Rectangle] (1) 2/8 - 10/7')
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        ls = [s1, s2]
        Square.save_to_file(ls)
        lso = Square.load_from_file()
        self.assertEqual(lso[0].__str__(), '[Square] (5) 0/0 - 5')

    def test_b_inst(self):
        b = Base()
        self.assertIsInstance(b, Base)

    def test_save_to_file(self):
        R_1 = Rectangle(10, 7, 2, 8)
        R_2 = Rectangle(2, 4)
        Rectangle.save_to_file([R_1, R_2])
        self.assertTrue(os.path.isfile('Rectangle.json'))
        S_1 = Square(10, 7, 2)
        S_2 = Square(8)
        Square.save_to_file([S_1, S_2])
        self.assertTrue(os.path.isfile('Square.json'))

    def test_pep8_base(self):
        self.assertEqual(os.system('pep8 models/base.py'), 0)

    def test_module_docstring(self):
        self.assertTrue(len(Base.__doc__) >= 1)
        self.assertTrue(len(Base.__init__.__doc__) >= 1)
        self.assertTrue(len(Base.create.__doc__) >= 1)
        self.assertTrue(len(Base.to_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.from_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.save_to_file.__doc__) >= 1)
        self.assertTrue(len(Base.load_from_file.__doc__) >= 1)

    def test_name_file(self):
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(hasattr(Base, "load_from_file"))

if __name__ == '__main__':
    unittest.main()
