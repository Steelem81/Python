import products 
class Store:
    def __init__(self, name, product_list):
        self.name = name
        self.product_list = product_list
    
    def __repr__(self):
        return(f"store: {self.name} contains {self.product_list}")

    def add_product(self, new_product):
        """takes a product and adds it to the store"""
        self.product_list.append(products.Product(new_product))
        return self

    def sell_product(self, id):
        """remofve the product from the store's list of product given the id and print its info"""
        self.product_list.pop(id)
        return self

    def inflation(self, percent_increase):
        """increases the price of each product by the percent_increase given"""
        self.product_list = [p.update_price(percent_increase, True) for p in self.product_list]
        return self

    def set_clearance(self, category, percent_discount):
        """updates all the products matching the given category by reducing the price by the percent_discount given"""
        pass