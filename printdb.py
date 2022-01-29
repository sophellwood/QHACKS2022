from app import db
from app.models import User

user_data = User.query.all()

for user in user_data:
    print(user.username)
    print(user.user_email)
