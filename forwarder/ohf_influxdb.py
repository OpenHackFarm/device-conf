from influxdb import InfluxDBClient

INFLUXDB_HOST = ''
INFLUXDB_DATABASE = ''
INFLUXDB_MEASUREMENT = ''

inClient = InfluxDBClient(host=INFLUXDB_HOST, database=INFLUXDB_DATABASE)


def forward(data_in):
    try:
        tags = {
            'id': data_in['device']['id'],
            'latitude': data_in['device']['latitude'] if data_in['device']['latitude'] else None,
            'longitude': data_in['device']['longitude'] if data_in['device']['longitude'] else None,
            'geohash': data_in['device']['geohash'] if data_in['device']['geohash'] else None
        }

        fields = {}
        for k, v in data_in['sensors'].items():
            fields[v['key']] = v['value']

        _ = {
            "measurement": INFLUXDB_MEASUREMENT,
            "tags": tags,
            "fields": fields
        }

        data_output = []
        data_output.append(_)

        # print(data_output)

        inClient.write_points(data_output)

        return {'status': 'success'}
    except:

        return {'status': 'error'}
