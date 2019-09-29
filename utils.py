#
# utils.py: Utility functions
#

import os
import logging
import traceback
from bson import json_util
import pymongo
from config import CONFIG


# File Processing

def get_json_filenames():
    """Returns list of file names with json extension from data/import folder"""
    filenames = os.listdir(CONFIG['DATA_PATH'] + "/import")
    json_filenames = []
    for f in filenames:
        fname, ext = f.split('.')
        if ext == 'json':
            json_filenames.append(f)
    return json_filenames


def read_json(fname):
    """Reads json file and returns data as python dictionary"""
    data = None
    with open(fname) as f:
        try:
            data = json_util.loads(f.read())
            res = data
        except:
            logging.error("read_json(): Failed to read file " + fname)
            traceback.print_exc()
    return data


def write_json(fname, data):
    """Writes data to DATA_PATH/export/fname.json"""
    path = CONFIG['DATA_PATH'] + "/export"
    filepath = path + "/fname" + ".json"
    status = False
    try:
        with open(filepath, 'w') as f:
            rawData = json_util.dumps(data)
            f.write(rawData)
        status = True
    except:
        logging.error("write_json(): Failed to write data to file " + filepath)
        traceback.print_exc()
    return status

# Database Utilities


def get_db():
    """Returns database object after connecting to mongo server"""
    db = None
    try:
        client = pymongo.MongoClient(CONFIG['MONGO_SERVER'])
        db = client[CONFIG['DB_NAME']]
    except:
        logging.error("get_db(): Failed to connect to database")
        logging.error("get_db(): Check MONG_SERVER and DB_NAME in config.py")
        traceback.print_exc()
    return db


def get_collections(db):
    """Returns list of collections present in database"""
    res = None
    if db:
        res = db.list_collection_names()
    return res


def collection_exists(collectionName, collections):
    """Checks if a collection exists in the database"""
    res = False
    if collections and collectionName:
        res = collectionName in collections
    return res
