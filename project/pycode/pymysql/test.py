import pymysql
from pymysql import MySQLError

def create_connection():
    try:
        db = pymysql.connect(host='10.6.0.103',
                             user='root',
                             password='123456',
                             database='web_server')
        return db
    except MySQLError as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None

def create_table(db):
    try:
        with db.cursor() as cursor:
            sql = """
            CREATE TABLE IF NOT EXISTS stu(
                sid CHAR(6),
                sname VARCHAR(20),
                age INT,
                gender VARCHAR(10)
            );
            """
            cursor.execute(sql)
            db.commit()  # 提交事务
            print("Table created successfully")
    except MySQLError as e:
        print(f"Error creating table: {e}")

def main():
    db = create_connection()
    if db:
        create_table(db)
        db.close()

if __name__ == "__main__":
    main()
