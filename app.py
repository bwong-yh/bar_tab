from pathlib import Path
import csv

def create_csv(path, drinks, sum, tip, total):
    with path.open('a+', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Drink', 'Price'])
        writer.writerows(drinks)
        writer.writerow(['Sum', sum])
        writer.writerow(['Tip', tip])
        writer.writerow(['Total', total])
        print('CSV created')


def calculate_total(drinks, tip=0.2):
    sum = 0

    for drink, price in drinks:
        sum += price

    return sum, tip, sum * (1 + tip)

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

    # calculate tip and total  
    if not drinks:
        print('No drinks added. Exiting program.')
        return

    sum, tip, total = calculate_total(drinks)

    # create csv
    create_csv(path, drinks, sum, tip, total)

    return

if __name__ == '__main__':
    main()