# Write the code you need here to figure out the answer
tables = client.list_tables(dataset)
for table in tables:
    print(table.table_id)
