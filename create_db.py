from flask import Flask
from config import Config
from schema import db
from sqlalchemy import inspect

#create Flask app, Flask path define
app = Flask(__name__)
#apply config setting
app.config.from_object(Config)
#connect Flask, DB
db.init_app(app)

with app.app_context():
    db.create_all()
    print("Database initialized.")
    #check db table
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    print("table list:")
    for table in tables:
        print(f" - {table}")

    # licenses table schema check
    print("licenses table schema:")
    columns = inspector.get_columns('licenses')
    for col in columns:
        print(f" - {col['name']} ({col['type']})")
