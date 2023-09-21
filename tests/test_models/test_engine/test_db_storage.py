#!/usr/bin/python3
"""import models"""

from models.engine.db_storage import DBStorage
import os
import unittest


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db",
    "Test is not for DBStorage"
)
class test_DB_Storage(unittest.TestCase):
    """test db storage"""

    def test_documentation(self):
        """test db storage"""
        self.assertIsNot(DBStorage.__doc__, None)