from product import Product


class Laptop(Product):

    def __init__(self, name, stock_price, final_price, diskspace, ram):
        Product.__init__(self, name, stock_price, final_price)
        self.diskspace = diskspace
        self.ram = ram

