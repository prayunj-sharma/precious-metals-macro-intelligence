import streamlit as st
from matplotlib import pyplot as plt

from gsr import fetch_data, analyse_gsr, plot_gsr, plot_gsr_plotly
# from metals_valuation.gsr import plot_gsr_plotly
from real_rates import fetch_us_data, analyze_us_rates, plot_us_rates


st.set_page_config(page_title="Metals Macro Intelligence Platform", layout='wide')

st.title("Metals Macro Intelligence Platform")
st.write("Real-time analysis of precious metals and Micro Economic-Indicators")

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

st.header("Central Bank Gold Accumulation Dashboard")
st.write("Global central bank gold holdings")

if st.button("Run Central Bank Gold Accumulation Analysis"):
    with st.spinner("retrieving data...."):
        from central_bank_gold import fetch_reserve_data, plot_top_holdings

        reserve_data = fetch_reserve_data()
        fig = plot_top_holdings(reserve_data)
        st.plotly_chart(fig, use_container_width=True)


