from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from app import db
from app.models import URL
import secrets
import string
 



def create_url(chars):
    random_url = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(chars))
    # random_url = ''.join(secrets.choice(string.digits) for i in range(chars))

    db_data = URL.query.all()

    for i in db_data:
        if random_url == i.short_url:
            return create_url(chars)

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
        new_url = create_url(5)
        print(new_url)
        new_url = request.host_url + new_url
        if form.validate_on_submit():
            dburl = URL(og_url = url, short_url = new_url)
            db.session.add(dburl)
            db.session.commit()
            print("Successful submission")
            return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)

