from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)  # New field for first name
    last_name = db.Column(db.String(50), nullable=False)   # New field for last name

    def __repr__(self):
        return f'<User {self.username}>'


# Sample route
@app.route('/')
def index():
    return "Database migrations setup complete!"

if __name__ == '__main__':
    app.run(debug=True)
