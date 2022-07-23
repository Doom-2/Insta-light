from flask import Blueprint, render_template, request, redirect

from logs import logger_main
from posts.post_dao import PostDAO
from posts.comment_dao import CommentDAO
from posts.utils import load_bookmarks, add_post_to_bookmarks, remove_post_from_bookmarks
from settings import POST_PATH, COMMENTS_PATH

# Creating a blueprint
post_blueprint = Blueprint('post_blueprint', __name__, template_folder="templates")

# Creating a DAO instances
post_dao = PostDAO(POST_PATH)
comment_dao = CommentDAO(COMMENTS_PATH)


# Creating a view for one post
@post_blueprint.get('/posts/<pk>/')
def page_post(pk):
    logger_main.info('Opening a single post')
    pk_list = post_dao.get_all_pk()

    try:
        int(pk)
    except ValueError:
        logger_main.error('Only int \'pk\' values is allowed')
        return '<br><span style="margin-left:20px; color: blue;"><strong>Only int \'pk\' values is allowed</span>'
    if int(pk) not in pk_list:
        logger_main.error(f'Post with \'pk\' {pk} does not exist')
        return f'<br><span style="margin-left:20px; color: red;"><strong>Post with \'pk\' {pk} does not exist</span>'

    comments = comment_dao.get_comments_by_post_id(int(pk))
    post = post_dao.get_post_by_pk(int(pk))
    bookmarks = load_bookmarks()
    return render_template('post.html', post=post, comments=comments, bookmarks=bookmarks)


# Creating a view for specific user's posts
@post_blueprint.get('/users/<poster_name>/')
def page_user_feed(poster_name):
    logger_main.info('Opening a user feed')
    try:
        user_posts = post_dao.get_posts_by_user(poster_name)
        bookmarks = load_bookmarks()
    except ValueError:
        logger_main.error(f'There is no user with name {poster_name}')
        return f'<br><span style="margin-left:20px; color: blue;"><strong>' \
               f'There is no user with name \'{poster_name}\'</span> '
    return render_template('user-feed.html', user_posts=user_posts, poster_name=poster_name, bookmarks=bookmarks)


# Creating a view for posts containing a specific tag
@post_blueprint.get('/tag/<tag_name>/')
def page_tag_posts(tag_name):
    logger_main.info(f'Searching for posts with tag #{tag_name}')
    tag_posts = post_dao.get_post_by_tag(tag_name)
    bookmarks = load_bookmarks()
    return render_template('tag.html', tag_posts=tag_posts, tag_name=tag_name, bookmarks=bookmarks)


# Creating a view for posts containing a specific query
@post_blueprint.get('/search/')
def search_page():
    query = request.args.get('s', '')
    logger_main.info(f'Searching for page containing \'{query}\'')
    posts_by_query = post_dao.search_for_posts(query)
    bookmarks = load_bookmarks()
    return render_template('search.html', query=query, posts_by_query=posts_by_query, bookmarks=bookmarks)


# Creating a view for adding a specific post to bookmarks
@post_blueprint.get('/bookmarks/add/<int:pk>/')
def add_to_bookmark(pk):
    logger_main.info(f'Adding a post with pk \'{pk}\' to bookmarks')
    add_post_to_bookmarks(pk)
    return redirect("/", code=302)


# Creating a view for removing a specific post from bookmarks and view for removing & updating bookmarks page
@post_blueprint.get('/bookmarks/update/<int:pk>/')
@post_blueprint.get('/bookmarks/remove/<int:pk>/')
def remove_from_bookmark(pk):
    logger_main.info(f'Removing a post with pk \'{pk}\' from bookmarks')
    remove_post_from_bookmarks(pk)
    bookmarks_num = load_bookmarks()
    if bookmarks_num and request.url == f'{request.url_root}bookmarks/update/{pk}/':
        return redirect("/bookmarks/", code=302)
    return redirect("/", code=302)


# Creating a view for posts added to bookmarks
@post_blueprint.get('/bookmarks/')
def page_post_bookmarked():
    logger_main.info(f'Opening a bookmarked posts page')
    bookmarks = load_bookmarks()
    bookmarked_posts = post_dao.get_bookmarked_posts()
    return render_template('bookmarks.html', bookmarks=bookmarks, bookmarked_posts=bookmarked_posts)
