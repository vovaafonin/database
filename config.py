from configparser import ConfigParser
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def config(filename=ROOT_DIR + "database" + "database.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename, encoding='windows-1251')
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db
