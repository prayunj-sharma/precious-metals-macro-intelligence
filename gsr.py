# Gold-Silver Ratio Project
import yfinance as yf
import matplotlib.pyplot as plt

def fetch_data():
    gold_data = yf.download('gc=f', start='2001-01-01', end='2026-03-31')
    silver_data = yf.download('si=f', start='2001-01-01', end='2026-03-31')

    # print(gold_data)
    # print(silver_data)

    gold_close = gold_data["Close"] .squeeze()
    silver_close = silver_data["Close"] .squeeze()

    #print(gold_close)
    #print(silver_close)
    # print(gsr)

    gsr = (gold_close / silver_close)
    return gsr
gsr = fetch_data()

def analyse_gsr(gsr):
    print(f"Current Gold Silver Ratio: {gsr.iloc[-1]:.2f}")
    print(f"Average Gold Silver Ratio: {gsr.mean() :.2f}")
    print(f"Maximum Gold silver Ratio: {gsr.max():.2f}" )
    print(f"Minimum Gold Silver Ratio: {gsr.min():.2f}")
    print(f"Maximum Gold Silver Ratio on: {gsr.idxmax().date()}")
    print(f"Minimum Gold Silver Ratio on: {gsr.idxmin().date()}")

# Determine if GSR is above normal range or below it and suggest Buy/Sell/Hold signal
    if gsr.iloc[-1] > 80:
        print("Currently GSR is too High, Strong Buy Signal")
    elif gsr.iloc[-1] < 50:
        print("Currently GSR is too Low, Strong Sell Signal")
    else:
        print("Currently GSR is in normal range.")

analyse_gsr(gsr)

# Matplot Example data
# x = (2021,2022,2023,2024)
# y = (3,5,9,26)
# plt.plot(x,y)
# plt.show()

def plot_gsr(gsr):
    plt.plot(gsr.index,gsr.values)
    plt.title("Gold Silver Ratio - Historical Analysis (2001-2026)")
    plt.xlabel("Years")
    plt.ylabel("GSR - Gold Silver Ratio")
    plt.axhline(y=gsr.mean(),color="red",linestyle="--",label="Historical Average")

    plt.axhspan(80,130, alpha=0.10, color="red", label=" OverHeated Zone (GSR > 80)")
    plt.axhspan(30,50, alpha=0.10, color="green", label=" Opportunity Zone (GSR < 50)")
    plt.legend()

    plt.show()

plot_gsr(gsr)
