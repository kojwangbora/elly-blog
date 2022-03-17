from app import create_app, db
from flask_migrate import Migrate
from app.models import User, Posts

app = create_app('production')

migrate = Migrate(app,db)

@app.shell_context_processor
def make_shell_context():
    return dict( db = db, User =User, Posts=Posts)