import streamlit as st
import datetime
from gold_silver_functions import calculate_gold, calculate_silver, generate_report
from gsr import fetch_data, analyse_gsr, plot_gsr, plot_gsr_plotly
from real_rates import fetch_us_data, analyze_us_rates, plot_us_rates, fetch_ind_data, analyze_ind_rates, plot_ind_rates
from central_bank_gold import fetch_reserve_data, plot_top_holdings
from central_bank_gold import fetch_changes_data, plot_net_purchases


st.set_page_config(page_title="Metals Macro Intelligence Platform", layout='wide')

st.title("Metals Macro Intelligence Platform")
st.write("Real-time analysis of precious metals and Micro Economic-Indicators")

st.divider()

st.header("⭐ Precious Metals Fair Value Calculator")
st.write("Enter current market prices to Calculate fair value of Gold and Silver")

name = st.text_input("Your Name").title()
gold_price = st.number_input("Current Gold Price (INR/gm)", min_value=0.0, value=None, placeholder="0.00", format="%.2f")
silver_price = st.number_input("Current Silver Price (INR/gm)", min_value=0.0, value=None, placeholder="0.00", format="%.2f")

today = datetime.date.today().strftime("%d-%B-%Y")
st.caption(f"Fair value calculated as of {today} | Data: World Gold Council & FRED, Feb 2026")

if st.button("Calculate Fair Value"):
    if not name or gold_price is None or silver_price is None:
        st.error("Please fill in all the fields to Calculate")
    else:
        gold_result = calculate_gold(gold_price)
        silver_result = calculate_silver(gold_result["fair_value"], silver_price)

        st.subheader("Gold's Fair Value ")
        col1, col2, col3 = st.columns(3)
        col1.metric("Fair Value", f"Rs.{gold_result['fair_value']:,.2f}")
        col2.metric("Market Price", f"Rs.{gold_price:,.2f}")
        col3.metric("Gap", f"{gold_result['pct_gap']:+.2f}%")

        if gold_result["pct_gap"] > 10:
            st.error("🔴 Gold is OverValued")
        elif gold_result["pct_gap"] < -10:
            st.success("🟢 Gold is UnderValued")
        else:
            st.warning("🟡 Gold is Fairly Valued")

        st.subheader("Silver's Fair Value")
        col4, col5, col6 = st.columns(3)
        col4.metric("Fair Value", f"Rs.{silver_result['fair_value']:,.2f}")
        col5.metric("Market Price", f"Rs.{silver_price:,.2f}")
        col6.metric("Gap", f"{silver_result['pct_gap']:+.2f}%")

        if silver_result["pct_gap"] > 10:
            st.error("🔴 Silver is OverValued")
        elif silver_result["pct_gap"] < -10:
            st.success("🟢 Silver is UnderValued")
        else:
            st.warning("🟡 Silver is Fairly Valued")

        report = generate_report(name, gold_price, silver_price, gold_result, silver_result)
        st.download_button("📥 Download Report", data=report, file_name=f"{name}_Valuation_Report.txt")

    st.divider()

st.header("Gold Silver Ratio Analyzer")
st.write("Analyze 25 years of Gold-Silver Ratio data identifies Buy/Sell signals")

if st.button("Run GSR Analysis"):
    with st.spinner("fetching data...."):
        gsr = fetch_data()
        analyse_gsr(gsr)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric( "Current Gold Silver Ratio", f"{gsr.iloc[-1]:.2f}")
    col2.metric( "Average Gold Silver Ratio", f"{gsr.mean() :.2f}")
    col3.metric( 'Maximum Gold silver Ratio' , f'{gsr.max():.2f}')
    col4.metric( 'Minimum Gold Silver Ratio', f'{gsr.min():.2f}')
    col5.metric('Maximum Gold Silver Ratio on',f'{gsr.idxmax().date()}')
    col6.metric( 'Minimum Gold Silver Ratio on', f'{gsr.idxmin().date()}')

    current_gsr = gsr.iloc[-1]
    if current_gsr > 80:
        st.error("🔴 GSR Too High - Strong Buy Signal for Silver")
    elif current_gsr < 55:
        st.success("🟢 GSR Too Low - Strong Sell Signal for Silver")
    else:
        st.warning("🟡 GSR in Normal Range - Hold")


    # fig = plot_gsr(gsr)
    # st.pyplot(fig)

    fig = plot_gsr_plotly(gsr)
    st.plotly_chart(fig, use_container_width=True, config={"scrollZoom": True})

st.divider()

st.header("📈 Real Interest Rates")
st.write("US and India real interest rates — key Macro driver for Gold Prices")

if st.button("Load Real Interest Rates"):
    with st.spinner("Fetching data from FRED..."):
        us_data = fetch_us_data()
        us_stats = analyze_us_rates(us_data)
        us_fig = plot_us_rates(us_data)

        ind_data = fetch_ind_data()
        ind_stats = analyze_ind_rates(ind_data)
        ind_fig = plot_ind_rates(ind_data)

    st.subheader("🇺🇸 United States")
    col1, col2, col3 = st.columns(3)
    col1.metric("Current Real Rate", f"{us_stats['current']:.2f}%")
    col2.metric("Historic Average", f"{us_stats['mean']:.2f}%")
    col3.metric("Negative Rate Days", us_stats['negative'])
    st.write(us_stats['signal'])
    st.plotly_chart(us_fig)

    st.subheader("🇮🇳 India")
    col4, col5, col6 = st.columns(3)
    col4.metric("Current Real Rate", f"{ind_stats['current']:.2f}%")
    col5.metric("Historic Average", f"{ind_stats['mean']:.2f}%")
    col6.metric("Negative Rate Days", ind_stats['negative'])
    st.write(ind_stats['signal'])
    st.plotly_chart(ind_fig)

st.divider()

st.header("Central Bank Gold Accumulation Dashboard")
st.write("Global central bank gold holdings")

if st.button("Run Central Bank Gold Accumulation Analysis"):
    with st.spinner("retrieving data...."):

        reserve_data = fetch_reserve_data()
        fig = plot_top_holdings(reserve_data)
        st.plotly_chart(fig, use_container_width=True)


st.divider()

st.header("Central Bank Net Gold Purchases (2002-Present)")
st.write("Central Banks Ranked By Gold Bought")

if st.button("Run Central Banks By Gold Bought"):
    with st.spinner("retrieving data...."):

        net_purchases = fetch_changes_data()
        fig = plot_net_purchases(net_purchases)
        st.plotly_chart(fig, use_container_width=True)




