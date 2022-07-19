class Post:
    """ Post abstraction used for load data in PostDAO class """

    def __init__(self,
                 pk='',
                 poster_name='',
                 poster_avatar='',
                 pic='',
                 content='',
                 views_count=0,
                 likes_count=0
                 ):
        self.pk = pk
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count

    def __repr__(self):
        return f'Post from {self.poster_name}'
