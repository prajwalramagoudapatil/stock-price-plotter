
# Prajwal Patil – Code Test  
Historical Price Visualizer

---

## 📌 Project Overview

This project was developed as part of a technical code assessment.

The application:

1. Fetches historical stock price data for Apple Inc. (AAPL) using the YFinance API  
2. Stores the data in a structured JSON format  
3. Generates a labeled line chart using Matplotlib  
4. Provides an interactive user interface using Streamlit  

The solution is modular, configurable, and designed for clarity and reusability.

---

## 🏗 Architecture

The project follows a clean separation of concerns:

- `fetch_prices.py` → Data acquisition and JSON export  
- `chart.py` → Visualization logic  
- `app.py` → User interface layer (Streamlit)  

This structure allows independent testing of each module.

---

## ⚙️ Technologies Used

- Python
- yfinance
- matplotlib
- Streamlit
- JSON

---

## 📂 Project Structure

```

.
├── fetch_prices.py
├── chart.py
├── app.py
├── requirements.txt
├── historicalPrices.json
├── chart.png
└── README.md

````

---

## 🚀 Installation

Clone the repository:

```bash
git clone <repository-link>
cd <repository-folder>
````

Create a virtual environment (recommended):

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 📊 Features

* Dynamic ticker input
* Custom date range selection
* Support for multiple price columns (Open, High, Low, Close, Volume)
* Configurable chart options
* JSON export of fetched data
* Programmatic chart image export

---

## ✅ Assignment Requirements Coverage

✔ Fetch historical AAPL data \
✔ Save results as `historicalPrices.json` \
✔ Generate a labeled matplotlib chart \
✔ Save chart as `chart.png` \
✔ Submit via GitHub repository 

---

## 👤 Author

Prajwal Patil



