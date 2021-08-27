# coding = GBK
import pymysql


class DataBase:
    def __init__(self, website):
        self.obj = pymysql.connect(
            host='db-test-master.55haitao.com',
            user='haitao_php',
            password='haitao_php1234',
            database=website
        )
        self.cursor = self.obj.cursor()

    def select(self, sentence):
        try:
            self.cursor.execute(sentence)
            result = self.cursor.fetchall()
            self.obj.commit()
            return result
        except IndexError:
            return {'message': ' select IndexError '}
        except pymysql.err.OperationalError:
            return {'message': 'You have an error in your SQL syntax'}
