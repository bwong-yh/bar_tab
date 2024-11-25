import csv
from pathlib import Path
import pandas as pd

class BarTab():
    def __init__(self, table_number):
        self.table_number = table_number
        self.drinks = []
        self.sum = 0
        self.tip = 0
        self.total = 0

    def get_receipt(self):
        path = Path(__file__).parent / f'table_{self.table_number}.csv'

        data = pd.read_csv(path)
        print(data.to_string(index=False))

    def create_csv(self):
        if not self.drinks:
            print('Nothing added.')
            return

        path = Path(__file__).parent / f'table_{self.table_number}.csv'

        with path.open('w+', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(['Drink', 'Price'])
            writer.writerows(self.drinks)
            writer.writerow(['Sum', self.sum])
            writer.writerow(['Tip', self.tip])
            writer.writerow(['Total', self.total])
            print('CSV created.')

    def calculate_total(self, tip=0.2):
        for _, price in self.drinks:
            self.sum += price

        self.tip = self.sum * tip
        self.total = self.sum + self.tip

    def server_user(self):
        while True:
            drink = input('Drink (press f to finish): ').strip().lower()

            if drink == 'f':
                break

            try:
                price = float(input(f'{drink.title()} price: ').strip())
                self.drinks.append((drink.title(), price))        
            except ValueError:
                print('Invalid price.')
                continue

def main():
    try:
        table_number = int(input('Enter table number: ').strip())
        tab = BarTab(table_number)
        print(f'New tab created for table {tab.table_number}.')

        tab.server_user()
        tab.calculate_total()
        tab.create_csv()
        tab.get_receipt()
    except ValueError:
        print('Not a valid table number.')

if __name__ == '__main__':
    main()