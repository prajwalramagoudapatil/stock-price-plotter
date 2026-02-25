import yfinance as yf
import json

def fetch_prices(
    ticker,
    start_date,
    end_date,
    output_file="historicalPrices.json"
):
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        raise ValueError("No data returned. Check ticker or date range.")

    close_prices = data.reset_index()

    result = []

    for _, row in close_prices.iterrows():
        result.append({
            "Date": row["Date", ''].strftime("%Y-%m-%d"),
            "Open": float(row["Open", ticker]),
            "High": float(row["High", ticker]),
            "Low": float(row["Low", ticker]),
            "Close": float(row["Close", ticker]),
            "Volume": int(row["Volume", ticker])
        })

    with open(output_file, "w") as f:
        json.dump(result, f, indent=4)

    return result