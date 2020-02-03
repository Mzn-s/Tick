from influxdb import InfluxDBClient

def test_telegrafdb_in_influxdb():
	r =False
	client = InfluxDBClient(host='10.100.3.100', port=8086)
	a = client.get_list_database()
	for x in range (3):
		a2 = "dict_values(['telegraf'])"
		if a2 == str(a[x].values()):
			r = True
	assert r