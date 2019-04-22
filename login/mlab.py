import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds113845.mlab.com:13845/c4e25

host = "ds113845.mlab.com"
port = 13845
db_name = "c4e25"
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