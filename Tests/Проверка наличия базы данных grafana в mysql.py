import pymysql.cursors

def test_reverse_proxy_nginx_influx():
    con = pymysql.connect(host='localhost',
                                user='grauser',
                                password='Vjlbabrfwbz0!')
    with con: 
        cur = con.cursor()
        cur.execute("SHOW DATABASES")
        rows = cur.fetchall()
        if ('grafana',) in rows:
            res = True
        assert res
