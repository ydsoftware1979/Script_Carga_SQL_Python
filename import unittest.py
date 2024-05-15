import unittest
import pyodbc
from faker import Faker
import random

# Your code here...

class TestInsertFakeData(unittest.TestCase):
    def setUp(self):
        # Set up a test database connection
        self.connection_string = 'DRIVER=SQL Server;SERVER=test_server;DATABASE=test_database;UID=test_user;PWD=test_password'
        self.conn = pyodbc.connect(self.connection_string)
        self.cursor = self.conn.cursor()

    def tearDown(self):
        # Clean up the test database
        self.cursor.execute("DELETE FROM fornecedor")
        self.conn.commit()
        self.conn.close()

    def test_insert_fake_data(self):
        # Call the function to insert fake data
        insert_fake_data(self.conn, 10)

        # Check if the records were inserted correctly
        self.cursor.execute("SELECT COUNT(*) FROM fornecedor")
        num_records = self.cursor.fetchone()[0]
        self.assertEqual(num_records, 10)

if __name__ == '__main__':
    unittest.main()