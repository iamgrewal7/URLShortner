import sqlite3
from flask import Flask, g

# Init Flask
app = Flask(__name__)

# databse Path
DATABASE = 'store.db'

def get_db():
    """This method createds a connection with databse
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    """This function creates db table from sql script
    """
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

init_db()
