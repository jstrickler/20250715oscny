import psycopg

pg_conn = psycopg.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password='scripts',
)
pg_cursor = pg_conn.cursor()

# select specified columns from all presidents
pg_cursor.execute('''
    select termnum, firstname, lastname, party
    from presidents order by termnum
''')  # execute a SQL statement

print(f"{pg_cursor.rowcount} rows in result set\n")

#for term, firstname, lastname, party in pg_cursor.fetchall():
#    print(f"{term:2d} {firstname:25} {lastname:20} {party}")
#print()

# for row in pg_cursor.fetchall():
#     print(row)
# print()

print(pg_cursor.fetchone())
print('-' * 60)
print(f"{pg_cursor.fetchall() = }")
print(f"{pg_cursor.fetchall() = }")
print(f"{pg_cursor.fetchone() = }")

pg_cursor.execute('''
    select termnum, firstname, lastname, party
    from presidents order by termnum
''')  # execute a SQL statement
print(f"{pg_cursor.fetchmany(100) = }")
print(f"{pg_cursor.fetchmany(100) = }")


pg_cursor.close()
pg_conn.close()

