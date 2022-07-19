import json
from posts.post import Post


class PostDAO:
    def __init__(self, path: str):
        """ Creating a DAO instance, it is needed to specify the path to the JSON file """
        self.path = path

    def load_data(self) -> list:
        """ Loads data from post instance and return a list"""
        with open(self.path, encoding="utf-8") as file:
            all_posts_data = json.load(file)
            all_posts_obj_list = []  # An empty list for instances of class Post
            for post in all_posts_data:
                all_posts_obj_list.append(Post(
                    post['pk'],
                    post['poster_name'],
                    post['poster_avatar'],
                    post['pic'],
                    post['content'],
                    post['views_count'],
                    post['likes_count']
                ))
        return all_posts_obj_list

    def get_posts_all(self) -> list:
        """ Returns a list with all instances of the class Post """
        all_posts = self.load_data()
        return all_posts

    def get_all_posters(self) -> list:
        """ Returns a list of all users """
        all_posts = self.get_posts_all()
        posters_list = []
        for post in all_posts:
            posters_list.append(post.poster_name)
        return posters_list

    def get_all_pk(self) -> list:
        """ Returns a list of all post's pk """
        all_posts = self.get_posts_all()
        pk_list = []
        for post in all_posts:
            pk_list.append(int(post.pk))
        print(pk_list)
        return pk_list

    def get_posts_by_user(self, poster_name: str) -> list:
        """ Returns a list of posts instances of a specific poster by its 'poster_name' field"""
        if poster_name not in self.get_all_posters():
            raise ValueError

        all_posts = self.get_posts_all()
        poster_posts = []  # An empty list for posts instances of specific user
        for post in all_posts:
            if post.poster_name == poster_name:
                poster_posts.append(post)
        return poster_posts

    def get_post_by_pk(self, pk: int) -> list:
        """ Returns an instance of a specific post by its 'pk' field"""
        all_posts = self.get_posts_all()
        for post in all_posts:
            if post.pk == pk:
                return post

    def search_for_posts(self, query) -> list:
        """ Returns a list of posts instances containing the 'query' request """
        all_posts = self.get_posts_all()
        query_posts = []
        for post in all_posts:
            if query.lower() in post.content.lower():
                query_posts.append(post)

        return query_posts
