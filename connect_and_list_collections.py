import firebase_admin
from firebase_admin import credentials, firestore


PRIVATE_KEY_JSON = "cryptocobra-51525-firebase-adminsdk-dhel8-05a054ec6b.json"


def connect_and_list_first_document_of_each_collection():

    cred = credentials.Certificate(PRIVATE_KEY_JSON)
    firebase_admin.initialize_app(cred)

    # Get a reference to the Firestore database
    db = firestore.client()
    collections_gen = db.collections()
    for coll in collections_gen:
        print(f"> CollectionID: {coll.id}")
        docs_gen = coll.stream()
        # docs = list()
        for doc in docs_gen:
            print(f"Document ID='{doc.id}': {doc.to_dict()}")

if __name__ == '__main__':
    connect_and_list_first_document_of_each_collection()
