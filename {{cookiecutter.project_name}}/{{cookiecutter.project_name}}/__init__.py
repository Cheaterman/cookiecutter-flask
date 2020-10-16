from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData


app = Flask(__name__)
app.config.from_object('{{cookiecutter.project_name}}.config')

alembic_constraint_names = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}

metadata = MetaData(naming_convention=alembic_constraint_names)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from {{cookiecutter.project_name}} import model  # noqa
from {{cookiecutter.project_name}} import views  # noqa
