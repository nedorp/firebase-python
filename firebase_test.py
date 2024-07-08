import unittest
from decimal import Decimal

from firebase_api_main import add_document, get_document, firebase_string_to_py_decimal, \
    py_decimal_to_firebase_string, connect_to_firebase_db


class TestFirestoreOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # Initialize Firebase for testing purposes
        cls.db_client = connect_to_firebase_db()

    def test_add_and_get_document(self):
        # Define test data
        collection_name = "test_collection"
        document_id = "test_document"
        test_data = {
            "field1": "value1",
            "field2": 42,
            "field3": py_decimal_to_firebase_string(Decimal('123.7567363846283658637'))
        }

        # Add document to Firestore
        add_document(self.db_client, collection_name, test_data, document_id)

        # Retrieve the document from Firestore
        doc_ref = get_document(self.db_client, collection_name, document_id)
        retrieved_data = doc_ref.get().to_dict()

        # Convert retrieved decimal string back to Decimal for comparison
        retrieved_data["field3"] = firebase_string_to_py_decimal(retrieved_data["field3"])

        # Assert that the retrieved data matches the original data
        self.assertEqual(retrieved_data["field1"], test_data["field1"])
        self.assertEqual(retrieved_data["field2"], test_data["field2"])
        self.assertEqual(retrieved_data["field3"], Decimal(test_data["field3"]))


if __name__ == '__main__':
    unittest.main()
