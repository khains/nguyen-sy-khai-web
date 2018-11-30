import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds139690.mlab.com:39690/movie
host = "ds139690.mlab.com"
port = 39690
db_name = "movie"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())