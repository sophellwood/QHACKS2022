from app import db
from app.models import URL

db_data = URL.query.all()

for i in db_data:
    print("id:", i.id)
    print("original url:", i.og_url)
    print("short url:",i.short_url)

