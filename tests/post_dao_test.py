from posts.post_dao import PostDAO
import pytest


@pytest.fixture()
def post_dao():
    post_dao_instance = PostDAO("./data/data.json")
    return post_dao_instance


def check_fields(post):
    """ Checks whether an instance of the class Post has all the listed attributes or not """

    # Defining the fields of the class Post we expect should be
    fields_should_be = [
        'pk',
        'poster_name',
        'poster_avatar',
        'pic',
        'content',
        'views_count',
        'likes_count'
    ]
    for field in fields_should_be:
        assert hasattr(post, field), f'Object has no attribute {field}'


class TestPostDAO:

    def test_get_posts_all(self, post_dao):
        """
        Checking whether correct list of instances of class Post returns or not
        and whether instance has all the listed attributes or not
        """
        posts = post_dao.get_posts_all()
        assert type(posts) == list, "Not a list has been returned"
        assert len(posts) > 0, "The posts list is empty"
        check_fields(posts[0])

    def test_get_posts_by_user(self, post_dao):
        """
        Checking whether correct list of instances of class Post returns
        by using of get_posts_by_user() method and checking instance fields as well
        """
        poster_posts = post_dao.get_posts_by_user('leo')
        assert type(poster_posts) == list, "Not a list has been returned"
        assert len(poster_posts) > 0, "The poster doesn't have any posts"
        check_fields(poster_posts[0])
        with pytest.raises(ValueError):
            post_dao.get_posts_by_user('not_exist_poster')

    def test_get_post_by_pk(self, post_dao):
        """
        Checking whether correct instance of class Post returns
        by using of get_posts_by_pk() method and checking instance fields as well
        """
        post = post_dao.get_post_by_pk(1)
        assert post.pk == 1, "Wrong post has been returned"
        check_fields(post)
