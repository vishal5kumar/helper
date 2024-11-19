import sqlite3

def get_schema(table_name,cursor):
 
    GET_SCHEMA = f"SELECT sql from sqlite_schema where name = '{table_name}'"
    query = ""
    data = cursor.execute(GET_SCHEMA)
    for i in data:
        query = i[0]
    return query



def get_data(table_name,cursor):
 
    GET_DATA = f"SELECT * FROM  {table_name}"
    data = cursor.execute(GET_DATA).fetchall()
    return data


def get_table_names(table_names):
    return table_names


def transfer_tables(db1_name, db2_name, table_array):
    db1_conn = sqlite3.connect(db1_name)
    db1_cursor = db1_conn.cursor()

    db2_conn = sqlite3.connect(db2_name)
    db2_cursor = db2_conn.cursor()



    for table_name in table_array:
    #2 to get the schema
        x = get_schema(table_name,db1_cursor)

# print(x)



#3 drop table in the output database
        try:
            db2_cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            db2_conn.commit()
            print("Table dropped in output (if it existed).")

        except sqlite3.OperationalError as e:
            print(f"Table drop failed: {e}")   




#4 create table in the output database that we input 
        TABLE1_SQL_CREATE_QUERY = x
# print("table name", x)
        db2_cursor.execute(TABLE1_SQL_CREATE_QUERY)
        db2_conn.commit()


#5 fetching data from the table
        db1_cursor.execute(f"SELECT * FROM {table_name}")
        data = db1_cursor.fetchall()


#6 inserting the data in the table 
        for i in data:
         try:
               
            insert_query = f"INSERT INTO {table_name} VALUES {i}"
            db2_cursor.execute(insert_query)
            print(f"Data inserted into '{table_name}' in output.sqlite")
            db2_conn.commit()
   
        
         except sqlite3.Error as e:
            print(f"Error inserting data into table: {e}")




#7 for closing the connection
    db1_conn.close()
    db2_conn.close()





