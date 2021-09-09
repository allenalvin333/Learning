import os
import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Loading variables from .env
from dotenv import load_dotenv
load_dotenv()
p1=os.getenv('private_key_id')
p2=os.getenv('private_key')
p3=os.getenv('client_id')
u1=os.getenv('client_x509_cert_url')
u2=os.getenv('databaseURL')

# Creating credentials certificate for Authorization
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "learning-290101",
    "private_key_id": p1,
    "private_key": p2,
    "client_email": "firebase-adminsdk-x0tar@learning-290101.iam.gserviceaccount.com",
    "client_id": p3,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": u1
})

# Initializing the app with the certificate and access URL
firebase_admin.initialize_app(cred, {'databaseURL': u2})

# CRUD Operations on DB         --> Create, Read, Update, Delete

# Create                        --> .set()
r = db.reference('')
users = r.child('users')
users.set({
    'Allen': {
        'date_of_birth': 'September 26, 2000',
        'full_name': 'Allen Ben Philipose'
    },
    'Christi': {
        'date_of_birth': 'January 29, 2001',
        'full_name': 'Christiana John'
    },
    'Alvin': {
        'date_of_birth': 'January 16, 2004',
        'full_name': 'Alvin Ben George',
        'nick_name': 'Avin Boo'
    }
})

# Read                          --> .get()
read = r.child('users').child('Christi')
print(read.get())

# Update                        --> .update()
update = r.child('users').child('Christi')
update.update({'nick_name': 'Kishti Mol'})
update = r.child('users').child('Alvin')
update.update({'nick_name': 'Alvin Boo'})

# Delete                        --> .delete()
delete = r.child('users').child('Allen')
delete.delete()

# https://www.youtube.com/watch?v=s-Ga8c3toVY
# https://www.youtube.com/watch?v=LaGYxQWYmmc