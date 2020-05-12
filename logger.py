import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', 
    datefmt='%d-%b-%y %H:%M:%S', 
    level=logging.DEBUG)

class Logger:

    def __init__(self, name='compras'):
        self.logger = logging.getLogger(name)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)