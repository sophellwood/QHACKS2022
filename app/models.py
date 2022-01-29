from app import db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key =True)
#     username = db.Column(db.String(100), nullable = False)
#     user_email = db.Column(db.String(100), nullable= False)
#     user_password = db.Column(db.String(150), nullable = False)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    old_url = db.Column(db.Text(), nullable = False)
    new_url = db.Column(db.Text(), nullable= False)