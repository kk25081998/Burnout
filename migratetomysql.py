import sqlite3_to_mysql

# Define the conversion parameters
conversion_config = {
    "sqlite_db": "app.db",
    "mysql_db": "burnoutdev",
    "mysql_user": "root",
    "mysql_password": "S@!K@k2508",
    "mysql_host": "localhost",
    "mysql_port": 3306,
}

# Perform the conversion
sqlite3_to_mysql.convert(**conversion_config)