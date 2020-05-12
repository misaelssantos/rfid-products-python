from productsdb import ProdutosDB
from logger import Logger
import json

log = Logger(__name__)

class ProductList:

  def __init__(self):
    self.doc = {"products": []}
    self.db = ProdutosDB()
    
  def add(self, product):
    log.debug("Adding {0} to list.".format(product))
    self.doc['products'].append(product)

  def rem(self, product):
    log.debug(f'Removing {product} from list.')
    self.doc['products'].pop(self.doc['products'].index(product))

  # updates the product's value indicator
  def update(self, tag, value):
    log.debug(f'Updating product "{tag}" to "{value}"...')
    self.db.update_product(tag, value)

  # lists products with zero value indicator
  def listZeroStock(self):
    prods = self.db.listZeroStock()
    for p in prods:
      self.add(p[0])
    return self.doc