from flask import Flask

from api.routes.users import users
from api.routes.login import login

app = Flask(__name__)

app.register_blueprint(users)
app.register_blueprint(login)

app.debug = True

if __name__ == "__main__":
    app.run