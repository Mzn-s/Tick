def test_mysqld_installed(host):
    mysqld = host.package("mysql-community-server")
    assert mysqld.is_installed

def test_mysqld_running(host):
    mysqld = host.service("mysqld")
    assert mysqld.is_running
    
def test_mysqld_enabled(host):
    mysqld = host.service("mysqld")
    assert mysqld.is_enabled