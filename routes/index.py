from flask import render_template, Blueprint

index_blueprint = Blueprint('index', 
                            __name__, 
                            template_folder='templates', 
                            static_folder='static')

@index_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')