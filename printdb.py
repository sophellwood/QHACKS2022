from app import db
from app.models import URL

db_data = URL.query.all()

for i in db_data:
    print("id: ", i.id)
    print("old url: ", i.old_url)
    print("new url: ",i.new_url)

