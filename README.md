# Precious Metals Macro Intelligence Platform

A research-grade web platform for analyzing gold and silver through a macroeconomic lens. Built with Python and Streamlit.

## Features

**⭐ Gold & Silver Fair Value Calculator —**
Takes current market prices as input and calculates fair value using US and EU M2 money supply. Outputs overvalued/undervalued verdict with a downloadable report.

**📊 Gold Silver Ratio Analyzer —**
25 years of historical GSR data with signal zones — overheated above 80, opportunity below 50.

**📈 Real Interest Rates —**
Live US and India real interest rates via FRED API. Negative rate zones highlighted as bullish signals for gold.

**🏦 Central Bank Gold Monitor —**
Top 20 central bank gold holders and net purchase trends since 2002. Data sourced from World Gold Council.

## Tech Stack
- Python, Streamlit, Plotly
- yfinance, FRED API, World Gold Council data
- pandas, numpy

## Run Locally

```bash
git clone https://github.com/prayunj-sharma/precious-metals-macro-intelligence
cd metals_valuation
pip install -r requirements.txt
streamlit run app.py
