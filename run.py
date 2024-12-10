from app import db, create_app
from app.controllers.admin import create_admin

app = create_app()

with app.app_context():
    db.create_all()

create_admin(app)

if __name__ == "__main__":
    app.run()
