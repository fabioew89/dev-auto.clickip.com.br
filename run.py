from app import db, create_app
from app.controllers.admin import create_admin

app = create_app()

create_admin()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
