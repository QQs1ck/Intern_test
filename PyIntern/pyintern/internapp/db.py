import psycopg2

def input_psql(t):

    try:

        conn = psycopg2.connect(dbname='test_db', user='postgres', password='FU389', host='localhost')
    except:

        print('Can`t establish connection to database')

    zapzap = """INSERT INTO list1 (que) 
            VALUES ('{text}');""".format(text = t)

    cursor = conn.cursor()
    cursor.execute(zapzap)

    cursor.execute("SELECT * FROM list1")
    print(cursor.fetchall())
    conn.commit()
    cursor.close()
    conn.close()