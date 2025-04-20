class Wood:
    def __init__(self, view: str, density: str, height: int):
        if not isinstance(view, str):
            raise TypeError("Вид дерева должен быть строковым типом данным")
        if not isinstance(density, int):
            raise TypeError("Плотность дерева должна быть целочисленной")
        if not density > 0:
            raise ValueError("Плотность дерева должна быть положительной")
        if not isinstance(density, int):
            raise TypeError("Высота дерева должна быть целочисленной")
        if not height > 0:
            raise ValueError("Высота дерева должна быть положительной")

        self.view = view
        self.density = density
        self.height = height

def addition_view(self, type_wood: str):
    if not isinstance(type_wood, str):
        raise TypeError("Тип дерева должен быть строковым типом данным")
    self.view += type_wood

def kgm3_in_gcm3 (self):
    return self.density * 0.001

def m_in_cm (self):
    return self.height * 100


class Book:
    def __init__(self, title: str, author: str, pages: int):
        if not isinstance(title, str):
            raise TypeError("Заголовок должен быть строковым типом данным")
        if not isinstance(author, str):
            raise TypeError("Автор должен быть строковым типом данным")
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целочисленным")
        if not pages > 0:
            raise ValueError("Количество страниц должно быть положительным")

        self.title = title
        self.author = author
        self.pages = pages

def change_title(self, new_title: str):
    if not isinstance(new_title, str):
        raise TypeError("Новый заголовок должен быть строковым типом данным")
    self.title = new_title

def addition_page(self, new_pages:int):
    if not isinstance(new_pages, int):
        raise TypeError("Количество новых страниц должно быть целочисленным")
    if not new_pages > 0:
        raise ValueError("Количество новых страниц должно быть положительным")
    self.pages += new_pages

class Clothes:
    def __init__(self, view: str, size: str, cloth: int):
        if not isinstance(view, str):
            raise TypeError("Вид одежды должен быть строковым типом данным")
        if not isinstance(size, int):
            raise TypeError("Размер одежды должен быть целочисленным")
        if not size > 0:
            raise ValueError("Размер одежды должен быть положительным")
        if not isinstance(cloth, str):
            raise TypeError("Ткань должна быть строковым типом данным")

        self.view = view
        self.size = size
        self.cloth = cloth

def addition_view(self, new_view: str):
    if not isinstance(new_view, str):
        raise TypeError("Новый вид одежды должен быть строковым типом данным")
    self.view = new_view

def replacement_size(self, letter_size:str):
    if not isinstance(letter_size, str):
        raise TypeError("Буквенный размер одежды должен быть строковым типом данным")
    self.size = letter_size

