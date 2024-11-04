class Product:
    def __init__(self, name, weight, category):
        # Инициализация атрибутов товара: название, вес и категория
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        # Определяем строковое представление продукта для удобного вывода
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        # Имя файла, в котором хранятся данные о продуктах
        self.__file_name = 'products.txt'

    def get_products(self):
        # Открываем файл на чтение и возвращаем его содержимое
        with open(self.__file_name, 'r') as file:
            return file.read()

    def add(self, *products):
        # Получаем список уже существующих продуктов в магазине
        existing_products = self.get_products()
        for product in products:
            # Преобразуем объект продукта в строку для записи в файл
            product_str = str(product)
            # Проверяем, есть ли уже такой продукт в файле
            if product_str not in existing_products:
                # Если нет, добавляем его в конец файла
                with open(self.__file_name, 'a') as file:
                    file.write(product_str + '\n')
            else:
                # Если продукт уже есть, выводим сообщение об этом
                print(f'Продукт {product_str} уже есть в магазине')

# Создаем экземпляр магазина
s1 = Shop()

# Создаем несколько продуктов
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Выводим продукт p2 (благодаря методу __str__)
print(p2)

# Добавляем продукты в магазин
s1.add(p1, p2, p3)

# Выводим содержимое файла, чтобы увидеть все продукты в магазине
print(s1.get_products())
