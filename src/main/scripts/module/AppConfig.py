from configparser import ConfigParser
import os

DEFAULT_CONFIG_FILE = 'src/main/resources/app.cfg'

class MyConfigParser_1(ConfigParser):
    def get_list(self,section,option):
        value = self.get(section,option)
        return list(filter(None, (x.strip() for x in value.split(','))))

def get_config_file():
    return os.environ.get('APP_CONFIG_FILE', DEFAULT_CONFIG_FILE)

CONFIG_FILE = get_config_file()

def get_config(config_file=None):
    print ("CONFIG : ", get_config_file())
    parser = MyConfigParser_1()
    parser.read(config_file or get_config_file())
    return parser
