import MySQLdb
import sys
import os

curfile = os.path.abspath(__file__)
project_dir = os.path.dirname(curfile) + os.path.sep + '..' 
sys.path.append(project_dir)

# import app
import utils

db_config = utils.readJSONtoDict(os.path.join(project_dir, 'config', 'configuration.json'))
environment = 'development'
db_config = db_config[environment]['database']

def dbconnect():
    '''
    dbconnect function
    '''
    try:
        db = MySQLdb.connect(
            host=db_config['host'],
            port=db_config['port'],
            user=db_config['username'],
            passwd=db_config['password'],
            db=db_config['db']
        )
    except Exception as e:
        print e
        sys.exit("Can't connect to database")
    return db


