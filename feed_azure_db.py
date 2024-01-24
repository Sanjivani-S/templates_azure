import pymssql

conn = pymssql.connect(
    server='FirstServer-sgs.database.windows.net',
    user='FirstUser',
    password='idntknw12#',
    database='FirstDB',
    as_dict=True
)

query = "select  * from tab1"
cursor = conn.cursor()
cursor.execute(query)

records = cursor.fetchall()
print ("\nall the tables in DB are \n")
for r in records:
    print (f"{r['name']}")

print ("\n\n creating table.....\n\n")

create_table_query = "create table myTable (FirstName VARCHAR(20), LastName VARCHAR(20), email VARCHAR(50))"

cursor.execute(create_table_query)

insert_table_query = "INSERT into myTable (FirstName, LastName, email) values ('abc', 'abc', 'abc@abc.com'), ('xyz', 'xyz','xyz@xyz.com'), ('pqr', 'pqr', 'pqr@pqr.com')"
cursor.execute(insert_table_query)

select_query = "select * from myTable"
cursor.execute(select_query)
records = cursor.fetchall()
print ("First name \t Last name \t email\n")
for r in records:
    print(f"{r['FirstName']}\t\t{r['LastName']}\t\t {r['email']} ")


if conn:
     conn.commit()
     conn.close()
     print ("DB saved and connection closed")