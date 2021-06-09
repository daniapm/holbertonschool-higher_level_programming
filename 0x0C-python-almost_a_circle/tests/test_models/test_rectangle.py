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


"""
class test of the base
"""


class TestRectangle(unittest.TestCase):
    """Tests the Square class"""
    def setUp(self):
        """
        Reset the nb_objects
        """
        Base._Base__nb_objects = 0

    def tests_increment_id_Rectangule(self):
        """
        Test check the id
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

    def tests_exepc(self):
        """
        Test check error
        """
        with self.assertRaises(TypeError):
            r3 = Rectangle(9.2, 2.8)
            r4 = Rectangle(None)
            r5 = Rectangle(-5, 9)
            r6 = Rectangle(9, -5)
            r7 = Rectangle()
            r8 = Rectangle("hola")
            r9 = Rectangle(10, "2")
            r10 = Rectangle(10, 2, 3, -1)
            r11 = Rectangle(10, 2, "3", 1)

    def tests_area(self):
        """
        Test check the area
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        print(r3.area(), 56)
        r4 = Rectangle(33, 22)
        self.assertEqual(r4.area(), 726)
        r5 = Rectangle(222, 100)
        self.assertEqual(r5.area(), 22200)
        with self.assertRaises(TypeError):
            r6 = Rectangle()
            self.r.area(1)

    def test_display(self):
        """
        Test display Rectangle
        """
        r1 = Rectangle(4, 6)
        r2 = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r1.display()
        self.assertEqual(fakeOutput.getvalue(), '####\n####\n####\n####\n####\n####\n')
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r2.display()
        self.assertEqual(fakeOutput.getvalue(),
                             '##\n##\n')
    
    def test_display_x_and_y(self):
        """
        Test display Rectangle
        """
        r1 = Rectangle(2, 3, 2, 2)
        r2 = Rectangle(3, 2, 1, 0)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r1.display()
        self.assertEqual(fakeOutput.getvalue(), '\n\n  ##\n  ##\n  ##\n')
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r2.display()
        self.assertEqual(fakeOutput.getvalue(),
                             ' ###\n ###\n')

    def test_str(self):
        """
        Test representacion string Rectangle
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), '[Rectangle] (1) 1/0 - 5/5')
        r3 = Rectangle(5, 3, id="hola")
        self.assertEqual(r3.__str__(), '[Rectangle] (hola) 0/0 - 5/3')

    def tests_update(self):
        """
        Test updare rectangle
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 10/10 - 10/10')
        r1.update(None)
        self.assertEqual(r1.__str__(), '[Rectangle] (None) 10/10 - 10/10')
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 2/10')
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 2/3')
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 4/10 - 2/3')
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 4/5 - 2/3')
        r1.update(-6)
        self.assertEqual(r1.__str__(), '[Rectangle] (-6) 4/5 - 2/3')
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), '[Rectangle] (-6) 1/3 - 4/2')
        r1.update(*[10, 9, 1, 4, 3])
        self.assertEqual(r1.__str__(), "[Rectangle] (10) 4/3 - 9/1")
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (10) 4/3 - 9/1")
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (10) 2/3 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")


    def test_update_excep(self):
        """
        Test display Rectangle error
        """
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r1.update(width="10")
            r1.update(height="20")
            r1.update(x="30")
            r1.update(y="40")
            r1.update(width=-5)
            r1.update(height=-3)
            r1.update(x=-4)
            r1.update(y=-3)
            r1.update(width=0)
            r1.update(height=0)

    def tests_update_value_error(self):
        """
        Test display Rectangle error
        """
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r1.update(**{'id': 1337, 'x': -1})
            r1.update("stringid", None, None)

    def tests_to_dictionary(self):
        """
        Test dictionary
        """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertIs(type(r1.to_dictionary()), dict)
        self.assertDictEqual(r1.to_dictionary(), r1_dictionary)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/9 - 10/2")

    def test_pep8_base(self):
        """
        Test check pep8 style
        """
        self.assertEqual(os.system('pep8 models/rectangle.py'), 0)

    def test_module_docstring(self):
        """
        Test check the documentation
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__init__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.area.__doc__) >= 1)
        self.assertTrue(len(Rectangle.display.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__str__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.update.__doc__) >= 1)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) >= 1)

    def test_name_file(self):
        """
        Test check the name file
        """
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(hasattr(Rectangle, "area"))
        self.assertTrue(hasattr(Rectangle, "display"))
        self.assertTrue(hasattr(Rectangle, "__str__"))
        self.assertTrue(hasattr(Rectangle, "update"))
        self.assertTrue(hasattr(Rectangle, "to_dictionary"))
   

if __name__ == '__main__':
    unittest.main()
