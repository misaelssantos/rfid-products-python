from sanic import Sanic
from sanic.log import logger
from sanic.response import json
from sanic_cors import CORS, cross_origin
from products import ProductList

prods = ProductList()

app = Sanic("compras")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
async def hello(request):
  return json({"what": "API compras"})

@app.route("/api/lista", methods=['GET', 'OPTIONS'])
async def lista(request):
  logger.info('Consulta a lista de produtos...')
  lista = prods.listZeroStock()
  return json(lista)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)