from app import create_app, db
from flask_migrate import Migrate
from app.controllers.admin import create_admin

app = create_app()

Migrate(app, db)

create_admin()

if __name__ == "__main__":
    app.run()
