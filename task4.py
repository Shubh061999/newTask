import psycopg2

try:
    connection = psycopg2.connect(
        dbname="test",
        user="shubham",
        password="shubham",
        host="127.0.0.1",
        port="5432"
    )

    cursor = connection.cursor()

    query = "SELECT * from employees;"
    cursor.execute(query)

    result = cursor.fetchall()
    for i in result:
        print(i)
    connection.close()
except Exception as e:
    print(e)


