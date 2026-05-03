# Real Rates Calculation Project
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from fredapi import Fred
from dotenv import load_dotenv
import os

load_dotenv()
fred = Fred(api_key=os.getenv("FRED_API_KEY"))

# data = fred.get_series("DGS10")
# print(data)

def fetch_us_data():
    nominal = fred.get_series('DGS10')
    # print(fred.get_series('DGS10'))

    inflation = fred.get_series("T10YIE")
    # print(inflation)

    # Joining two columns in Dataframe
    us_data = (pd.concat([nominal,inflation], axis=1))

    us_data.columns = ["Nominal", "Inflation"]
    us_data = us_data.dropna()

    us_data["Real Rates"] = us_data["Nominal"] - us_data["Inflation"]
    return us_data
    print(us_data)

def analyze_us_rates(us_data):

    print(f"Current Real Rate: {us_data['Real Rates'].iloc[-1]:.2f}")
    print(f"Historic Average Real Rate: {us_data['Real Rates'].mean():.2f}")
    print(f"Maximum Real Rate: {us_data['Real Rates'].max():.2f}")
    print(f"Minimum Real Rate: {us_data['Real Rates'].min():.2f}")
    print(f"Days with Negative Real Rates: {(us_data["Real Rates"] < 0).sum()}")

    current_rate = us_data["Real Rates"].iloc[-1]

    if current_rate < 0:
        print(f"Current Real Rate: {current_rate:.2f} is in Negative (Bullish Trend) - Strong buy Signal for Gold.")
    else:
        print(f"Current Real Rate: {current_rate:.2f} is in Positive (Bearish Trend) - Neutral/Sell Signal for Gold.")


def plot_us_rates(us_data):
    plt.plot(us_data.index, us_data["Real Rates"])
    plt.title("United States Real Rates (2003-2026)")
    plt.xlabel("Years")
    plt.ylabel("Real Rates")

    plt.fill_between(us_data.index, us_data['Real Rates'],0 ,
                     where=(us_data['Real Rates'] < 0),
                     color='red', alpha=0.3, label='Negative Real Rate (Bullish for Gold)')
    plt.axhline(y=0,color="black",linestyle="--",label="Zero Line")
    plt.legend()

    plt.show()


# Real Rates Calculation for India

def fetch_ind_data():
    india_cpi = fred.get_series("INDCPIALLMINMEI")
    # print(india_cpi)

    # Converting CPI number into Percentage
    india_cpi_rate = india_cpi.pct_change (12) * 100

    india_bond = fred.get_series("INDIRLTLT01STM")
    # print(india_bond)

    ind_data = (pd.concat([india_bond, india_cpi_rate], axis=1))

    ind_data.columns = ["Nominal", "Inflation"]
    ind_data = ind_data.dropna()

    ind_data["Real Rates"] = ind_data["Nominal"] - ind_data["Inflation"]
    return ind_data
# print(ind_data)


def analyze_ind_rates(ind_data):

    print(f"Current Real Rate: {ind_data['Real Rates'].iloc[-1]:.2f}")
    print(f"Historic Average Real Rate: {ind_data['Real Rates'].mean():.2f}")
    print(f"Maximum Real Rate: {ind_data['Real Rates'].max():.2f}")
    print(f"Minimum Real Rates: {ind_data['Real Rates'].min():.2f}")
    print(f"Days with Negative Real Rates: {(ind_data['Real Rates'] < 0) .sum()}")

    current_rate = ind_data['Real Rates'].iloc[-1]

    if current_rate < 0:
        print(f"Current Real Rate: {current_rate:.2f} is in Negative (Bullish Trend) - Strong buy Signal for Gold.")
    else:
        print(f"Current Real Rate: {current_rate:.2f} is Positive (Bearish Trend) - Neutral/Sell Signal for Gold.")


def plot_ind_rates(ind_data):
    plt.plot(ind_data.index, ind_data["Real Rates"])
    plt.title("India Real Rates (2011-2026)")
    plt.xlabel("Years")
    plt.ylabel("Real Rates")

    plt.fill_between(ind_data.index, ind_data['Real Rates'],0 ,
                     where=(ind_data['Real Rates'] < 0),
                     color='red', alpha=0.3, label='Negative Real Rate (Bullish for Gold)')
    plt.axhline(y=0,color="black",linestyle="--",label="Zero Line")
    plt.legend()

    plt.show()

if __name__ == "__main__":
    us_data = fetch_us_data()
    analyze_us_rates(us_data)
    plot_us_rates(us_data)
    ind_data = fetch_ind_data()
    analyze_ind_rates(ind_data)
    plot_ind_rates(ind_data)







