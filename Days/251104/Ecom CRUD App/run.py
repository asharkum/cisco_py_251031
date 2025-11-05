from product import Product
import repo

def menu():
    option_str = '''Options are
    1 - Create Product
    2 - Search Product
    3 - Update Price
    4 - Delete Product
    5 - List All Products
    6 - Exit
    Your Choice = '''

    choice = int(input(option_str))
    if choice == 1:
        id = input('ID:')
        name = input('Name:')
        price = float(input('Price:'))
        
        index = repo.search_product(id)
        if index != -1:
            print('ID already exist.')
        else:
            repo.add_product(Product(id=id, name=name, price=price))
            print(f'Product {name} added successfully')
    elif choice == 2:
        id = input('ID:')
        index = repo.search_product(id)
        if index == -1:
            print('Product Not Found.')
        else:
            print(repo.products[index])
    elif choice == 3:
        id = input('ID:')
        index = repo.search_product(id)
        if index == -1:
            print('Product Not Found.')
        else:
            print(repo.products[index])
            new_price = float(input('New Price:'))
            repo.update_product(id, new_price)
            print(f'Product {repo.products[index].name} price updated successfully')
    elif choice == 4:
        id = input('ID:')
        index = repo.search_product(id)
        if index == -1:
            print('Product Not Found.')
        else:
            print(repo.products[index])
            repo.delete_product(id)
            print(f'Product {repo.products[index].name} deleted successfully')
    elif choice == 5:
        for product in repo.products:
            print(product)
    elif choice == 6:
        print('Exiting...')
    else:
        print('Invalid Choice.')

def menus():
    choice = menu()
    while choice != 6:
        choice = menu()
    print('End of application.')

menus()