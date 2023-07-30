import pandas as pd
from werkzeug.security import generate_password_hash

df = pd.read_excel("Employee_Roster.xlsx")

with open("import.sql", "w") as file:
    for index, row in df.iterrows():
        email = row['Email']
        firstname = row['First Name']
        lastname = row['Last Name']
        date_of_birth = row['Date of Birth']
        company_id = row['Company ID']

        password = generate_password_hash(f"{firstname}{date_of_birth.year}")  # Hash this password
        sql = f"INSERT INTO user (email, password_hash, firstname, lastname, date_of_birth, company_id) VALUES ('{email}', '{password}', '{firstname}', '{lastname}', '{date_of_birth}', '{company_id}');\n"
        file.write(sql)

    # Second pass to update the manager_id field for each user
    for index, row in df.iterrows():
        email = row['Email']
        manager_email = row['Manager Email']
        sql = f"UPDATE user SET manager_id = (SELECT id FROM user WHERE email = '{manager_email}') WHERE email = '{email}';\n"
        file.write(sql)


# # Chat GPT Code:
# import pandas as pd
# from werkzeug.security import generate_password_hash
# from app.models import User, Company
# from app import db

# df = pd.read_excel("Employee_Roster.xlsx")

# for index, row in df.iterrows():
#     email = row['Email']
#     firstname = row['First Name']
#     lastname = row['Last Name']
#     date_of_birth = row['Date of Birth']
#     company_id = row['Company ID']

#     # Create the password by concatenating firstname and year of birth.
#     password = generate_password_hash(f"{firstname}{date_of_birth.year}")

#     # Create a User instance.
#     user = User(email=email, 
#                 password_hash=password, 
#                 firstname=firstname, 
#                 lastname=lastname, 
#                 date_of_birth=date_of_birth, 
#                 companyId=company_id)
    
#     # Add the user to the session.
#     db.session.add(user)

# # Commit the changes to the database.
# db.session.commit()

# # Update the manager_id field for each user.
# for index, row in df.iterrows():
#     email = row['Email']
#     manager_email = row['Manager Email']

#     # Query the database for the manager and user.
#     manager = User.query.filter_by(email=manager_email).first()
#     user = User.query.filter_by(email=email).first()

#     # Update the manager_id field.
#     user.manager_id = manager.id

# # Commit the changes to the database.
# db.session.commit()
