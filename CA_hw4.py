import sqlite3
conn=sqlite3.connect('BBQ.db')
cursor=conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS meat(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        quantity INTEGER
        )''')
cursor.execute("INSERT INTO meat (name,price,quantity) VALUES ('chicken',30,5)")
cursor.execute("INSERT INTO meat (name,price,quantity) VALUES ('beaf',55,10)")
cursor.execute("INSERT INTO meat (name,price,quantity) VALUES ('pork',40,15)")
conn.commit()
cursor.execute("SELECT * FROM meat")
meat = cursor.fetchall()
print("烤肉列表:")
for Meat in meat:
    print(Meat)
#第一次變動
cursor.execute("UPDATE meat SET price=35 WHERE name='pork'")
conn.commit()
cursor.execute("SELECT*FROM meat")
meat = cursor.fetchall()
print("第一次變動後的烤肉列表:")
for Meat in meat:
    print(Meat)
#第二次變動
cursor.execute("UPDATE meat SET quantity=30 WHERE name='chicken'")
conn.commit()
cursor.execute("SELECT*FROM meat")
meat = cursor.fetchall()
print("第二次變動後的烤肉列表:")
for Meat in meat:
    print(Meat)
#第三次變動
cursor.execute("DELETE FROM meat WHERE price=40")
conn.commit()
cursor.execute("SELECT * FROM meat")
meat = cursor.fetchall()
print("第三次變動後的烤肉列表:")
for Meat in meat:
    print(Meat)
cursor.close()
conn.close()

