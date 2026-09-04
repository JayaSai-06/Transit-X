import firebase_admin
from firebase_admin import credentials, db

# Load service account key
cred = credentials.Certificate("serviceAccountKey.json")

# Initialize Firebase app with your DB URL
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://punjab-transport-541fb-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

# Quick test: write some data
ref = db.reference("test")
ref.set({"msg": "Hello Punjab!"})
