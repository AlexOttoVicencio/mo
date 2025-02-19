# classes/stock.py

import yfinance as yf
from datetime import date, datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Stock:
    def __init__(self, ticker):
        self._ticker = ticker
        print(f"The ticker: {ticker} was created")

    def basic_info(self):
        # Get current date
        today = date.today()
        one_year_ago = today - timedelta(days=365)
        
        # Get all the stock numbers
        stock_num = yf.download(self._ticker, one_year_ago, today)
        last_price = stock_num["Adj Close"].iloc[-1].round(2)
        previous_close = stock_num["Adj Close"].iloc[-2].round(2)
        change_percentage = ((last_price - previous_close) / previous_close * 100).round(2)
        volume = stock_num["Volume"].iloc[-1]
        
        # Historical performance
        ytd_start = datetime(today.year, 1, 1)
        ytd_data = stock_num[stock_num.index >= ytd_start]
        ytd_performance = ((last_price - ytd_data["Adj Close"].iloc[0]) / ytd_data["Adj Close"].iloc[0] * 100).round(2)
        
        high_52_week = stock_num["Adj Close"].max().round(2)
        low_52_week = stock_num["Adj Close"].min().round(2)
        max_value = stock_num["Adj Close"].max().round(2)
        average_value = stock_num["Adj Close"].mean().round(2)
        
        # Get stock text-written data
        stock_info = yf.Ticker(self._ticker)
        company_name = stock_info.info['longName']

        # Print stock information
        print(
            f"---------------------------------------------------\n"
            f"|                   Stock Information            |\n"
            f"---------------------------------------------------\n"
            f"| Company Name:          | {company_name}            |\n"
            f"| Ticker Symbol:         | {self._ticker}             |\n"
            f"---------------------------------------------------\n"
            f"|                  Current Market Data           |\n"
            f"---------------------------------------------------\n"
            f"| Current Price:         |    {last_price}            |\n"
            f"| Change (%):            |    {change_percentage:+.2f}%              |\n"
            f"| Volume:                |    {volume:,}                 |\n"
            f"---------------------------------------------------\n"
            f"|              Historical Performance            |\n"
            f"---------------------------------------------------\n"
            f"| YTD Performance:       |    {ytd_performance:+.2f}%              |\n"
            f"| 52-Week High:          |    {high_52_week}            |\n"
            f"| 52-Week Low:           |    {low_52_week}            |\n"
            f"| Max Value:             |    {max_value}            |\n"
            f"| Average Value:         |    {average_value}            |\n"
            f"---------------------------------------------------"
        )

        # Store information in instance variables
        self.company_name = company_name
        self.last_price = last_price
        self.change_percentage = change_percentage
        self.volume = volume
        self.ytd_performance = ytd_performance
        self.high_52_week = high_52_week
        self.low_52_week = low_52_week
        self.max_value = max_value
        self.average_value = average_value

    def generate_pdf(self, filename="stock_info.pdf"):
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter

        # Title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(30, height - 40, "Stock Information")

        # Content
        c.setFont("Helvetica", 12)
        text = [
            f"Company Name:          {self.company_name}",
            f"Ticker Symbol:         {self._ticker}",
            "---------------------------------------------------",
            "Current Market Data",
            "---------------------------------------------------",
            f"Current Price:         ${self.last_price}",
            f"Change (%):            {self.change_percentage:+.2f}%",
            f"Volume:                {self.volume:,}",
            "---------------------------------------------------",
            "Historical Performance",
            "---------------------------------------------------",
            f"YTD Performance:       {self.ytd_performance:+.2f}%",
            f"52-Week High:          ${self.high_52_week}",
            f"52-Week Low:           ${self.low_52_week}",
            f"Max Value:             ${self.max_value}",
            f"Average Value:         ${self.average_value}",
        ]

        y = height - 60
        for line in text:
            c.drawString(30, y, line)
            y -= 15

        c.save()
        print(f"PDF generated: {filename}")

# Example usage
#if __name__ == "__main__":
#    apple_stock = Stock("AAPL")
#    apple_stock.basic_info()
#    apple_stock
