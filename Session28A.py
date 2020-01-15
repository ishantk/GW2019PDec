import firebase_admin
from firebase_admin import credentials

from firebase_admin import firestore

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred)



db = firestore.client()

# Read Data from Firebase
# doc = db.collection("customers").document("fionna@example.com").get()
# print(doc)
# print(doc.__dict__)
#
# customerData = doc.to_dict()
# print(customerData)


# Store Complex Data
data = {
        'phone': '99999-76543',
        'cid': 2, 'name': 'Fionna Watson',
        'email': 'fionna@example.com',
        'address': [
                    {'adrsLine':'Redwood Shores', 'pinCode':141001},
                    {'adrsLine':'Pristine Magnum', 'pinCode':141004}
                   ]
        }

# Save Data
db.collection("mycustomers").document("fionna@example.com").set(data)
print(">> Data Saved in Firebase Firestore")

# Delete Data
# db.collection("mycustomers").document("fionna@example.com").delete()
# print(">> Document Deleted")

