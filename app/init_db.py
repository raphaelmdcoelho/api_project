"""Populate database with sample data."""
from datetime import date
from app.database import SessionLocal, engine
from app.models import Base, User


def init_db():
    """Initialize database with sample data."""
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    
    # Check if data already exists
    if db.query(User).count() > 0:
        print("Database already populated.")
        db.close()
        return

    # Create sample users
    users = [
        User(
            name="Alice Johnson",
            birthdate=date(1990, 5, 15),
            gender="Female"
        ),
        User(
            name="Bob Smith",
            birthdate=date(1985, 8, 22),
            gender="Male"
        ),
        User(
            name="Carol Davis",
            birthdate=date(1992, 3, 10),
            gender="Female"
        ),
        User(
            name="David Wilson",
            birthdate=date(1988, 11, 30),
            gender="Male"
        ),
        User(
            name="Emma Brown",
            birthdate=date(1995, 7, 18),
            gender="Female"
        ),
    ]

    db.add_all(users)
    db.commit()
    db.close()
    
    print("✅ Database initialized with 5 sample users")


if __name__ == "__main__":
    init_db()
