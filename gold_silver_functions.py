import datetime

# =================== Constants =====================
total_gold_mined = 219_890
total_gold_reserves = 50_000
troy_oz_per_tonne = 32150.7
total_gold_troy_oz = total_gold_mined * troy_oz_per_tonne
us_m2_usd_bn = 22_411
eu_m2_usd_bn = 9_603
usd_to_inr = 94.5
grams_per_troy_oz = 31.1035
current_gsr = 47
fair_gsr = 60

# ===================== Function 1 ==========================
# Calculates fair value of gold and % change and returns both
def calculate_gold(gold_price):
    gold_fair_value_usd_us = (us_m2_usd_bn * 1_000_000_000) / total_gold_troy_oz
    gold_fair_value_usd_eu = (eu_m2_usd_bn * 1_000_000_000) / total_gold_troy_oz
    gold_fair_value_usd_final = gold_fair_value_usd_us + gold_fair_value_usd_eu
    gold_fair_value_inr_per_gram = (gold_fair_value_usd_final / grams_per_troy_oz) * usd_to_inr
    gold_pct_gap = ((gold_price - gold_fair_value_inr_per_gram) / gold_fair_value_inr_per_gram) * 100
    return {
        "fair_value": gold_fair_value_inr_per_gram,
        "pct_gap": gold_pct_gap
    }

# ===================== Function 2 ==========================
# Calculates fair value of silver and % change and returns both
def calculate_silver(gold_fair_value, silver_price):
    silver_fair_value = gold_fair_value / fair_gsr
    silver_pct_gap = ((silver_price - silver_fair_value) / silver_fair_value) * 100
    return {
        "fair_value": silver_fair_value,
        "pct_gap": silver_pct_gap
    }

# =================== Function 3 ========================
# Generates a text report named after the user and saves it
def generate_report(name, gold_price, silver_price, gold_result, silver_result):
    today = datetime.date.today().strftime("%d-%B-%Y")
    report = ""
    report += "=" * 55 + "\n"
    report += "      Precious Metals Fair Value Calculator\n"
    report += "=" * 55 + "\n"
    report += f"Report for: {name}\n"
    report += f"Date: {today}\n"
    report += "\n"
    report += "=" * 55 + "\n"
    report += "              GOLD VALUATION REPORT\n"
    report += "=" * 55 + "\n"
    report += f" Fair Value of Gold : Rs.{gold_result['fair_value']:,.2f} per gm\n"
    report += f" Current Gold Price : Rs.{gold_price:,.2f} per gm\n"
    report += f" Difference         : Rs.{gold_price - gold_result['fair_value']:+,.2f} per gm\n"
    report += "-" * 55 + "\n"
    if gold_result["pct_gap"] > 10:
        report += f" Gold Is OverValued by {gold_result['pct_gap']:,.2f}%\n"
    elif gold_result["pct_gap"] < -10:
        report += f" Gold Is UnderValued by {gold_result['pct_gap']:,.2f}%\n"
    else:
        report += f" Gold Is Fairly Valued Within {gold_result['pct_gap']:,.2f}%\n"
    report += "\n"
    report += "=" * 55 + "\n"
    report += "             SILVER VALUATION REPORT\n"
    report += "=" * 55 + "\n"
    report += f" Fair Value of Silver : Rs.{silver_result['fair_value']:,.2f} per gm\n"
    report += f" Current Silver Price : Rs.{silver_price:,.2f} per gm\n"
    report += f" Difference           : Rs.{silver_price - silver_result['fair_value']:+,.2f} per gm\n"
    report += "-" * 55 + "\n"
    if silver_result["pct_gap"] > 10:
        report += f" Silver Is OverValued by {silver_result['pct_gap']:,.2f}%\n"
    elif silver_result["pct_gap"] < -10:
        report += f" Silver Is UnderValued by {silver_result['pct_gap']:,.2f}%\n"
    else:
        report += f" Silver Is Fairly Valued Within {silver_result['pct_gap']:,.2f}%\n"
    report += "\n" + "=" * 55 + "\n"
    report += "               END OF REPORT\n"
    report += "=" * 55 + "\n"
    return report