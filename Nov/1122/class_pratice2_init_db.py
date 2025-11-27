from sqlalchemy import create_engine, inspect
from class_pratice2_model import Base
import os

# Define database path
db_path = os.path.join(os.path.dirname(__file__), 'guessgame.db')

# Create engine
engine = create_engine(f'sqlite:///{db_path}', echo=False)

# Function to create all tables from Base
def create_all_tables():
    Base.metadata.create_all(engine)
    print("✅ All tables from Base have been created/updated.")

# 1️⃣ Check if database file exists
if not os.path.exists(db_path):
    print("❌ Database file does not exist. Creating database file and tables...")
    create_all_tables()
else:
    print("ℹ️ Database file exists. Checking tables and columns...")

    inspector = inspect(engine)

    # Iterate over all tables defined in Base
    for table in Base.metadata.tables.values():
        table_name = table.name
        print(f"\nChecking table: '{table_name}'")

        # Check if table exists
        if not inspector.has_table(table_name):
            print(f"❌ Table '{table_name}' does not exist. Creating table...")
            create_all_tables()  # Creates all tables, including this one
        else:
            print(f"ℹ️ Table '{table_name}' exists. Checking columns...")

            # Get existing columns in the table
            existing_columns = [col['name'] for col in inspector.get_columns(table_name)]
            # Get required columns from the model
            required_columns = [col.name for col in table.columns]

            # Compare
            missing_columns = [col for col in required_columns if col not in existing_columns]

            if missing_columns:
                print(f"❌ Missing columns in '{table_name}': {missing_columns}")
                print("⚠️ Please add them manually or use a migration tool like Alembic.")
            else:
                print(f"✅ All required columns exist in '{table_name}'.")
