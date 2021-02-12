import functions = require('firebase-functions')

import express = require('express')

import routes from './routes'

const app = express()

app.use(express.json())//plugin para poder usar o json

app.use(routes)

exports.api = functions.https.onRequest(app)
