from flask import Blueprint, render_template
from logs import logger_main
from posts.post_dao import PostDAO
from posts.utils import load_bookmarks
from settings import POST_PATH

main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")

# Creating a DAO instance
post_dao = PostDAO(POST_PATH)


@main_blueprint.get('/')
def page_index():
    logger_main.info('Loading a main page')
    all_posts = post_dao.get_posts_all()
    try:
        bookmarks = load_bookmarks()
    except TypeError:
        return '<br><span style="margin-left:20px; color: blue;"><strong>json file not a list</span>'
    return render_template('index.html', all_posts=all_posts, bookmarks=bookmarks)
