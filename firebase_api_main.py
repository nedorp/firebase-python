import firebase_admin
from algo.algo_log import AlgoLoggerRow
from algo.base_algo import BuyOrderItem
from firebase_admin import credentials, firestore
from datetime import datetime
from decimal import Decimal

# Path to the Firebase private key JSON file
PRIVATE_KEY_JSON = "cryptocobra-51525-firebase-adminsdk-dhel8-05a054ec6b.json"

# Converts a string from Firebase into a Decimal object
def firebase_string_to_py_decimal(firebase_string):
    return Decimal(firebase_string)

# Converts a Decimal object to a string format suitable for Firebase, without losing precision
def py_decimal_to_firebase_string(py_decimal):
    return str(py_decimal)


# Initializes connection to Firebase Firestore and returns the database client
def connect_to_firebase_db():
    # Use the provided credentials to initialize the Firebase app
    cred = credentials.Certificate(PRIVATE_KEY_JSON)
    firebase_admin.initialize_app(cred)

    # Get a reference to the Firestore database
    db = firestore.client()
    return db

# Lists all collections and documents in the Firestore database
def list_collections(db_client):
    # Get a generator for all collections in the database
    collections_gen = db_client.collections()
    for coll in collections_gen:
        print(f"> CollectionID: {coll.id}")
        # Get a generator for all documents in the collection
        docs_gen = coll.stream()
        # docs = list()
        for doc in docs_gen:
            # Print each document ID and its content
            print(f"Document ID='{doc.id}': {doc.to_dict()}")


# Retrieves a specific document from a collection in Firestore
def get_document(db_client, collection_name, document_id):
    coll_ref = db_client.collection(collection_name)
    return coll_ref.document(document_id)


# Adds a document to a collection in Firestore, optionally with a specific document ID
def add_document(db_client, collection_name, python_dict_data, document_id=None):

    # Collection if not present will be created

    # If a document ID is provided, set the document with that ID
    if document_id is not None:
        db_client.collection(collection_name).document(document_id).set(python_dict_data)
    else:
        # Otherwise, let Firestore generate an ID for the new document
        db_client.collection(collection_name).document().set(python_dict_data)

# Converts a Firebase document to an AlgoLoggerRow object
def firebase_doc_to_algologrow(fake_doc):
    algologrow = AlgoLoggerRow()
    dict_doc = fake_doc.get().to_dict()

    # Map document fields to AlgoLoggerRow fields
    algologrow.tick = dict_doc["tick"]
    algologrow.reason = dict_doc["reason"]
    algologrow.amount_usd = dict_doc["amount_usd"]
    algologrow.timestamp = dict_doc["timestamp"]
    algologrow.wallet_btc_in_usd = dict_doc["wallet_btc_in_usd"]
    algologrow.wallet_usd = dict_doc["wallet_usd"]
    algologrow.action_code = dict_doc["action_code"]
    algologrow.stationary_percent_change = dict_doc["stationary_percent_change"]

    # Convert active orders to a list of BuyOrderItem objects
    active_orders = dict_doc["active_orders"]
    algologrow.deserialized_active_orders = [BuyOrderItem(dct["buyPrice"], dct["btcAmount"], dct["timestamp"]) for dct in active_orders]
    return algologrow


if __name__ == '__main__':

    # Connect to Firestore database
    db_client = connect_to_firebase_db()

    # List all collections and their documents
    list_collections(db_client)

    # Retrieve and print a specific document
    doc = get_document(db_client, "btc_usdt_orders", "EVSJIsSuDcr2ap9uEAlq")
    print(doc.get().to_dict())

    # Create and save an AlgoLoggerRow object
    obj = AlgoLoggerRow()
    obj.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current timestamp
    obj.trading_pair = "BTC/USDT"
    obj.stationary_percent_change = 0.05
    obj.tick = "99999.5"
    obj.action_code = "BUY"
    obj.amount_usd = 1000.00
    obj.reason = "Signal from trading algorithm"
    obj.active_orders = [{
        "buyPrice": 56000,
        "btcAmount": py_decimal_to_firebase_string(0.0000184645732921654973375),
        "timestamp": str(datetime.now())
    }]
    obj.wallet_usd = 50.0
    obj.wallet_btc_in_usd = 50.0

    # Add the document to the Firestore collection
    add_document(db_client, "cities", obj.__dict__, "WITHTIMESTAMP")

    # Retrieve and convert the document back to an AlgoLoggerRow object
    fake_doc = get_document(db_client, "cities", "WITHTIMESTAMP")
    algologrow_from_doc = firebase_doc_to_algologrow(fake_doc)

    # Print the contents of the AlgoLoggerRow object
    print("Read OBJ")
    print(algologrow_from_doc.__dict__)
