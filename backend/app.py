from flask import Flask
from flask_cors import CORS
from api.routes.users import users
from api.routes.login import login
from api.routes.roster import roster

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(users)
app.register_blueprint(login)
app.register_blueprint(roster)

app.debug = True

if __name__ == "__main__":
    app.run()
