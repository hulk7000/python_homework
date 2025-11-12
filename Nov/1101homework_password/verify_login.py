from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash
from class_pratice2_model import UserAccount

def verify_login(session: Session, username_or_email: str, password: str):
    """
    Verify a user's login credentials.

    :param session: SQLAlchemy database session
    :param username_or_email: username or email for login
    :param password: plain-text password to verify
    :return: (bool, UserAccount or str) — (success, user or error message)
    """

    # Try to find user by username or email
    user = session.query(UserAccount).filter(
        (UserAccount.username == username_or_email) | (UserAccount.email == username_or_email)
    ).first()

    if not user:
        return False, "User not found."

    # Check hashed password
    if check_password_hash(user.password_hash, password):
        return True, user  # Successful login
        print(f"{UserAccount.username} Successful login")
    else:
        return False, "Incorrect password."


def create_user(session: Session, username: str, email: str, password: str):
    """
    Create a new user account safely.

    :param session: SQLAlchemy session
    :param username: desired username
    :param email: user email
    :param password: plain text password (will be hashed)
    :return: (bool, UserAccount or str) — success and either user object or error message
    """
    # Check for existing user with same username or email
    existing_user = session.query(UserAccount).filter(
        (UserAccount.username == username) | (UserAccount.email == email)
    ).first()

    if existing_user:
        return False, "Username or email already exists."

    # Hash password before saving
    hashed_password = generate_password_hash(password)

    # Create and add new user
    new_user = UserAccount(
        username=username,
        email=email,
        password_hash=hashed_password
    )

    try:
        session.add(new_user)
        session.commit()
        return True, new_user
    except IntegrityError as e:
        session.rollback()
        return False, f"Database error: {str(e)}"

