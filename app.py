from pathlib import Path


def serve_user():
    drinks = []
    
    while True:
        drink = input('Drink (press f to finish): ').strip().lower()

        if drink == 'f':
            break

        try:
            price = float(input(f'{drink.title()} price: ').strip())
            drinks.append((drink.title(), price))        
        except ValueError:
            print('Invalid price')
            continue

    return drinks

def main():
    # get table number
    try:
        table_number = int(input('Table no: '))
        print(f'Starting tab for table {table_number}.')
    except ValueError:
        print('Not a valid table number. Exiting program.')

    # create path
    path = Path(__file__).parent / f'table_{table_number}.csv'

    # ask for drinks and prices
    drinks = serve_user()
    print(drinks)

    # calculate tip and total

    # create csv
    
    return

if __name__ == '__main__':
    main()