from productsdb import ProdutosDB
from logger import Logger
import json

log = Logger(__name__)

class ProductList:

  def __init__(self):
    self.doc = {"products": []}
    self.db = ProdutosDB()

  def clear(self):
    self.doc = {"products": []}

  def add(self, tag, name=""):
    # avoid duplications
    for p in self.doc['products']:
      if p['tag'] == tag:
        return
    log.debug("Adding {0} to list.".format(tag))
    self.doc['products'].append({
      'tag' : tag, 
      'name': name
    })

  # updates the product's value indicator
  def update(self, tag, value):
    log.debug(f'Updating product "{tag}" to "{value}"...')
    self.db.update_product(tag, value)

  # lists products with zero value indicator
  def listZeroStock(self):
    prods = self.db.listZeroStock()
    self.clear()
    for p in prods:
      self.add(p[0], p[1])
    return self.doc

  def findByTag(self, tag):
    log.debug(f'Looking product "{tag}"...')
    r = self.db.find_product(tag)
    prod = {
      'tag' : r[0],
      'name': r[1],
      'icon': r[2],
      'value': r[3]
    }
    return prod
