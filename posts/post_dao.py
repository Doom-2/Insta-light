import json
from posts.post import Post
from posts.utils import load_bookmarks, remove_html_tags


class PostDAO:
    def __init__(self, path: str):
        """ Creating a DAO instance, it is needed to specify the path to the JSON file """
        self.path = path

    def load_data(self) -> list[Post]:
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

    def get_posts_all(self) -> list[Post]:
        """
        Returns a list with all instances of the class Post
        where field 'pure_content' has text without html tags
        It is used to proper trim post's description
        if it contains html tags in the first 50 characters
        """
        all_posts = self.load_data()
        for post in all_posts:
            post.pure_content = remove_html_tags(post.content)
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
        return pk_list

    def get_posts_by_user(self, poster_name: str) -> list:
        """ Returns a list of posts instances of a specific poster by its 'poster_name' field"""
        if poster_name not in self.get_all_posters():
            raise ValueError

        all_posts = self.get_posts_all()
        poster_posts = []
        for post in all_posts:
            if post.poster_name == poster_name:
                poster_posts.append(post)
        return poster_posts

    def get_post_by_pk(self, pk: int) -> Post:
        """ Returns an instance of a specific post by its 'pk' field"""
        all_posts = self.get_posts_all()
        if pk not in self.get_all_pk():
            raise ValueError('Post does not exist')
        for post in all_posts:
            if post.pk == pk:
                return post

    def get_post_by_tag(self, tag) -> list[Post]:
        """ Returns a list of posts instances containing a specific tag"""
        all_posts = self.get_posts_all()
        tag_posts = []
        for post in all_posts:
            if tag in post.content:
                tag_posts.append(post)
                print(tag)
        return tag_posts

    def search_for_posts(self, query: any) -> list[Post]:
        """ Returns a list of posts instances containing the 'query' request """
        all_posts = self.get_posts_all()
        query_posts = []
        for post in all_posts:
            if query.lower() in post.content.lower():
                query_posts.append(post)

        return query_posts

    def get_bookmarked_posts(self) -> list[Post]:
        """ Returns a list of post instances that have been added to bookmarks """
        all_posts = self.get_posts_all()
        bookmarks = load_bookmarks()
        bookmarked_posts = []
        for post in all_posts:
            if post.pk in bookmarks:
                bookmarked_posts.append(post)
        return bookmarked_posts
