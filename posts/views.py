from flask import Blueprint, render_template, request
from posts.post_dao import PostDAO
from posts.comment_dao import CommentDAO

# Creating a blueprint
post_blueprint = Blueprint('post_blueprint', __name__, template_folder="templates")

# Creating a DAO instances
post_dao = PostDAO("./data/data.json")
comment_dao = CommentDAO("./data/comments.json")


# Creating a view for one post
@post_blueprint.get('/posts/<pk>/')
def page_post(pk):
    pk_list = post_dao.get_all_pk()
    try:
        int(pk)
    except ValueError:
        return 'Only int \'pk\' values is allowed'
    if int(pk) not in pk_list:
        return f'Post with \'pk\' {pk} does not exist'
    comments = comment_dao.get_comments_by_post_id(int(pk))
    post = post_dao.get_post_by_pk(int(pk))
    return render_template('post.html', post=post, comments=comments)


# Creating a view for specific user's posts
@post_blueprint.get('/users/<poster_name>/')
def page_user_feed(poster_name):
    try:
        user_posts = post_dao.get_posts_by_user(poster_name)
    except ValueError:
        return f'There is no user with name {poster_name}'
    return render_template('user-feed.html', user_posts=user_posts)


# Creating a view for search post by query
@post_blueprint.get('/search/')
def search_page():
    query = request.args.get('s', '')
    posts_by_query = post_dao.search_for_posts(query)
    return render_template('search.html', query=query, posts_by_query=posts_by_query)
