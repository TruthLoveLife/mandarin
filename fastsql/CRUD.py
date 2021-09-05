import pymysql


class DataModel:
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="1",
                               database="sign_up_db", charset="utf8",
                               cursorclass=pymysql.cursors.DictCursor
                               )
        self.cursor = self.conn.cursor()
#  删除和插入
    def test(self, sql_test):
        self.cursor.execute(sql_test)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


# 查询
    def test_query(self, sql_test):
        self.cursor.execute(sql_test)
        # self.conn.commit()
        result = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        return result

    def try1(self, sql_test, image):
        self.cursor.execute(sql_test, image)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

def new_student(*args):
    sql = "insert into person_infor(registration_number,name,sex," \
          "minzu,cartype,cart_number,cart_photo,job," \
          "phone,birthday,province,city,detail_addrees)" \
          " values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    insert = DataModel()
    insert.try1(sql, args)


