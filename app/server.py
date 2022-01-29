from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from app import db
from app.models import URL
import secrets
import string
 



def create_url(chars):
    # random_url = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(chars))
    random_url = ''.join(secrets.choice(string.digits) for i in range(chars))

    db_data = URL.query.all()

    for i in db_data:
        if i.short_url == random_url:
            print("id", id)
            print("url:",i.short_url)
            create_url(chars)

    return random_url

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":

        req = request.form
        url = req.get("username") 
        print(url)
        new_url = create_url(1)
        # db_data = URL.query.all()

        # for i in db_data:
        #     if i.short_url == new_url:
        #         print(i)
        #         create_url(1)

        print(new_url)
        
        if form.validate_on_submit():
            dburl = URL(og_url = url, short_url = new_url)
            db.session.add(dburl)
            db.session.commit()
            print("Successful submission")
            return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     #check the request method to ensure the handling of POST request only
#     # if request.method == "POST":
#     form = LoginForm()
#     if form.validate_on_submit():
#         url = form.username.data
#         flash(url)
#             # store the user details in the user database table
#         dburl = User(username = url, user_email = url, user_password = url)
#         db.session.add(dburl)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('login.html',  title='Sign In', form=form)