import sqlite3

con = sqlite3.connect("Test_db.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS student(
            user_id INTEGER,
            NameStudent TEXT,
            group_student TEXT
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS teacher(
id_user INTEGER,
NameTeacher TEXT)""")

cur.execute("""CREATE TABLE IF NOT EXISTS reg_teacher(
NameTeacher TEXT,
Verification_code INTEGER)""")