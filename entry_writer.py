import pymongo
import conn
import json
import datetime
from pathlib import Path
import os


def write_entries_db(entries):
    """
    Writes an array of entries to the database.

    :param: entries
    :return: None
    """
    try:
        connection = conn.conn_str

        my_client = pymongo.MongoClient(connection, serverSelectionTimeoutMS=5000)
        my_db = my_client["algorithms"]
        my_col = my_db["checks"]

        print("Connection Successful: Appending entries to database.")
        my_col.insert_many(entries)

    except Exception:
        print("Connection Error: Unable to connect to the server. Creating local logs.")
        write_entries_local(entries)

    return


def write_entries_local(entries):
    """
    Creates a json file for local storage.

    :return:
    """
    file_path = f"offline_logs/{datetime.datetime.utcnow().isoformat().replace(':', '-')[0:18]}.json"

    Path(file_path).touch()

    for entry in entries:
        entry['date'] = datetime.datetime.isoformat(entry['date'])

    with open(file_path, "w") as file:
        json.dump(entries, file)

    file.close()
    print('Local log created.')

    return


def append_locals_to_db():
    """
    Appends offline logs to the database if: (1) offline logs exist and (2) a connection is made.

    :return:
    """
    offline_path = Path('offline_logs/')
    files = offline_path.iterdir()

    for file in files:

        with open(str(file)) as data:
            file_contents = json.load(data)

        data.close()

        # Converting timestamp strings to timestamp objects. This is required
        # because json doesn't store timestamp objects.
        for i in file_contents:
            i['date'] = datetime.datetime.fromisoformat(i['date'])

        write_entries_db(file_contents)
        os.remove(file)

