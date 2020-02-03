def test_nginx_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_nginx_running(host):
    nginx = host.service("nginx")
    assert nginx.is_running

def test_nginx_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_enabled
