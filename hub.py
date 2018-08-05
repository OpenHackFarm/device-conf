import importlib
import json
import geohash
import os

root = os.path.dirname(__file__).split('/')[-1]
print(root)


DEV_ID = ''
RAW_DATA = ''

def process(DEV_ID, RAW_DATA):
    # --------

    NODE_FILE = root + '/nodes/' + DEV_ID + '.json'
    # print(NODE_FILE)

    f = open(NODE_FILE)
    NODE = json.load(f)
    # print(NODE)

    # --------

    PARSER = root + '.parser.' + NODE['node_conf']['parser']
    # print(PARSER)
    parser = importlib.import_module(PARSER)
    # print(dir(parser))

    PARSE_DATA = parser.parse(RAW_DATA)
    print(PARSE_DATA)
    print()

    # --------

    DEV_FILE = root + '/devices/' + NODE['node_conf']['device'] + '.json'
    # print(DEV_FILE)

    f = open(DEV_FILE)
    DEV_DATA = json.load(f)
    # print(DEV_DATA)

    # --------

    # for s in DEV_DATA['sensor_conf']:
        # print(s)

    # print(len(PARSE_DATA), len(DEV_DATA['sensor_conf']))

    node_data = {"device": {"id": DEV_ID, "latitude": None, "longitude": None, "geohash": None}, "sensors": {}}

    if NODE['node_conf']['ref_latitude'] and NODE['node_conf']['ref_longitude']:
        node_data['device']['latitude'] = NODE['node_conf']['ref_latitude']
        node_data['device']['longitude'] = NODE['node_conf']['ref_longitude']
        node_data['device']['geohash'] = geohash.encode(NODE['node_conf']['ref_latitude'], NODE['node_conf']['ref_longitude'])

    if len(PARSE_DATA) == len(DEV_DATA['sensor_conf']):
        for k, i in enumerate(PARSE_DATA):
            k = k + 1
            node_data['sensors']['field_%d' % k] = {}
            node_data['sensors']['field_%d' % k]['key'] = DEV_DATA['sensor_conf']['field_%d' % k]['field']
            node_data['sensors']['field_%d' % k]['value'] = eval(DEV_DATA['sensor_conf']['field_%d' % k]['type'])(i)

    print(node_data)
    print()

    # --------

    FORAWRD = root + '.forwarder.' + NODE['node_conf']['forwarder']
    forwarder = importlib.import_module(FORAWRD)

    ret = forwarder.forward(node_data)

if __name__ == "__main__":
    process(DEV_ID, RAW_DATA)
