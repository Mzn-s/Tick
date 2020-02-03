def test_nginx_port(host):
    sock = host.socket("tcp://80")
    assert sock.is_listening  

def test_grafana_port(host):
    sock = host.socket("tcp://3000")
    assert sock.is_listening

def test_influx_port(host):
    sock = host.socket("tcp://8086")
    assert sock.is_listening

