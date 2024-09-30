class Product:
    def __init__(self, name, weight, category):# как всегда прежде всего инициализация
        self.name = str(name)# атрибуты
        self. weight = float(weight)
        self. category = str(category)
    def __str__(self): # возврат строки
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        p = file.read()
        file.close()
        return p
    def add (self, *products):
        file = open(self.__file_name, 'a')
        for i in products: # добавляем новые продукты из in products
            if i.name in self.get_products():
                print(f'продукт{i}уже есть в магазине')
            else:
                file.write(f'{i.name}, {i.weight}, {i.category}\n')
        file.close()
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
