import streamlit as st
import fetch_prices
import chart
from datetime import date

st.set_page_config(page_title="Stock Viewer", layout="wide")

st.title("Stock Price Visualizer")

st.sidebar.header("Stock Settings")

ticker = st.sidebar.text_input("Ticker Symbol", value="AAPL")

start_date = st.sidebar.date_input(
    "Start Date",
    value=date(2025, 2, 10)
)

end_date = st.sidebar.date_input(
    "End Date",
    value=date(2026, 2, 10)
)

columns_to_plot = st.sidebar.multiselect(
    "Columns to Plot",
    options=["Open", "High", "Low", "Close"],
    default=["Close"]
)

grid_visibility = st.sidebar.checkbox("Show Grid", value=True, )

xticks_month_interval = st.sidebar.number_input(
    "X-axis Tick interval(months)",
    min_value=1,
    value=1,
    step=1,
    max_value=12,
)

# Convert 0 to None
if xticks_month_interval == 0:
    xticks_month_interval = None

# --- ACTION BUTTON ---

if st.button("Fetch & Plot Data"):

    try:
        json_data = fetch_prices.fetch_prices(
            ticker=ticker,
            start_date=str(start_date),
            end_date=str(end_date)
        )

        fig = chart.create_plot(
            json_data=json_data,
            columns_to_plot=columns_to_plot,
            xlabel="Date",
            ylabel="Price (USD)",
            title=f"{ticker} Historical Prices",
            grid_visibility=grid_visibility,
            xticks_month_interval=xticks_month_interval,
            save_path="chart.png"
        )

        st.pyplot(fig)
        st.success("Chart generated successfully!")

    except Exception as e:
        st.error(f"Error: {e}")