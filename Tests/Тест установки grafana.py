def test_grafana_installed(host):
    grafana = host.package("grafana")
    assert grafana.is_installed

def test_grafana_running(host):
    grafana = host.service("grafana-server")
    assert grafana.is_running
   
def test_grafana_enabled(host):
    grafana = host.service("grafana-server")
    assert grafana.is_enabled