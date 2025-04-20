class ConstructionMaterial:
    """Базовый класс для строительных материалов."""

    def __init__(self, material_type: str, weight: float, price_per_unit: float):
        """
        Конструктор для строительных материалов.

        :param material_type: Тип строительного материала
        :param weight: Вес одной единицы материала в килограммах
        :param price_per_unit: Цена за единицу материала в рублях
        """
        self.material_type = material_type
        self._weight = weight  # Непубличный атрибут для инкапсуляции
        self.price_per_unit = price_per_unit

    def __str__(self) -> str:
        """Возвращает строковое представление строительного материала."""
        return f"{self.material_type}: {self._weight} kg, {self.price_per_unit} руб."

    def __repr__(self) -> str:
        """Возвращает представление объекта для разработчиков."""
        return f"ConstructionMaterial(material_type={self.material_type!r}, weight={self._weight}, price_per_unit={self.price_per_unit})"

    def calculate_cost(self, quantity: int) -> float:
        """
        Рассчитывает стоимость заданного количества материала.

        :param quantity: Количество единиц материала
        :return: Общая стоимость
        """
        return quantity * self.price_per_unit


class Brick(ConstructionMaterial):
    """Класс для кирпичей, наследует от ConstructionMaterial."""

    def __init__(self, weight: float, price_per_unit: float, color: str):
        """
        Конструктор для кирпичей.

        :param weight: Вес одного кирпича в килограммах
        :param price_per_unit: Цена за один кирпич в рублях
        :param color: Цвет кирпича
        """
        super().__init__(material_type="Кирпич", weight=weight,
                         price_per_unit=price_per_unit)  # Вызов конструктора базового класса
        self.color = color

    def __str__(self) -> str:
        """Возвращает строковое представление кирпича с учетом его цвета."""
        return f"{super().__str__()} Цвет: {self.color}"

    def get_weight(self) -> float:
        """
        Получает вес кирпича.

        :return: Вес кирпича
        """
        return self._weight  # Доступ к непубличному атрибуту

    def calculate_cost(self, quantity: int) -> float:
        """
        Рассчитывает общую стоимость кирпичей с учетом скидки за большое количество.

        Если количество превышает 100, предоставляется скидка 10%.

        :param quantity: Количество кирпичей
        :return: Общая стоимость с учетом скидки
        """
        cost = super().calculate_cost(quantity)  # Вызов метода базового класса
        if quantity > 100:
            cost *= 0.9  # Применение скидки
        return cost
class Rebar(ConstructionMaterial):
    """Класс для арматуры, наследует от ConstructionMaterial."""

    def __init__(self, weight: float, price_per_unit: float, diameter: float):
        """
        Конструктор для арматуры.

        :param weight: Вес одного метра арматуры в килограммах
        :param price_per_unit: Цена за один метр арматуры в рублях
        :param diameter: Диаметр арматуры в миллиметрах
        """
        super().__init__(material_type="Арматура", weight=weight,
                         price_per_unit=price_per_unit)  # Вызов конструктора базового класса
        self.diameter = diameter

    def __str__(self) -> str:
        """Возвращает строковое представление арматуры с учетом ее диаметра."""
        return f"{super().__str__()} Диаметр: {self.diameter} мм"

    def get_weight(self) -> float:
        """
        Получает вес арматуры.

        :return: Вес арматуры
        """
        return self._weight  # Доступ к непубличному атрибуту

    def calculate_cost(self, length: float) -> float:
        """
        Рассчитывает стоимость арматуры по заданной длине.

        :param length: Длина арматуры в метрах
        :return: Общая стоимость
        """
        return length * self.price_per_unit  # Стоимость на основе длины

if __name__ == '__main__':
    brick = Brick(weight=3.5, price_per_unit=10, color="красный")
    print(brick)  # Печать информации о кирпиче
    print(f"Стоимость 150 кирпичей: {brick.calculate_cost(150)} руб.")  # Рассчет стоимости

    rebar = Rebar(weight=0.8, price_per_unit=30, diameter=12)
    print(rebar)  # Печать информации об арматуре
    print(f"Стоимость 20 метров арматуры: {rebar.calculate_cost(20)} руб.")  # Рассчет стоимости
