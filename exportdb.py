import utils
import logging
import traceback


def export_all():
    """Exports all collections to DATA_PATH/export folder"""
    db = utils.get_db()
    collection_names = utils.get_collections(db)
    status = True
    failed_writes = []
    for cname in collection_names:
        try:
            collection = db[cname]
            data = collection.find()
            write_status = utils.write_json(cname, data)
            if write_status:
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
