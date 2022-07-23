from flask import json
from json import JSONDecodeError
from logs import logger_api
from settings import POST_PATH


def get_all_posts():
    """ Loads posts data from json and returns a list """
    try:
        with open(POST_PATH, encoding="utf-8") as file:
            all_posts = json.load(file)
        return all_posts
    except FileNotFoundError:
        logger_api.error(f'File {POST_PATH} not found')
    except JSONDecodeError:
        logger_api.error(f'File {POST_PATH} is not valid')


def get_single_post(pk):
    try:
        return get_all_posts()[pk]
    except IndexError:
        logger_api.error(f'There is no post with pk {pk}')
    except TypeError:
        logger_api.error('Loaded data is not a list')
