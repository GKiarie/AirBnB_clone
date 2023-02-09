#!/usr/bin/python3
"""
Test Suite for Base Model
"""
import unittest
import uuid
from datetime import datetime
from time import sleep
import models
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test Class for base Model
    """
    def test_new_instance(self):
        """
        Test that new instance is an instance of BaseModel()
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, type(BaseModel()))
        
    def test_instance_uniqueness(self):
        """
        Test that two instances are not equal
        """
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1, my_model2)

    def test_uuid(self):
        """
        Test uuid:
        Test 1: Is UUID an instance of str
        Test 2: Test UUID Version
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertEqual(uuid.UUID(my_model.id).version, 4)

    def test_created_at(self):
        """
        Test created at:
        Test1: Test that created_at is an instance of datetime
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_updated_at(self):
        """
        Test updated at:
        Test 1: Test updated at type
        """
        self.assertEqual(type(BaseModel().updated_at), datetime)

    def test_models_created_at_different_times(self):
        """
        Test that two models created at different times will have different
        created_at times with the first created_at time being less that the second
        """
        my_model1 = BaseModel()
        sleep(0.02)
        my_model2 = BaseModel()
        self.assertLess(my_model1.created_at, my_model2.created_at)

    def test_models_updated_at_different_times(self):
        """
        Test that two models updated at different times will have different
        updated_at times with the first updated_at time being less that the second
        """
        my_model1 = BaseModel()
        sleep(0.02)
        my_model2 = BaseModel()
        self.assertLess(my_model1.updated_at, my_model2.updated_at)

    def test_str_format(self):
        """
        Test the str method return format
        """
        my_model = BaseModel()
        expected_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_str)

    def test_save(self):
        """
        Test that the save method updates 'updated_at' attribute
        """
        my_model = BaseModel()
        my_model.save()
        self.assertLess(my_model.created_at, my_model.updated_at)

    def test_to_dict_contents(self):
        """
        Test that all expected keys are contained in dict created on runninge to_dict()
        """
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        self.assertIn("id", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)
        self.assertIn("__class__", my_dict)

    def test_to_dict_update(self):
        """
        Testing that dict captures updated information corresctly
        """
        my_model = BaseModel()
        my_model.name = "new name"
        my_dict = my_model.to_dict()
        self.assertEqual(my_dict["name"], "new name")

        

if __name__ == "__main__":
    unittest.main()
