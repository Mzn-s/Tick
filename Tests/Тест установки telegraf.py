import testinfra
def test_telegraf_installed(host):
    telegraf = host.package("telegraf")
    assert telegraf.is_installed

def test_telegraf_running(host):
    telegraf = host.service("telegraf")
    assert telegraf.is_running

def test_telegraf_enabled(host):
    telegraf = host.service("telegraf")
    assert telegraf.is_enabled