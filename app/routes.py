from flask import render_template, redirect, flash, url_for, request
from app.forms import RegistrationForm, LoginForm
from app.models import User, Activity, Gear
from app import app, db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required


# Routes
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        
        flash(f'Account created! Try logging in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'error')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')


@app.route('/new_adventure')
def create_adventure():
    return render_template('new_adventure.html', title='Create New Adventure')


@app.route('/gear')
def gear():
    return render_template('gear.html')


@app.route('/about')
def about():
    return render_template('about.html')


# @app.route('/adventures', method=['GET'])
# def display_adventures():
#     pass

# @app.route('/new_adventure', methods=['POST'])
# def create_adventure():
#     adventure_data = {
#         'title': request.form['title'],
#         'activity': request.form['activity'],
#         'type': request.form['type'],
#         'created_by': request.form['created_by'],
#         'created_at': datetime.now()
#     }

#     # Insert the adventure data into the MongoDB collection
#     adventures_collection.insert_one(adventure_data)

#     return 'Adventure created successfully!'
