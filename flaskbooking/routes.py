from flask import render_template, url_for, flash, redirect, request
from flaskbooking import app, db, bcrypt
from flaskbooking.forms import RegistrationForm, LoginForm, EventForm, CustomerForm
from flaskbooking.models import User, Event, Customer
from flask_login import login_user, current_user, logout_user, login_required



@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your credentials.', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file)

@app.route("/event/new", methods=['GET', 'POST'])
@login_required
def new_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(title=form.title.data, start_time=form.start_time.data, end_time=form.end_time.data, payment=form.payment.data)
        db.session.add(event)
        db.session.commit()
        flash('The event has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_event.html', title='New Event', form=form)

@app.route("/customer/new", methods=['GET', 'POST'])
@login_required
def new_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        customer = Customer(f_name = form.f_name.data, l_name = form.l_name.data, phone = form.phone.data, f_name2 = form.f_name2.data, l_name2 = form.l_name2.data, phone2 = form.phone2.data, street_address = form.street_address.data, city = form.city.data, state = form.state.data, zip_code = form.zip_code.data)
        db.session.add(customer)
        db.session.commit()
        flash('The customer has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_customer.html', title='New Customer', form=form)
    



@app.route("/addcustomer")
@login_required
def addcustomer():
    return print('finish this page')