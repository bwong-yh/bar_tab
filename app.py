from pathlib import Path

def main():
    # get table number
    try:
        table_number = int(input('Table no: '))
        print(f'Starting tab for table {table_number}.')
    except ValueError:
        print('Not a valid table number. Exiting program.')

    # create path
    path = Path(__file__).parent / f'table_{table_number}.csv'
    print(path)

    # ask for drinks and prices

    # calculate tip and total

    # create csv
    
    return

if __name__ == '__main__':
    main()