#!/bin/bash

# Define the project name and directories
PROJECT_NAME="flask_app"
APP_DIR="$PROJECT_NAME/app"
MODELS_DIR="$APP_DIR/models"
ROUTES_DIR="$APP_DIR/routes"
TEMPLATES_DIR="$APP_DIR/templates"
AUTH_TEMPLATES="$TEMPLATES_DIR/auth"
MAIN_TEMPLATES="$TEMPLATES_DIR/main"

# Create the main project folder and subfolders
mkdir -p $PROJECT_NAME
mkdir -p $APP_DIR
mkdir -p $MODELS_DIR
mkdir -p $ROUTES_DIR
mkdir -p $AUTH_TEMPLATES
mkdir -p $MAIN_TEMPLATES

# Create __init__.py files
touch $APP_DIR/__init__.py
touch $MODELS_DIR/__init__.py
touch $ROUTES_DIR/__init__.py

# Create config.py
cat <<EOL > $APP_DIR/config.py
import os
from datetime import timedelta

class Config:
    # Basic Flask config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    
    # Database config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Additional configs
    POSTS_PER_PAGE = 10
EOL

# Create __init__.py for the app
cat <<EOL > $APP_DIR/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from .routes import main, auth
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    
    return app
EOL

# Create models
cat <<EOL > $MODELS_DIR/user.py
from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
EOL

cat <<EOL > $MODELS_DIR/post.py
from datetime import datetime
from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
EOL

# Create route files
cat <<EOL > $ROUTES_DIR/auth.py
from flask import Blueprint, render_template, flash, redirect, url_for, request
from app.models.user import User
from app import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        user = User(username=username, email=email)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful!')
        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html')
EOL

cat <<EOL > $ROUTES_DIR/main.py
from flask import Blueprint, render_template
from app.models.post import Post

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('main/index.html', posts=posts)
EOL

# Create templates (HTML files)
touch $AUTH_TEMPLATES/register.html
touch $MAIN_TEMPLATES/index.html

# Create run.py
cat <<EOL > run.py
from app import create_app, db
from app.models import User, Post

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    app.run(debug=True)
EOL

# Create requirements.txt
cat <<EOL > requirements.txt
Flask
Flask-SQLAlchemy
Flask-Migrate
EOL

echo "Flask app setup complete. Project structure created."
