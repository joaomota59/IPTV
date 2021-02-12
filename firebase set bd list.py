import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore,storage
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "credenciais.json" #informar o diretório das credenciais(arquivo em .json que baixa no firebase)

f = open("listaNova.txt","r")#coloca a lista m3u(tranformar em txt antes) que deseja enviar para cloud
k=""
for line in f:
    k+=line
        

# Add a new document
db = firestore.Client()
doc_ref = db.collection(u'lista').document(u'bYknxRFAaMXKDWBzBrL4')#coloca a lista no bd Cloud Firestore
doc_ref.set({
    u'conteudo': k,
})

# Then query for documents
users_ref = db.collection(u'lista')
