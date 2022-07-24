import json
from posts.comment import Comment


class CommentDAO:
    def __init__(self, path: str):
        """ Creating a DAO instance, it is needed to specify the path to the JSON file """
        self.path = path

    def load_data(self) -> list[Comment]:
        """ Loads data from post instance and return a list"""
        with open(self.path, encoding="utf-8") as file:
            all_comments_data = json.load(file)
            all_comments_obj_list = []  # An empty list for instances of class Comment
            for comment in all_comments_data:
                all_comments_obj_list.append(Comment(
                    comment['pk'],
                    comment['post_id'],
                    comment['commenter_name'],
                    comment['comment'],
                ))
        return all_comments_obj_list

    def get_comments_by_post_id(self, post_id: int) -> list:
        """ Returns a list of comments of a specific post by its 'post_id' field """
        all_comments = self.load_data()
        return [comment for comment in all_comments if comment.post_id == post_id]
