def test_influxdb_installed(host):
    influxdb = host.package("influxdb")
    assert influxdb.is_installed

def test_influxdb_running(host):
    influxdb = host.service("influxdb")
    assert influxdb.is_running
    
def test_influxdb_enabled(host):
    influxdb = host.service("influxdb")
    assert influxdb.is_enabled