import pprint

class Products:
    title: str = 'Chocolate'
    price: int = 1


Products.amount = 12
pprint.pprint(Products.__dict__)
