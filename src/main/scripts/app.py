import os,sys
import logging
import logging.config
import simplejson as json
from flask import Flask

from module.AppConfig import get_config



cgi_folder = "."
config_folder = os.path.join(cgi_folder,"src/main/resources")
config_file=os.path.join(config_folder,"app.cfg")

logging_file = os.path.join(config_folder,"logging.conf")


os.environ["APP_CONFIG_FILE"] = config_file

port=get_config().get("server","port")
app = Flask(__name__)
 
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name
 
if __name__ == '__main__':
   app.run(port=port)
