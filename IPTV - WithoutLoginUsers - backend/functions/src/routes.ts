import express = require('express');//importante para usar nas rotas

const routes = express.Router()

const listController = require('./controllers/listController')

routes.get('/listaaovivo',listController.index)

export default routes