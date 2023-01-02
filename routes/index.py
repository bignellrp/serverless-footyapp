from flask import render_template, Blueprint
#from services.get_spread import player

index_blueprint = Blueprint('index', 
                            __name__, 
                            template_folder='templates', 
                            static_folder='static')

@index_blueprint.route('/', methods=['GET', 'POST'])
def index():

    '''A function for building the index page.
    Takes in available players from a flask form 
    and returns an even set of two 5 a side teams'''

    # players = player()
    # player_names = players.player_names()
    # player_count = players.player_count()
    return render_template('index.html')
    # return render_template('index.html', 
    #                         player_names = player_names, 
    #                         player_count = player_count)