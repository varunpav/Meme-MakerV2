from flask import Flask
from models import db, User, Meme

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meme_maker.db'
db.init_app(app)

with app.app_context():
    db.create_all()
