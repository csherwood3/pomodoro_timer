import pymongo
import conn


def write_entries_db(entries):
    """
    Writes an array of entries to the database.

    :param: entries
    :return: None
    """
    connection = conn.conn_str

    my_client = pymongo.MongoClient(connection, serverSelectionTimeoutMS=5000)
    my_db = my_client["algorithms"]
    my_col = my_db["checks"]

    try:
        for i in entries:
            my_col.insert_one(i)

    except Exception:
        print("Unable to connect to the server.")
