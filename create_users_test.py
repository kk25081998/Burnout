import random

def generate_users_sql():
    roles = {
        2: "Admin",
        3: "HR",
        4: "Manager",
        5: "User"
    }

    company_id = 10
    password = "pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f"
    
    user_count = 11  # starting from 12
    user_sql_statements = []

    for role_id, role in roles.items():
        for i in range(5):  # 5 users per role
            user_count += 1
            email = f"{role.lower()}{i + 1}@example.com"
            firstname = f"{role} {i + 1}"
            lastname = "User"
            user_sql = f"INSERT INTO user (email, password_hash, firstname, lastname, companyId, role_id) VALUES ('{email}', '{password}', '{firstname}', '{lastname}', {company_id}, {role_id});"
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
    results_sql = generate_results_sql(12, 31)  # User IDs start from 12 and end at 31 (20 users in total)
    feedback_sql = generate_feedback_sql(10, 12, 31)

    # Combine all statements
    all_statements = user_sql + results_sql + feedback_sql

    # Write to a file
    with open("insert_statements.sql", "w") as file:
        for statement in all_statements:
            file.write(statement + "\n")
    
    print("SQL statements generated and saved to insert_statements.sql!")
