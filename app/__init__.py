
from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_migrate import Migrate

# from flask_uploads import configure_uploads, IMAGES, UploadSet

db = SQLAlchemy()
# bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap =Bootstrap()
mail = Mail()
migrate = Migrate()
# photos = UploadSet('photos', IMAGES)

def create_app():

    app = Flask(__name__)
    app.config.from_object(config_options['development'])
    

    # #configure requests
    # from .requests import configure_requests
    # configure_requests(app)

    #registering blueprints

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/auth')

    #initializinga extensions
    from .models import User,Posts,Comments
    db.init_app(app)
    
    migrate.init_app(app,db)
    # bcrypt.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
     # configure UploadSet
    # configure_uploads(app,photos)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app