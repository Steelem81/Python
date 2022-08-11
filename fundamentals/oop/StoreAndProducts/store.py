class Store:
    def __init__(self, name, products):
        self.name = name
        self.products = products

    def add_product(self, new_product):
        """takes a product and adds it to the store"""
        pass

    def sell_product(self, id):
        """remofve the product from the store's list of product given the id and print its info"""
        pass

    def inflation(self, percent_increase):
        """increases the price of each product by the percent_increase given"""
        pass

    def set_clearance(self, category, percent_discount):
        """updates all the products matching the given category by reducing the price by the percent_discount given"""
        pass