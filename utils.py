from pymongo import MongoClient


def get_db_handle():

    client = MongoClient(host="192.168.29.96",
                         port=int(27017),
                         username='admin',
                         password='letsgo!'
                         )
    db_handle = client['projectop']
    return db_handle, client


# hlnhyyjswaxgpxmd
