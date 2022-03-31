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

    @classmethod
    def free_page_slot(cls, photos):
        for page in range(len(cls.photos):
            if len(photos[page]) < 4:
                return page

    def add_photo(self, label):

                page.append(label)