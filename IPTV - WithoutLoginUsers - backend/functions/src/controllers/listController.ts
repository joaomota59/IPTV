import {Request,Response} from 'express'

import * as admin from 'firebase-admin';



const db = require('../database/db')//importa o banco de dados

module.exports = {
    async index(request : Request , response : Response){
        const docRef = db.collection('lista');
        let todos: any[] = [];

        await docRef.get()
        .then((snapshot : admin.firestore.QuerySnapshot)=>{
            snapshot.forEach(doc=>{
                todos.push(doc.data().conteudo)//pega lista m3u que está no bd do firebase
            })
        }).then(()=>{
            //response.writeHead(200, {'Content-Type': 'application/force-download','Content-disposition':'attachment; filename=listaCanais.m3u'});
            response.end(todos[0]); // Envia lista m3u
            


        }).catch(()=>{
            response.status(404).send()
        })
    }
}