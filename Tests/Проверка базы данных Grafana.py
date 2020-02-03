def test_1_graphan_sql_settings():
    read = open('/etc/grafana/grafana.ini', 'r')
    typ = "type = mysql"
    if typ in read.read():
        res = True
    assert res == True