import logging
import confuse
import os
from time import sleep
appname='testapp'
config = confuse.LazyConfig(appname)
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info('App started')


directory=config.config_dir()
con_file_dir=config.user_config_path()
logging.warn('Config file Directory: {0} | User Config File:{1}'.format(directory,con_file_dir))
logging.warn('Discoverd Keys {0}'.format(config.keys()))

while (True):
    config.clear()
    config.read()
    logging.warn('{0}: {1}'.format(config.keys()[0],config[config.keys()[0]]))
    sleep(1)