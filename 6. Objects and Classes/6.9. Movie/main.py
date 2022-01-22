class Movie:
    def __init__(self, name, director):
        self.name = name
        self.director = director
        watched = False
        __watched_movies = []

    def change_name(self, new_name):
        self.name = new_name

    def change_director(self, new_director):
        self.director = new_director

    def watch(self):
        self.watched = True

    def __repr__(self):
        return f"Movie name: {self.name}] Movie director: {self.director}. Total watched movies: {__watched_movies}"