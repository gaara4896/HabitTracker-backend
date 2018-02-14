from flask_dotenv import DotEnv
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
env = DotEnv()
jwt = JWTManager()
mail = Mail()
migrate = Migrate()
