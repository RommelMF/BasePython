from os import getenv
from flask import Flask
from web_app.view.posts import posts_app
from web_app.models import db
from flask_migrate import Migrate

app = Flask(__name__, template_folder='templates')
app.register_blueprint(posts_app)
app_env = getenv("FLASK_ENV", 'development')
config_name = {
    "development": "config.DevelopmentConfig",
    "production": "config.ProductionConfig",
    "test": "config.TestingConfig"
}
app.config.from_object(config_name[app_env])
db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)