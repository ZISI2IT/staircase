import mysql.connector
# print("test1")
def establish_connection():

    config = {
        'user': 'admin',
        'password': 'admin123',
        'host': 'istaircasedb.cbrmztnfdrpj.ap-south-1.rds.amazonaws.com',
        'port': '3306',
        'database': 'staircase'
    }
    return config
    

cursor = establish_connection()
cursor()

'''
    cnx: str = mysql.connector.connect(**config)
    print("test")
    print(cnx)
    return cnx
'''