#!/usr/bin/python3
import unittest
import json
import os
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys
from unittest.mock import patch

class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0
    
    def test_increment_id_Rectangule(self):
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Square(2)
        self.assertEqual(r2.id, 2)
        r3 = Square(5, 7, 8, 9)
        self.assertEqual(r3.id, 9)
        r4 = Square(5, 7, 8)
        self.assertEqual(r3.id, 9)
    
    def test_size_Rectangule(self):
        r1 = Square(10, 2)
        self.assertEqual(r1.size, 10)
        r2 = Square(2)
        self.assertEqual(r2.size, 2)
        r3 = Square(5, 7, 8, 9)
        self.assertEqual(r3.size, 5)
        r4 = Square(5, 7, 8)
        self.assertEqual(r3.size, 5)

    def test_exepc(self):
        with self.assertRaises(TypeError):
            s3 = Square(9.2, 2.8)
            s4 = Square(None)
            s5 = Square(-5, 9)
            s6 = Square(9, -5)
            s7 = Square()
            s8 = Square("hola")
            s9 = Square(10, "2")
            s10 = Square(10, 2, 3, -1)
            s11 = Square(10, 2, "3", 1)
            s12 = Square(1, 1, 1, 1, 1)
            s12.size = "Hola"
            s = Square()
            s13 = Square(hola)
            s14 = Square(1, hola)
            s15 = Square(5, 5, hola)
            s16 = Square(5, 5, hola)
        with self.assertRaises(ValueError):
            s3 = Square(-2)
            s4 = Square(0)
            s3 = Square(9, -5)
            s4 = Square(9, 9, -5)

    def test_create_square(self):
        s1 = Square(5, 3, 2, 2)
        s2 = Square(5, 3, 2, 2)
        s3 = Square(10)
        self.assertEqual(s3.__str__(), "[Square] (1) 0/0 - 10")
        self.assertEqual(s1.size, 5)
        s2.size = (10)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s3.width, 10)
        self.assertEqual(s3.height, 10)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s3.x, 0)
        self.assertEqual(s3.y, 0)
    
    def test_update(self):
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")
        s1 = Square(5)
        s1.update()
        self.assertEqual(s1.__str__(), "[Square] (2) 0/0 - 5")

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1)
        s2 = s1.to_dictionary()
        self.assertEqual(s2.__str__(), "{'id': 1, 'x': 2, 'size': 10, 'y': 1}")
        self.assertTrue(type(s2) is dict)
        self.assertEqual(s1.__str__(), "[Square] (1) 2/1 - 10")
        s3 = Square(1, 1)
        s3.update(**s2)
        self.assertEqual(s1.__str__(), "[Square] (1) 2/1 - 10")
        self.assertNotEqual(s1, s3)

    def test_update_excep(self):
        s = Square(5, 8, 1, 3)
        with self.assertRaises(ValueError):
            s.update(5, 3, -1)
            s.update(5, 0)
            s.update(2, 7, 9, -1)
            s.update(5, -1)
        with self.assertRaises(TypeError):
            s.update(5, 3, "hola")
            s.update(5, "como")
            s.update(5, 3, 9, "estas")

    def test_pep8_base(self):
        self.assertEqual(os.system('pep8 models/square.py'), 0)

    def test_module_docstring(self):
        self.assertTrue(len(Square.__doc__) >= 1)
        self.assertTrue(len(Square.__init__.__doc__) >= 1)
        self.assertTrue(len(Square.__str__.__doc__) >= 1)
        self.assertTrue(len(Square.update.__doc__) >= 1)
        self.assertTrue(len(Square.to_dictionary.__doc__) >= 1)

    def test_name_file(self):
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(hasattr(Square, "__str__"))
        self.assertTrue(hasattr(Square, "update"))
        self.assertTrue(hasattr(Square, "to_dictionary"))

if __name__ == '__main__':
    unittest.main()
