import random


def generate_users_sql():
    user_roles = {2: ("Admin", 2), 3: ("HR", 3), 4: ("Manager", 10), 5: ("User", 35)}

    company_id = 35
    password = "pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f"

    user_count = 69  # starting from 70
    user_sql_statements = []

    manager_ids = []

    # Extended departments
    departments = [
        "Tech",
        "Sales",
        "Finance",
        "Marketing",
        "Support",
        "HR",
        "Operations",
        "Research",
    ]

    for role_id, (role_name, count) in user_roles.items():
        for i in range(count):
            user_count += 1

            if role_id == 4:
                manager_ids.append(user_count)

            email = f"{role_name.lower()}{user_count}@example.com"
            firstname = f"{role_name} {i + 1}"
            lastname = "User"
            dob = f"198{random.randint(0, 9)}-0{random.randint(1, 9)}-{random.randint(10, 29)}"
            title = f"{role_name} Title"

            image = "NULL"  # Assuming no image for now

            if role_id == 4:
                department = departments[i % len(departments)]
            else:
                department = random.choice(departments)

            if user_count in [75, 76]:
                manager_id = user_count  # They are their own managers
            elif 77 <= user_count <= 80:
                manager_id = 75
            elif 81 <= user_count <= 84:
                manager_id = 76
            else:
                manager_id = random.choice(manager_ids) if manager_ids else "NULL"

            user_sql = f"INSERT INTO user (email, password_hash, firstname, lastname, image, date_of_birth, companyId, manager_id, department, title, role_id) VALUES ('{email}', '{password}', '{firstname}', '{lastname}', '{image}', '{dob}', {company_id}, {manager_id}, '{department}', '{title}', {role_id});"
            user_sql_statements.append(user_sql)

    return user_sql_statements


def generate_results_sql(user_start_id, user_end_id):
    results_sql_statements = []

    start_year = 2020
    end_year = 2023

    for user_id in range(user_start_id, user_end_id + 1):
        for year in range(start_year, end_year + 1):
            for month in range(1, 13):  # for each month
                if year == 2020 and month < 1:
                    continue
                if year == 2023 and month > 8:
                    break
                date = f"{year}-{month:02}-01"
                scoreA = random.randint(0, 42)
                scoreB = random.randint(0, 42)
                scoreC = random.randint(0, 48)
                result_sql = f"INSERT INTO results (testDate, scoreA, scoreB, scoreC, user_id) VALUES ('{date}', {scoreA}, {scoreB}, {scoreC}, {user_id});"
                results_sql_statements.append(result_sql)

    return results_sql_statements


if __name__ == "__main__":
    user_sql = generate_users_sql()
    results_sql = generate_results_sql(70, 119)  # Extended user count

    # Combine all statements
    all_statements = user_sql + results_sql

    # Write to a file
    with open("insert_statements.sql", "w") as file:
        for statement in all_statements:
            file.write(statement + "\n")

    print("SQL statements generated and saved to insert_statements.sql!")
