
import mysql.connector
class DBConnection:
    @staticmethod
    def getConnection():
        database = mysql.connector.connect(host="localhost", user="root", passwd="root", db='medicalchatbot')
        return database


if __name__=="__main__":
    print(DBConnection.getConnection())