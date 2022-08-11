import store
import products

if __name__ == '__main__':
    product_dict = [
                            {'name':'hammer',
                            'price': 5.00,
                            'cateogry': 'handtool'
                            },
                            {'name':'saw',
                            'price': 3.00,
                            'cateogry': 'handtool'
                            },
                            {'name':'drill',
                            'price': 15.00,
                            'cateogry': 'powertool'
                            }
                        ]
    init_products = []
    for product in product_dict:
        init_products.append(products.Product(product))

    store1 = store.Store("JMart", init_products)
    print(store1)
    store1.add_product(new_product = {'name':'scissors', 'price': 3.00, 'category':'crafting'})
    print(store1)
    store1.inflation(0.01)
    print(store1)
    store1.sell_product(2)
    print(store1)

