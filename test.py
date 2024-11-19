from python_functions import get_schema, get_data, transfer_tables


table_names = ["assm_options", "assm_questions", "assm_topics"]
db1_name = "database.sqlite"
db2_name = "db2.sqlite"
transfer_tables(db1_name, db2_name, table_names)


