import pandas as pd
import streamlit as st
import plotly.graph_objects as go

@st.cache_data
def fetch_reserve_data():
    # Loads Data
    reserves = pd.read_excel("gold_reserves.xlsx", skiprows=5)

    # Displays max Columns
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    left = reserves [["Unnamed: 1", "Tonnes", "% of reserves**","Holdings as of "]]
    right = reserves [["Unnamed: 6", "Tonnes.1", "% of reserves**.1","Holdings as of .1"]]

    # Rename right columns to match left
    right.columns = ["Unnamed: 1", "Tonnes", "% of reserves**","Holdings as of"]

    # Stack them Vertically (Above one another)
    combined = pd.concat([left, right], axis=0)

    # print(combined.columns)

    # Drop duplicate columns
    combined = combined.iloc[:, :4]

    # Rename column names
    combined.columns = ["Country", "Tonnes", "Pct_Reserves", "Holdings_Date"]

    # Drop NaN rows
    combined = combined.dropna(subset=["Country"])

    # Reset Index
    combined = combined.reset_index(drop=True)

    # Convert tonnes to numeric values
    combined["Tonnes"] = pd.to_numeric(combined["Tonnes"], errors="coerce")

    # Convert Pct (%) reserve to numeric value
    combined["Pct_Reserves"] = pd.to_numeric(combined["Pct_Reserves"], errors="coerce")

    # print(combined.head(20))

    # print(reserves.head(10))
    # print(reserves.shape)
    # print(reserves.columns)

    return combined

# print(reserve_data)

# Chart Plotting

def plot_top_holdings(reserve_data):


    # Remove World and ECB gold holdings
    top20 = reserve_data[~reserve_data["Country"].str.contains("World|Euro",na=False)]

    # Sort by tonnes and take to 20
    top20 = top20.nlargest(20, "Tonnes")

    # Creates empty canvas
    fig = go.Figure()

    # Adds Horizontal Bar Charts. trace defines the type of chart (Bar, Line Pie)
    fig.add_trace(go.Bar
                  (x=top20["Tonnes"],
                   y=top20["Country"],
                   orientation="h",
                   marker=dict(color=top20["Tonnes"], colorscale="Viridis", showscale=True),
                   hovertemplate="%{y}: %{x:.0f} tonnes<extra></extra>"
))

# Add titles and sizing
    fig.update_layout(
        title="Top 20 Central Bank Gold Holdings (Tonnes)",
        xaxis_title="Gold Holdings (Tonnes)",
        yaxis_title="Country",
        height=800,
)
    return fig


# if __name__ == "__main__":
    # reserve_data = fetch_reserve_data()
    # fig = plot_top_holdings(reserve_data)
    # fig.show()


# Reserve Data

# Reserve Changes over time
def fetch_changes_data():
    gold_changes = pd.read_excel("gold_changes.xlsx", sheet_name="Monthly", skiprows=7)

    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.width', None)

    # print(gold_changes.columns[:10])
    # print(gold_changes)

    # Drop columns we don't need , duplicate country column
    gold_changes = gold_changes.drop(columns=["Country"])

    # Change specific column came
    gold_changes = gold_changes.rename(columns={"Country Lookup Column": "Country"})

    # Set that country column to index
    gold_changes = gold_changes.set_index("Country")

    # Drop columns we don't need , comments
    gold_changes = gold_changes.drop(columns=["Comments"])

    # Total for each country
    total = gold_changes.sum(axis=1)

    # Drop countries which never bought or sold anything
    total = total[total !=0].dropna()

    # Sort by biggest buyers
    total = total.sort_values(ascending=False)

    # print(total)
    return total
total = fetch_changes_data()

# Chart Plotting

def plot_net_purchases(total):
    top20 = total.head(20)

    fig = go.Figure()

    fig.add_trace(go.Bar(
                        x=top20.values,
                        y=top20.index,
                        orientation="h",
                        marker=dict(color=top20, colorscale="Inferno", showscale=True),
                        hovertemplate="%{y}: %{x:.0f} tonnes<extra></extra>"
    ))

    # Add titles and sizing
    fig.update_layout(
            title="Top 20 Central Bank Gold Buyers (2002-Present)",
            xaxis_title="Gold Holdings (Tonnes)",
            yaxis_title="",
            height=800,
            margin=dict(l=250)
    )
    return fig

fig = plot_net_purchases(total)
fig.show()




















