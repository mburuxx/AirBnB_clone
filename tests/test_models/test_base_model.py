#!/usr/bin/env python3
""" Module of unittests"""
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBase(unittest.TestCase):
    """Base Model test class. """
    my_model = BaseModel()

    def testBaseModel(self):
        """ Test the attributes of Base Model. """
        self.my_model.name = "My First Model"
        self.my_model.my_number = 21
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])

    def testSave(self):
        """Checks if the save method updates the public
        instance attribute 'updated_at'. """
        self.my_model.first_name = "First"
        self.my_model.save()

        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

        first_dict = self.my_model.to_dict()

        self.my_model.first_name = "Second"
        self.my_model.save()
        sec_dict = self.my_model.to_dict()

        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])


if __name__ == '__main__':
    unittest.main()
