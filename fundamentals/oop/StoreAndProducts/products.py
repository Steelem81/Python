class Product:
    def __init__(self, prd_dict):
        self.name = prd_dict.get('name')
        self.price = prd_dict.get('price')
        self.catetogry = prd_dict.get('category')

    def __repr__(self):
        return(f"{self.name}:{self.price}")

    def update_price(self, percent_change, is_increased):
        """updates the product's price. If is_increased is True, the price should increase by the percent_change provided. If False, the price should decrease by the percent_change provided."""
        priceDiff = self.price * percent_change
        if is_increased == True:
            self.price += priceDiff
        else:
            self.price -= priceDiff
        return self

    def print_info(self):
        """print the name of the product, its category, and its price."""
        print(f"Product: {self.name}, Category: {self.catetogry}, Price: {self.price}")
        return self