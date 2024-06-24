from faker import Faker
from bcrypt import hashpw, gensalt
from app import create_app, db
from app.models import User

# Initialize Faker instance
fake = Faker()
app = create_app()

# Function to generate password hash
def generate_password_hash(password):
    return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

# Generate dummy data for users table
with app.app_context():
    for _ in range(50):
        # Generate username and email
        username = fake.user_name()
        email = fake.email()

        # Generate password and hash it
        password = fake.password()
        password_hash = generate_password_hash(password)

        # Assign role (e.g., regular user or administrator)
        role = 'user' if fake.boolean(80) else 'admin'

        user = User(username=username, email=email, password_hash=password_hash, role=role)
        # print(f"username:{username}\temail:{email}\tpassword:{password}\trole:{role}")
        
        # Insert data into users table
        db.session.add(user)

    # Commit changes
    db.session.commit()

