#importing classes to outsource logic

from classes.stock import Stock

def search_stock():
    ticker = input("Enter stock ticker: ")
    print(f"Searching for stock: {ticker}")
    # Construct stock
    searched_stock = Stock(ticker)
    # Call basic_info method to display stock information
    searched_stock.basic_info()
    return searched_stock

def create_pdf():
    ticker = input("Enter stock ticker for PDF: ")
    print(f"Creating PDF for stock: {ticker}")
    stock = Stock(ticker)
    stock.basic_info()
    filename = input("Enter filename for the PDF (default: stock_info.pdf): ")
    if not filename:
        filename = "stock_info.pdf"
    stock.generate_pdf(filename)

def create_graph():
    ticker = input("Enter stock ticker for graph: ")
    print(f"Creating graph for stock: {ticker}")
    stock = Stock(ticker)
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    filename = input("Enter filename for the graph (default: stock_graph.png): ")
    if not filename:
        filename = "stock_graph.png"
    stock.generate_graph(start_date, end_date, filename)

def create_moving_average():
    ticker = input("Enter stock ticker for moving average: ")
    print(f"Creating moving average for stock: {ticker}")
    stock = Stock(ticker)
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    window = int(input("Enter moving average window (e.g., 20 for 20-day MA): "))
    filename = input("Enter filename for the moving average graph (default: moving_average.png): ")
    if not filename:
        filename = "moving_average.png"
    stock.generate_moving_average(start_date, end_date, window, filename)

def indicators_menu():
    options = {
        '1': create_moving_average,
    }
    
    while True:
        print("Indicators Menu")
        print("1. Moving Average")
        print("2. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice in options:
            options[choice]()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    options = {
        '1': search_stock,
        '2': create_pdf,
        '3': create_graph,
        '4': indicators_menu
    }
    
    while True:
        print("Welcome to MoonLanding")
        print("1. Search for a stock")
        print("2. Create PDF for stock information")
        print("3. Create graph for stock")
        print("4. Indicators")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice in options:
            options[choice]()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
