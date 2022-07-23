from api.utils import get_all_posts, get_single_post
from run import app

# Defining the fields we expect should be
keys_should_be = {
    'pk',
    'poster_name',
    'poster_avatar',
    'pic',
    'content',
    'views_count',
    'likes_count'
}


def test_api_get_all_posts():
    """
    Checks that request to endpoint '/api/posts/' is correct,
    that it returns a valid data with correct structure
    """
    all_posts = get_all_posts()
    response = app.test_client().get('/api/posts/')
    assert response.status_code == 200
    assert type(all_posts) == list
    assert set(all_posts[0].keys()) == keys_should_be
    assert response.json[0]["poster_name"] == "leo", "The received name is incorrect"


def test_api_get_single_post():
    """
    Checks that request to endpoint '/posts/0' is correct,
    that it returns a valid data with correct structure
    """
    single_post = get_single_post(0)
    response = app.test_client().get('/api/posts/0')
    assert response.status_code == 200
    assert type(single_post) == dict
    assert set(single_post.keys()) == keys_should_be
    assert response.json.get("poster_name") == "leo", "The received name is incorrect"
