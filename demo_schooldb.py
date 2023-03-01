import datetime
import mysql.connector
from connection_Mysql import connection


class Student:
    connection = connection
    my_cursor = connection.cursor()

    def __init__(self,id,name,surname,birthdate,gender):
        self.id = id
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def savestudent(self):
        sql = "INSERT INTO students(id,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.id, self.name, self.surname, self.birthdate, self.gender)
        Student.my_cursor.execute(sql, value)

        try:
            Student.connection.commit()       #cursor dan hemen sonra olması lazım yoksa atılmaz db ye
            print(f'{Student.my_cursor.rowcount} tane kayıt eklendi.')
            print(f'son eklenen kaydın id: {Student.my_cursor.lastrowid} ')
        except mysql.connector.Error as err:
            print('Hata :', err)
        finally:
            Student.connection.close()
            print('Bağlantı sonlandırıldı.')

    @staticmethod
    def savestudents(students):
        sql = "INSERT INTO students(id,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.my_cursor.executemany(sql, values)

        try:
            Student.connection.commit()  # cursor dan hemen sonra olması lazım yoksa atılmaz db ye
            print(f'{Student.my_cursor.rowcount} tane kayıt eklendi.')
            print(f'son eklenen kaydın id: {Student.my_cursor.lastrowid} ')
        except mysql.connector.Error as err:
            print('Hata :', err)
        finally:
            Student.connection.close()
            print('Bağlantı sonlandırıldı.')




ogrenciler = [
    ("301", "Ahmet","Yılmaz",datetime.datetime(2005,5,17),"E"),
    ("302", "Ali", "Can", datetime.datetime(2005, 6, 17), "E"),
    ("303", "Canan", "Tan", datetime.datetime(2005, 7, 7), "K"),
    ("304", "Ayşe", "Taner", datetime.datetime(2005, 9, 23), "K"),
    ("305", "Bahadır", "Toksöz", datetime.datetime(2004, 7, 27), "E"),
    ("306", "Ali", "Cenk", datetime.datetime(2003, 8, 25), "E")

]

Student.savestudents(ogrenciler)


#ahmet = Student("202","ahmet","yılmaz",datetime.datetime(2005,5,17),"E")
#ahmet.savestudent()

