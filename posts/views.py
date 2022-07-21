from flask import Blueprint, render_template, request
from posts.post_dao import PostDAO
from posts.comment_dao import CommentDAO
from settings import POST_PATH, COMMENTS_PATH, logger_main

# Creating a blueprint
post_blueprint = Blueprint('post_blueprint', __name__, template_folder="templates")

# Creating a DAO instances
post_dao = PostDAO(POST_PATH)
comment_dao = CommentDAO(COMMENTS_PATH)


# Creating a view for one post
@post_blueprint.get('/posts/<pk>/')
def page_post(pk):
    logger_main.info('Open a single post')
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
    return render_template('post.html', post=post, comments=comments)


# Creating a view for specific user's posts
@post_blueprint.get('/users/<poster_name>/')
def page_user_feed(poster_name):
    logger_main.info('Opening a user feed')
    try:
        user_posts = post_dao.get_posts_by_user(poster_name)
    except ValueError:
        logger_main.error(f'There is no user with name {poster_name}')
        return f'There is no user with name {poster_name}'
    return render_template('user-feed.html', user_posts=user_posts)


# Creating a view for search post by query
@post_blueprint.get('/search/')
def search_page():
    query = request.args.get('s', '')
    logger_main.info(f'Searching for page containing \'{query}\'')
    posts_by_query = post_dao.search_for_posts(query)
    return render_template('search.html', query=query, posts_by_query=posts_by_query)
