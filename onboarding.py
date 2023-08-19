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


'''
Format we need for creating a user
| First Name | Last Name | Email              | Date of Birth | Company ID | Manager Email       | Role    |
|------------|-----------|--------------------|---------------|------------|---------------------|---------|
| John       | Doe       | john.doe@email.com | 1990-01-15    | 1          | hr.jane@email.com   | User    |
| Jane       | Smith     | hr.jane@email.com  | 1985-12-20    | 1          | admin.bob@email.com | HR      |
| Bob        | Brown     | admin.bob@email.com| 1982-05-30    | 1          |                     | Admin   |
| Alice      | Green     | alice.g@email.com  | 1995-04-10    | 1          | john.doe@email.com  | Manager |


**Onboarding Document**

Welcome to FlorishatWork!

We're excited to have you onboard. To make the onboarding process smooth and efficient, we require your employee roster in a specific format. This document outlines the structure and format of the Excel spreadsheet you'll need to provide.

Excel Document Structure:

Your Excel spreadsheet should have the following columns:

1. **Email**: The email address of the employee. This should be unique for each user.
2. **First Name**: The first name of the employee.
3. **Last Name**: The last name of the employee.
4. **Date of Birth**: The birth date of the employee in the format `MM/DD/YYYY`.
5. **Company ID**: The unique ID of your company. This will be provided by us.
6. **Manager Email**: The email of the manager/supervisor to whom the employee reports.
7. **Role**: The role of the user. This can be 'Admin', 'HR', 'Manager', or 'User. 

Important Notes:

- Please ensure that the **Email** column contains unique and valid email addresses for each user.
- If the **Role** column is left empty for a user, they will be onboarded as a regular user.
- The **Date of Birth** should be accurately filled in, as it plays a crucial role in our data processing.
- Please cross-check the **Manager Email** to ensure they correspond to a valid user in the **Email** column.
- It's crucial to avoid any typos or errors in the document to ensure a smooth onboarding process.


Sample Excel Entry:

| Email             | First Name | Last Name | Date of Birth | Company ID | Manager Email        | Role  |
|-------------------|------------|-----------|---------------|------------|----------------------|-------|
| john.doe@email.com| John       | Doe       | 01/15/1990    | 12345      | manager@email.com    | Admin |
| jane.doe@email.com| Jane       | Doe       | 03/22/1985    | 12345      | hrperson@email.com   |       |


Once your spreadsheet is ready, please share it with our onboarding team at [onboarding@yourwebapp.com](mailto:onboarding@yourwebapp.com) or through the dedicated portal on our website.

Thank you for your cooperation. Should you have any questions or need further clarification, feel free to reach out to us.

Warm Regards,

The FlorishatWork Team
'''

'''
Admin:
Overview: Has the highest level of access and is responsible for configuring and managing the burnout application.

Full System Access: Ability to view, modify, delete any data.
User Management: Can add, modify, or delete users, and set or modify their roles.
Settings & Configuration: Access to all system settings, including survey frequencies, reminders, etc.
Reporting: Generate system-wide reports on burnout trends, feedback, etc.
Data Backup & Recovery: Ensure data integrity and backups.
System Updates & Maintenance: Oversee app updates, especially with new burnout detection methodologies.
Audit Trails: View logs or audit trails of all system activities.
Content Management: Add, edit, or remove resources for burnout prevention.

HR:
Overview: Ensures employee well-being, understands burnout trends, and implements preventive measures.

Employee Burnout Data: View aggregated, non-identifiable data on employee burnout levels.
Intervention Initiatives: Launch and manage programs to reduce burnout based on the data.
Reporting: Generate reports on departmental burnout trends.
Feedback & Suggestions: Receive suggestions or feedback on improving work-life balance.
Resource Distribution: Share resources (articles, videos) about handling stress and burnout.
Anonymous Communication: Facilitate channels where employees can discuss their stress anonymously.

Manager:
Overview: Keeps a check on their team's well-being, ensuring that the work environment is conducive to mental health.

Team Burnout Data: View aggregated, non-identifiable data on their team's burnout levels.
Check-ins: Conduct regular check-ins with team members to discuss work-life balance.
Resource Sharing: Share resources on managing workload, stress, and ensuring a balanced work environment.
Workload Management: Adjust workloads based on feedback and burnout data.
Communication: Discuss team members' concerns privately and anonymously, if needed.

User (Regular Employee):
Overview: Provides feedback on their stress and burnout levels, accesses resources, and receives support.

Burnout Surveys: Regularly fill out surveys or feedback forms to rate their burnout levels.
Profile Management: Update personal settings, such as survey frequencies or reminders.
Resource Access: Browse articles, videos, and other resources on handling burnout.
Anonymous Feedback: Provide feedback on work stressors without revealing their identity.
Peer Support: Access to chat rooms or forums where employees discuss stress and provide mutual support.
'''