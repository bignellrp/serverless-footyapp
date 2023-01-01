from flask import Flask
#from services.lookup import lookup
from routes import *

app = Flask(__name__)

##Register the blueprint for each route
app.register_blueprint(index_blueprint)
#app.register_blueprint(compare_blueprint)
#app.register_blueprint(leaderboard_blueprint)
#app.register_blueprint(stats_blueprint)
#app.register_blueprint(result_blueprint)
#app.register_blueprint(score_blueprint)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=False, port=5000)