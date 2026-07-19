from sqlalchemy import create_engine, inspect
from DB_Model import Base
import os

DB_FILENAME = 'game.db'
DB_PATH = os.path.join(os.path.dirname(__file__), DB_FILENAME)
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, echo=False)
inspector = inspect(engine)

def create_all_tables():
    """Creates all tables defined in Base metadata."""
    Base.metadata.create_all(engine)
    print("✅ Database tables created/updated successfully.\n")


def check_tables_and_columns():
    """Checks that all tables & columns match the SQLAlchemy models."""
    print("🔍 Checking tables and columns...\n")

    for table in Base.metadata.tables.values():
        table_name = table.name
        print(f"▶ Checking table: {table_name}")

        if not inspector.has_table(table_name):
            print(f"   ❌ Table missing: {table_name}")
            return False  # Something is missing → require full create
        else:
            print(f"   ✔ Table exists.")

        # Existing DB columns
        existing_columns = {
            col['name'] for col in inspector.get_columns(table_name)
        }

        # Required from model
        model_columns = {col.name for col in table.columns}

        # Compare
        missing = model_columns - existing_columns

        if missing:
            print(f"   ❌ Missing columns: {missing}")
            print("   ⚠️ Add manually or use Alembic migrations.")
        else:
            print("   ✔ All required columns exist.")

        print()  # spacing

    return True  # All tables + columns OK

def main():
    print("========== DATABASE VALIDATION ==========\n")

    # Create database file if missing
    if not os.path.exists(DB_PATH):
        print(f"❌ Database file '{DB_FILENAME}' does not exist.")
        print("➡️ Creating new database and tables...\n")
        create_all_tables()
        return

    print(f"ℹ️ Database file '{DB_FILENAME}' found.\n")

    # Check table structure
    tables_ok = check_tables_and_columns()

    if not tables_ok:
        print("⚠️ Tables missing → Creating all tables...")
        create_all_tables()
    else:
        print("✅ Database schema is up to date. Nothing to change.")


if __name__ == "__main__":
    main()
