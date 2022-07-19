from flask import Blueprint, render_template
from posts.post_dao import PostDAO

main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")

# Creating a DAO instance
post_dao = PostDAO("./data/data.json")

@main_blueprint.get('/')
def page_index():
    all_posts = post_dao.get_posts_all()
    return render_template('index.html', all_posts=all_posts)
