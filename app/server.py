from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from app import db
from app.models import User


def create_url(chars):
    return "98379283u0"

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
        new_url = create_url(5)
        print(new_url)
        
        if form.validate_on_submit():
            dburl = User(username = url, user_email = new_url, user_password = url)
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


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         url = form.username.data
#         # flash(url)
#         if url.find("https://") == -1:
#             url = "https://" + url
#             flash(url)
#         else:
#             flash(url)

#         # flash('Login requested for user {}, remember_me={}'.format(
#         #      form.username.data, form.remember_me.data))
#         return redirect(url_for('index'))
#     return render_template('login.html',  title='Sign In', form=form)




        # #store the form value
        # user_name = request.form["username"]
        # email = request.form["email"]
        # password = request.form["password"]
        
        
        
        # add the user object to the database
        
        
        # commit changes to the database 
        
    #     return 'User registration successful'

    # return render_template('register.html')