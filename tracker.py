import yfinance as yf

# Define your stock portfolio
portfolio = {
    'AAPL': 10,  # 10 shares of Apple
    'GOOGL': 5,  # 5 shares of Alphabet (Google)
    'MSFT': 15,  # 15 shares of Microsoft
    'TSLA': 8    # 8 shares of Tesla
}

def fetch_stock_price(ticker):
    stock = yf.Ticker(ticker)
    stock_info = stock.history(period='1d')
    return stock_info['Close'].iloc[-1]

def calculate_portfolio_value(portfolio):
    total_value = 0.0
    print(f"{'Stock':<10}{'Shares':<10}{'Price':<10}{'Value':<10}")
    print("="*40)
    
    for ticker, shares in portfolio.items():
        price = fetch_stock_price(ticker)
        value = shares * price
        total_value += value
        print(f"{ticker:<10}{shares:<10}{price:<10.2f}{value:<10.2f}")
    
    print("="*40)
    print(f"Total Portfolio Value: ${total_value:.2f}")

if __name__ == "__main__":
    calculate_portfolio_value(portfolio)
