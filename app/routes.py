from flask import render_template, redirect, flash, url_for
from app.forms import RegistrationForm, LoginForm
from app.models import User, Activity, Gear
from app import app


# Routes
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.email}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'adm@test.com' and form.password.data == 'password':
            flash('You are logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password.', 'error')
    return render_template('login.html', title='Login', form=form)

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
