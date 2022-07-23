import re
import json
from json import JSONDecodeError
from logs import logger_main
from settings import BOOKMARKS_PATH


def _load_json(filename: str, encoding: str = 'utf-8') -> list:
    """ Reads json from file and returns a list """

    try:
        with open(filename, encoding=encoding) as f:
            return json.load(f)
    except FileNotFoundError:
        logger_main.error(f'File {filename} not found')
    except JSONDecodeError:
        logger_main.error(f'File {filename} is not valid')


def load_bookmarks() -> list:
    """ Loads bookmarks data and returns a list"""
    return _load_json(BOOKMARKS_PATH)


def add_post_to_bookmarks(pk: int) -> None:
    """ Adds post's pk to bookmarks list and returns its number of items"""
    bookmarks_list = load_bookmarks()
    bookmarks_list.append(pk)
    bookmarks_list = list(set(bookmarks_list))  # gets a unique items of a list
    with open(BOOKMARKS_PATH, 'w') as file:
        json.dump(bookmarks_list, file)


def remove_post_from_bookmarks(pk: int) -> None:
    """ Gets bookmarks list, removes a specific post's pk from it and rewrite a json """
    bookmarks_list = load_bookmarks()
    bookmarks_list.remove(pk)
    with open(BOOKMARKS_PATH, 'w') as file:
        json.dump(bookmarks_list, file)


def remove_html_tags(content: str):
    """ Removes html tags and extra spaces from content """
    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
    no_tags = tag_re.sub('', content)
    re.sub(r'\s+', ' ', no_tags)
    return no_tags
