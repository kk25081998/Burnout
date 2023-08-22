import random

def generate_users_sql():
    user_roles = {
        2: ("Admin", 2),
        3: ("HR", 2),
        4: ("Manager", 3),
        5: ("User", 13)
    }

    company_id = 9
    password = "pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f"
    
    user_count = 31  # starting from 32
    user_sql_statements = []

    manager_ids = []

    # For departments and manager assignment
    departments = ["Tech", "Sales"]
    manager_department = {1: "Tech", 2: "Tech", 3: "Sales"}

    for role_id, (role_name, count) in user_roles.items():
        for i in range(count):
            user_count += 1
            
            if role_id == 4:  # Collect manager IDs to assign to users later
                manager_ids.append(user_count)

            email = f"{role_name.lower()}{user_count}@example.com"  # Modified email to include user_id
            firstname = f"{role_name} {i + 1}"
            lastname = "User"
            dob = f"198{random.randint(0, 9)}-0{random.randint(1, 9)}-{random.randint(10, 29)}"  # Random DOB
            title = f"{role_name} Title"

            # Assign manager to a specific department
            if role_id == 4:
                department = manager_department[i + 1]
            else:
                department = random.choice(departments) 

            manager_id = random.choice(manager_ids) if role_id == 5 and manager_ids else "NULL"
            
            user_sql = f"INSERT INTO user (email, password_hash, firstname, lastname, date_of_birth, companyId, manager_id, department, title, role_id) VALUES ('{email}', '{password}', '{firstname}', '{lastname}', '{dob}', {company_id}, {manager_id}, '{department}', '{title}', {role_id});"
            user_sql_statements.append(user_sql)

    return user_sql_statements

def generate_results_sql(user_start_id, user_end_id):
    results_sql_statements = []

    for user_id in range(user_start_id, user_end_id + 1):
        for month in range(1, 13):  # for each month
            date = f"2023-{month:02}-01"
            scoreA = random.randint(0, 42)
            scoreB = random.randint(0, 42)
            scoreC = random.randint(0, 48)
            result_sql = f"INSERT INTO results (testDate, scoreA, scoreB, scoreC, user_id) VALUES ('{date}', {scoreA}, {scoreB}, {scoreC}, {user_id});"
            results_sql_statements.append(result_sql)

    return results_sql_statements



def generate_feedback_sql(company_id, user_start_id, user_end_id):
    feedback_sql_statements = []

    for user_id in range(user_start_id, user_end_id + 1):
        date_submitted = f"2023-01-01 10:10:{user_id:02}"
        description = f"Feedback from User {user_id}"
        feedback_sql = f"INSERT INTO feedback (company_id, date_submitted, description, status) VALUES ({company_id}, '{date_submitted}', '{description}', 'Pending');"
        feedback_sql_statements.append(feedback_sql)

    return feedback_sql_statements




if __name__ == '__main__':
    user_sql = generate_users_sql()
    results_sql = generate_results_sql(32, 51)  # User IDs start from 32 and end at 51
    feedback_sql = generate_feedback_sql(9, 32, 51)

    # Combine all statements
    all_statements = user_sql + results_sql + feedback_sql

    # Write to a file
    with open("insert_statements.sql", "w") as file:
        for statement in all_statements:
            file.write(statement + "\n")
    
    print("SQL statements generated and saved to insert_statements.sql!")