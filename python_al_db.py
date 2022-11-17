import mysql.connector

mydb = mysql.connector.connect(
host="istaircasedb.cbrmztnfdrpj.ap-south-1.rds.amazonaws.com",
user="admin",
password="admin123",
database="staircase"
)

mycursor = mydb.cursor()
x=input('Enter a integer value')
sql = f"INSERT INTO py_insert VALUES ({x})"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
mydb.close()