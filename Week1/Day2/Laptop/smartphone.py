from product import Product


class Smartphone(Product):

    def __init__(self, name, stock_price, final_price,
                 display_size, mega_pixels):
        Product.__init__(self, name, stock_price, final_price)
        self.display_size = display_size
        self.final_price = final_price

