from flask import Flask
from db import mongo
from home import homereq
from auth import authentication

app = Flask(__name__)
app.config.from_object('config')
mongo.init_app(app)

app.register_blueprint(authentication)
app.register_blueprint(homereq)


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
    app.run()
