import urllib.request

def test_reverse_proxy_nginx_grafana():
    f = urllib.request.urlopen('http://127.0.0.1/grafana')
    if f:
    	res = True
    assert res