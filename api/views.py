from flask import Blueprint, jsonify
from logs import logger_api
from api.utils import get_all_posts, get_single_post

# Creating a blueprint
api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.get('/api/posts/')
def api_get_all_posts():
    """ Endpoint API for all posts """
    logger_api.info('Getting a json data of all posts')
    return jsonify(get_all_posts())


@api_blueprint.get('/api/posts/<int:pk>')
def api_get_single_post(pk):
    """ Endpoint API for one post """
    logger_api.info(f'Getting a json data of a single post with pk \'{pk}\'')
    return jsonify(get_single_post(pk))
