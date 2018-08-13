import importlib
import json
import geohash
import os
import sys

DEV_ID = ''
RAW_DATA = ''

root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, root)


def get_node_info(dev_id):
    node_file = os.path.join(root, 'nodes', dev_id + '.json')
    print(node_file)

    f = open(node_file)
    node = json.load(f)

    return node


def load_data_parser(parser_module_name):
    parser_path = 'plugin.parser.' + parser_module_name

    parser = importlib.import_module(parser_path)

    return parser


def load_device_define(dev):
    dev_file = os.path.join(root, 'devices', dev + '.json')
    print(dev_file)

    f = open(dev_file)
    dev = json.load(f)

    return dev

def mapping_node_data(dev, node, dev_id, data):
    node_structure = {"device": {"id": dev_id, "latitude": None, "longitude": None, "geohash": None}, "sensors": {}}

    if node['node_conf']['ref_latitude'] and node['node_conf']['ref_longitude']:
        node_structure['device']['latitude'] = node['node_conf']['ref_latitude']
        node_structure['device']['longitude'] = node['node_conf']['ref_longitude']
        node_structure['device']['geohash'] = geohash.encode(node['node_conf']['ref_latitude'], node['node_conf']['ref_longitude'])

    # print(len(PARSE_DATA), len(DEV_DATA['sensor_conf']))
    if len(data) == len(dev['sensor_conf']):
        for k, i in enumerate(data):
            k = k + 1
            node_structure['sensors']['field_%d' % k] = {}
            node_structure['sensors']['field_%d' % k]['key'] = dev['sensor_conf']['field_%d' % k]['field']
            node_structure['sensors']['field_%d' % k]['value'] = eval(dev['sensor_conf']['field_%d' % k]['type'])(i)

    return node_structure


def load_data_forwarder(forwarder_module_name):
    forwarder_path = 'plugin.forwarder.' + forwarder_module_name

    forwarder = importlib.import_module(forwarder_path)

    return forwarder


def process(dev_id, raw_data):
    node = get_node_info(dev_id)

    dev = load_device_define(node['node_conf']['device'])
    print(dev)
    print()

    if node['node_conf']['parser']:
        parser = load_data_parser(node['node_conf']['parser'])

        parse_data = parser.parse(raw_data)
    else:
        parse_data = raw_data
    print(parse_data)
    print()

    node_data = mapping_node_data(dev, node, dev_id, parse_data)
    print(json.dumps(node_data, indent=4, sort_keys=True))
    print()

    if node['node_conf']['forwarder']:
        forwarder = load_data_forwarder(node['node_conf']['forwarder'])
        ret = forwarder.forward(node_data)

if __name__ == "__main__":
    process(DEV_ID, RAW_DATA)
