from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    
with app.app_context():
    db.create_all()
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if not username or not email or not password:
            flash("All fields are required", "error")
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        new_User = User(username=username, email=email, password=hashed_password)
        
        try:
            db.session.add(new_User)
            db.session.commit()
            flash("Registration successful!", "success")
            return redirect(url_for('login'))
        except:
            db.session.rollback()
            flash("Username or Email already exists!", 'error')
            
    return render_template("register.html")

@app.route("/login")
def login():
    return "Login Page (To be implemented)"
    
if __name__ == "__main__":
    app.run(debug=True)