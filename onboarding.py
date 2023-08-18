import pandas as pd
from werkzeug.security import generate_password_hash

df = pd.read_excel("Employee_Roster.xlsx")

# Convert 'date_of_birth' column to pandas datetime object
df['Date of Birth'] = pd.to_datetime(df['Date of Birth'])

with open("import_employees.sql", "w") as file:
    for index, row in df.iterrows():
        email = row['Email']
        firstname = row['First Name']
        lastname = row['Last Name']
        date_of_birth = row['Date of Birth'].strftime('%Y-%m-%d')
        companyId = row['Company ID']

        # Check if 'Role' column is empty or NaN, and default to "User" if it is
        role = row['Role'] if not pd.isna(row['Role']) else 'User'

        password = generate_password_hash(f"{firstname}{row['Date of Birth'].year}")
        sql = f"INSERT INTO user (email, password_hash, firstname, lastname, date_of_birth, companyId, role) VALUES ('{email}', '{password}', '{firstname}', '{lastname}', '{date_of_birth}', '{companyId}', '{role}');\n"
        file.write(sql)

    # Second pass to update the manager_id field for each user
    for index, row in df.iterrows():
        email = row['Email']
        manager_email = row['Manager Email']
        sql = f"UPDATE user SET manager_id = (SELECT id FROM user WHERE email = '{manager_email}') WHERE email = '{email}';\n"
        file.write(sql)
