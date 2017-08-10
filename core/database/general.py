import MySQLdb
from res.values import strings as _str


def connect():
    try:
        m = MySQLdb.connect(host="galact03.mysql.ukraine.com.ua", user="galact03_sample", passwd="nbnfhtyrj",
                    db="galact03_sample")
    except MySQLdb.MySQLError as err:
        return None, str(err)
    return m, _str.DB_CON_OK_MESSAGE
