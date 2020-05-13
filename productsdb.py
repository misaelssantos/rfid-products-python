from dao import Connect
from logger import Logger

log = Logger(__name__)

class ProdutosDB(object):

    tb_name = 'pessoas'

    def __init__(self):
        self.db = Connect('db/compras.db')
        self.tb_name

    def fechar_conexao(self):
        self.db.close_db()

    def list(self):
        sql = 'SELECT tag, name, icon, value FROM products'
        r = self.db.cursor.execute(sql)
        return r.fetchall()

    def find_product(self, tag):
        r = self.db.cursor.execute(
            'SELECT tag, name, icon, value FROM products WHERE tag = ?', (tag,))
        return r.fetchone()

    def update_product(self, tag, value):
        try:
            p = self.find_product(tag)
            if p:
                self.db.cursor.execute("""
                    UPDATE products
                    SET value = ?
                    WHERE tag = ?
                """, (value, tag,))
                # gravando no bd
                self.db.commit_db()
                log.debug("Update ok!")
            else:
                log.warn('Não existe cliente com o id informado.')
        except e:
            raise e

    def listZeroStock(self):
        sql = 'SELECT tag, name, icon, value FROM products WHERE value = 0'
        r = self.db.cursor.execute(sql)
        return r.fetchall()        