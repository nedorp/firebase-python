# Firebase Python Utility (firebase-python)
Basic Operations with Firebase Database (2024)

This repository provides a set of utility functions to interact with Google Firestore using Python. It includes functions for connecting to Firestore, listing collections and documents, adding and retrieving documents, and converting data between Python and Firestore formats.

## Prerequisites

- Python 3.8+
- Google Cloud account with Firestore enabled
- Firebase Admin SDK JSON private key file

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/firebase-python.git
    cd firebase-python
    ```

2. **Install dependencies:**

    Create and activate a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

    Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

3. **Set up Firebase Admin SDK:**

    - Place your Firebase Admin SDK JSON file (`your-firebase-project-51525-firebase-adminsdk-xyz-xyz.json`) in the project directory.
    - Ensure the `PRIVATE_KEY_JSON` variable in the script points to this file.

## Usage

### 1. Initialize Firestore Connection

Use the `connect_to_firebase_db` function to initialize a connection to Firestore:

```python
from your_module import connect_to_firebase_db

db_client = connect_to_firebase_db()
```

# Firestore Python Utility

This repository provides a set of utility functions to interact with Google Firestore using Python. It includes functions for connecting to Firestore, listing collections and documents, adding and retrieving documents, and converting data between Python and Firestore formats.

## Prerequisites

- Python 3.8+
- Google Cloud account with Firestore enabled
- Firebase Admin SDK JSON private key file

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/firestore-python-utility.git
    cd firestore-python-utility
    ```

2. **Install dependencies:**

    Create and activate a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

    Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

3. **Set up Firebase Admin SDK:**

    - Place your Firebase Admin SDK JSON file (`cryptocobra-51525-firebase-adminsdk-dhel8-05a054ec6b.json`) in the project directory.
    - Ensure the `PRIVATE_KEY_JSON` variable in the script points to this file.

## Usage

### 1. Initialize Firestore Connection

Use the `connect_to_firebase_db` function to initialize a connection to Firestore:

```python
from your_module import connect_to_firebase_db

db_client = connect_to_firebase_db()
```

### 2. List Collections and Documents

Use the `list_collections` function to print all collections and their documents:

```python
from your_module import list_collections

list_collections(db_client)
```

### 3. Add a Document to Firestore

Use the `add_document` function to add a document to a specified collection:

```python
from your_module import add_document

collection_name = "your_collection"
document_id = "your_document_id"
data = {
    "field1": "value1",
    "field2": 42,
    "field3": py_decimal_to_firebase_string(Decimal('123.45'))
}

add_document(db_client, collection_name, data, document_id)
```

### 4. Retrieve a Document from Firestore

Use the `get_document` function to retrieve a document by its ID:

```python
from your_module import get_document

collection_name = "your_collection"
document_id = "your_document_id"

doc_ref = get_document(db_client, collection_name, document_id)
doc_data = doc_ref.get().to_dict()
print(doc_data)
```

### 5. Convert Between Python Decimal and Firestore String

Use `firebase_string_to_py_decimal` and `py_decimal_to_firebase_string` to convert data types:

```python
from your_module import firebase_string_to_py_decimal, py_decimal_to_firebase_string
from decimal import Decimal

# Convert Firestore string to Python Decimal
decimal_value = firebase_string_to_py_decimal("123.45")

# Convert Python Decimal to Firestore string
firebase_string = py_decimal_to_firebase_string(Decimal('123.45'))
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
