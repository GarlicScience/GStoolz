import MySQLdb
from res.values import strings as _str


def connect():
    try:
        m = MySQLdb.connect(host="galact03.mysql.ukraine.com.ua", user="galact03_sample", passwd="nbnfhtyrj",
                    db="galact03_sample")
    except MySQLdb.MySQLError as err:
        return None, str(err)
    return m, _str.DB_CON_OK_MESSAGE







{
 "all_weight":  "15",
          "0":  {"id":"41","amount":"1","weight":"1","chance":"1"},
          "1":  {"id":"43","amount":"1","weight":"2","chance":"0.9"},
          "2":  {"id":"42","amount":"1","weight":"3","chance":"0.8"},
          "3":  {"id":"44","amount":"1","weight":"4","chance":"0.5"},
          "4":  {"id":"45","amount":"1","weight":"5","chance":"0.45"},
          "5":  {"id":"46","amount":"1","weight":"6","chance":"0.2"},
          "6":  {"id":"47","amount":"1","weight":"7","chance":"0.15"}
}