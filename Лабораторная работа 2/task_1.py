BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    """Класс книги с атрибутами id, name и pages."""

    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError("Идентификатор книги должен быть положительным целым числом.")
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть строковым типом данных.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")

        self._id = id_
        self._name = name
        self._pages = pages

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self._id}, name={self.name!r}, pages={self._pages})"

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
