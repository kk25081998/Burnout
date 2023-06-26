# StudyPlanGen

## Prerequisites

Before running the application, ensure that you have the following dependencies installed:

- Python
- SQLite

Additionally, make sure to download all necessary python packages by running the code:
```pip install -r requirements.txt```

## Getting Started

To start the application, follow these steps:

1. Configure the database:
   - Remove any existing databases by running the command: `rm app.db`
   - Open a Python terminal and run the following commands:
     ```python
     from app import create_app, db
     app = create_app()
     with app.app_context():
         db.create_all()
     ```

2. Start the Flask app:
   Open a terminal and run the command:
   ```
   python3 run.py
   ```

Once the application is running, you can access it in your web browser. Make sure to adapt the database settings if necessary, as the project currently uses SQLite for simplicity. Feel free to switch to a different database for production purposes or further practice.

## Common Commands

1. Database
Open the database: ```./sqlite3.exe app.db```
See all tables: ```.tables```