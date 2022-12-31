import os
import boto3
from flask import Flask,jsonify
#from services.lookup import lookup
from routes import *
#import bot #Used even though shows as not accessed

app = Flask(__name__)

##Register the blueprint for each route
app.register_blueprint(index_blueprint)
#app.register_blueprint(compare_blueprint)
#app.register_blueprint(leaderboard_blueprint)
#app.register_blueprint(stats_blueprint)
#app.register_blueprint(result_blueprint)
#app.register_blueprint(score_blueprint)

dynamodb_client = boto3.client('dynamodb')

if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )


USERS_TABLE = os.environ['USERS_TABLE']


@app.route('/users/<string:user_id>')
def get_user(user_id):
    result = dynamodb_client.get_item(
        TableName=USERS_TABLE, Key={'userId': {'S': user_id}}
    )
    item = result.get('Item')
    if not item:
        return jsonify({'error': 'Could not find user with provided "userId"'}), 404

    return jsonify(
        {'userId': item.get('userId').get('S'), 'name': item.get('name').get('S')}
    )
