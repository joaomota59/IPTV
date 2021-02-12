//inicializa o firestore (database do firebase)

const admin = require('firebase-admin');//inicializa o banco de dados

const functions = require('firebase-functions');//gera o link das rotas que iremos colocar no isomnia 

admin.initializeApp(functions.config().firebase);//inicia as configurações de funções do firebase 

const database = admin.firestore();

module.exports = database