class Song:
    def __init__(self, name, length: float, single: bool):
        self.name = name
        self.length = float(length)
        self.single = single

    def get_info(self):
        return f"{self.name} - {self.length}"


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = [*songs]
        self.published = False

    def add_song(self, song):
        if song.single is True:
            return f"Cannot add {song.name}. It's a single."
        elif song.name in self.songs:
            return f"Song is already in the album"
        elif self.published:
            return f"Cannot add songs. Album is published."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been successfully added to the album {self.name}"

    def remove_song(self, song):
        if not song.name in self.songs:
            return f"Song is already in the album"
        elif self.published:
            return f"Cannot remove songs. Album is published."
        else:
            self.songs.remove(song)
            return f"Removed song {song.name} from album {self.name}"

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published"
        else:
            return f"Album {self.name} is already published"

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.name} - {song.length}\n"
        return result


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if not album.name in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}"
        else:
            return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album):
        if not album in self.albums:
            return f"Album {album} is not found"
        elif album in self.albums and album.published:
            return "Album has been published. It cannot be removed."
        else:
            self.albums.remove(album)
            return f"Album {album} has been removed."

    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += f"{album.details()}\n"
        return result

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())