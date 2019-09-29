import logging
import os
import traceback
import utils
from config import CONFIG


def import_all():
    """Imports all data files from DATA_PATH/export to database. File name is taken as collection name."""
    db = utils.get_db()
    filenames = utils.get_json_filenames()
    status = True
    failed_writes = []
    for fname in filenames:
        cname = fname.split('.')[0]
        try:
            collection = db[cname]
            filepath = CONFIG['DATA_PATH'] + '/import/' + fname
            command = 'mongoimport --db {0} --collection {1} --type json --file {2}'.format(
                CONFIG['DB_NAME'], cname, filepath)
            os.system(command)
            if True:
                logging.info("Wrote", cname, "to", cname + ".json")
            else:
                failed_writes.append(cname)
        except:
            logging.error("export_all(): Export failed!")
            traceback.print_exc()
            status = False
    if len(failed_writes) > 0:
        print("Failed to write", failed_writes)
        status = False
    return status
