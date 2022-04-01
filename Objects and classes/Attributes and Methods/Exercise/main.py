def create_matrix(n):
    lst = []
    for num in range(n):
        lst.append([])
    return lst


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = create_matrix(self.pages)

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count / 4)

    @staticmethod
    def first_page_with_free_slot(photos):
        for page in range(len(photos)):
            if len(photos[page]) < 4:
                return page, len(photos[page]) + 1
        return False, False

    def add_photo(self, label):
        first_free_page, slot = PhotoAlbum.first_page_with_free_slot(self.photos)
        if first_free_page is False:
            return "No more free slots"
        self.photos[first_free_page].append(label)
        return f"{label} photo added successfully on page {first_free_page + 1} slot {slot}"


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
