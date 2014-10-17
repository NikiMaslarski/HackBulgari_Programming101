class Store:

    def __init__(self, name):
        self.name = name
        self.__storage = {}
        self.__income = 0

    def load_new_products(self, product, count):
        if product in self.__storage.keys():
            self.__storage[product] += count
        else:
            self.__storage[product] = count

    def list_products(self, product_class):
        for item in self.__storage.keys():
            if isinstance(item, type(product_class)):
                print("{} - {}".format(item, self.__storage[item]))

    def sell_product(self, product):
        if product not in self.__storage.keys() or \
           self.__storage[product] == 0:
            return False
        else:
            self.__storage[product] -= 1
            self.__income += product.profit()
            return True

    def total_income(self):
        return self.__income

