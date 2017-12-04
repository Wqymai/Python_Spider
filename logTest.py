import logging

logging.basicConfig(filename='logger.log',level=logging.DEBUG,format='%(funcName)s %(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug('debug...')
logging.info('info...')
logging.warn('warn...')
logging.error('error...')
logging.critical('critical...')
