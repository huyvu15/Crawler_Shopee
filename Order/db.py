import mysql.connector
   
# tạo đối tượng connection
db = mysql.connector.connect(host = "localhost", user = "root", password = "12345")

code = "CREATE DATABASE IF NOT EXISTS `TEST`;"

   

data_field = [
    ("item_id", "integer"),
    ("shop_id", "integer"),
    ("shop_name", "varchar(255)"),  # Đặt độ dài cho cột varchar
    ("name", "varchar(255)"),  # Đặt độ dài cho cột varchar
    ("item_price", "integer"),
    ("amount", "integer"),
    ("order_id", "integer"),
    ("status", "varchar(255)")  # Đặt độ dài cho cột varchar
]

list_str_field_name_and_field_type = [f"`{field[0]}` {field[1]}" for field in data_field]

result_field = ', '.join(list_str_field_name_and_field_type)  # Cách nhau bởi dấu ,
create_db = f"""
    CREATE TABLE IF NOT EXISTS `TEST` (
        {result_field}
    );
"""

mycursor = db.cursor()

mycursor.execute(create_db)
