import pytest
from posts.comment_dao import CommentDAO
from settings import COMMENTS_PATH


@pytest.fixture()
def comment_dao():
    comment_dao_instance = CommentDAO(COMMENTS_PATH)
    return comment_dao_instance


def check_fields(comment):
    """ Checks whether an instance of the class Comment has all the listed attributes or not """

    # Defining the fields of the class Comment we expect should be
    fields_should_be = [
        'pk',
        'post_id',
        'commenter_name',
        'comment'
    ]
    for field in fields_should_be:
        assert hasattr(comment, field), f'Object has no attribute {field}'


class TestCommentDAO:

    def test_get_comments_by_post_id(self, comment_dao):
        """
        Checking whether correct list of instances of class Post returns
        by using of get_comments_by_post_id() method and checking instance fields as well
        """
        post_comments = comment_dao.get_comments_by_post_id(2)
        assert type(post_comments) == list, "Not a list has been returned"
        assert len(post_comments) > 0, "The post doesn't have any comments"
        check_fields(post_comments[0])
