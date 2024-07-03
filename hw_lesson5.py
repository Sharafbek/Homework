"""Homework:
users nomli tabelga Pythonda User classi yozasiz va ushbu classda save(),get_users,
get_user,delete_user(),update_user() metodlari bo'lsin va bu metod ishlaganda bazadayam
o'zgarishlar hosil bo'lsin"""

# =================>    Create table
import psycopg2

conn = psycopg2.connect(database='m5_lesson5',
                        user='postgres',
                        password='1234',
                        host='localhost',
                        port='5432')
cur = conn.cursor()


# create_users_table_query = '''CREATE TABLE IF NOT EXISTS users (
#                                 id SERIAL PRIMARY KEY,
#                                 full_name VARCHAR(255) NOT NULL,
#                                 age INTEGER NOT NULL,
#                                 address VARCHAR(255) NOT NULL,
#                                 CHECK(age>0));'''
#
# cur.execute(create_users_table_query)
# conn.commit()

class User:
    def __init__(self, full_name: str,
                 age: int,
                 address: str):
        self.full_name = full_name
        self.age = age
        self.address = address

    def save(self):
        insert_into_query = """INSERT INTO users (full_name,age,address) 
                               VALUES (%s,%s,%s);
                               """
        data = (self.full_name, self.age, self.address)
        cur.execute(insert_into_query, data)
        conn.commit()

    @staticmethod
    def get_users():
        get_users_query = """SELECT * FROM users;"""
        cur.execute(get_users_query)
        users = cur.fetchall()
        return users

    @staticmethod
    def get_user():
        get_user_query = """SELECT * FROM users WHERE age = 23;"""
        cur.execute(get_user_query)
        user = cur.fetchone()
        return user

    @staticmethod
    def delete_user():
        delete_user_query = """DELETE FROM users WHERE age BETWEEN 35 AND 45;"""
        cur.execute(delete_user_query)
        conn.commit()
        return "User deleted"

    @staticmethod
    def update_user():
        update_user_query = """UPDATE users SET full_name = 'Hamza', age = 48, address = 'Tashkent' WHERE id = 2;"""
        cur.execute(update_user_query)
        conn.commit()
        return "User updated"

# =======> Save data
# user1 = User('John Doe', 23, 'Washington')
# user1.save()

# =======> Get users
# get_users = User.get_users()
# print(get_users)

# =======> Get user
# get_user = User.get_user()
# print(get_user)

# =======> Delete data
# delete_user = User.delete_user()
# print(delete_user)

# =======> Update data
# update_user = User.update_user()
# print(update_user)
