import pandas as pd

df = pd.read_csv('smartphones.csv')

# df = pd.read_json('students.json', encoding="UTF-8")

# df = pd.read_excel()
# excel için -pip install xlrd indirilmesi gerek

# connection = sqlite3.connect("example.db")
# df = pd.read_sql_query("SELECT * FROM students", connection)
# sql için -pip install pysqlite3 indirilmesi gerek


print(df)
