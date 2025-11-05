from db_setup import session
from product import Product

def read_all_products():
    products = session.query(Product).all()
    return products

def add_product(product):
    session.add(product)
    session.commit()
    print('Product Added Successfully')

def search_product(id):
    product = session.query(Product).filter_by(id=id).first()
    return product

def update_product(id, price):
    old_product = search_product(id)
    if old_product:
        old_product.price = price
        session.commit()
        print('Product Updated Successfully')
    else:
        print('Product Not Found.')

def delete_product(id):
    old_product = search_product(id)
    if old_product:
        session.delete(old_product)
        session.commit()
        print('Product Deleted Successfully')
    else:
        print('Product Not Found.')
    