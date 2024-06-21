#importing classes to outsource logic

from classes.stock import Stock









#Simple dictionary with terminal structure

def search_stock():
    ticker = input("Enter stock ticker: ")
    print(f"Searching for stock: {ticker}")
    ##construct stock
    searched_stock = Stock(ticker)


    # Add logic to search and display stock information

def display_stock_data():
    print("Displaying stock data")
    # Add logic to display stock data

def exit_program():
    print("Exiting...")
    exit()

def main():
    options = {
        '1': search_stock,
        '2': display_stock_data,
        '3': exit_program
    }
    
    while True:
        print("Welcome to MoonLanding ")
        print("1. Search for a stock")
        print("2. -----------------")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

