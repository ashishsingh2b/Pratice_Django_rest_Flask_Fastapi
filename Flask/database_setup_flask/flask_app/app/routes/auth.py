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
