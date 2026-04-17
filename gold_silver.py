#Gold & Silver Fair Value Calculation Project.
import datetime
print("=" * 55)
print(" " * 6, "Precious Metals fair Value Calculator ")
print("=" * 55)

name = input("Enter your name: ").capitalize()
print(f"Welcome {name}, Generating your valuation report....")
print("Data Reference: World Gold Council & FRED, Feb 2026")
print("-" * 55)

# Taking Live Prices from the User
gold_price = float(input("Enter current Gold price.(inr/gm): ").replace(",",""))
silver_price = float(input("Enter current Silver price.(inr/gm): ").replace(",",""))

#BACKGROUND DATA (Real World Values)

# Total Gold Ever Mined and Brought Above the Ground( in Tonnes)
# Source: World Gold Council, Dec 2025 estimate
total_gold_mined = 219_890

# Gold Sitting underground, not yet Mined (Not used in Calculation)
total_gold_reserves = 50_000

# Conversion Method used - 1 tonne = 32,150.7 troy ounces
troy_oz_per_tonne = 32150.7

# Converting Total Gold mined from tonnes to troy ounces
# 219,865 x 32,150.7 = approximately 7.07 Billion troy oz
total_gold_troy_oz = total_gold_mined * troy_oz_per_tonne

# US M2 Money Supply - Total Money circulating in the US Economy ( in USD Billion)
# This Represents how much the paper money the US has printed
us_m2_usd_bn = 22_411

# EU M2 Money supply - Taken at 50% of total as not all EU money directly competes with gold globally
eu_m2_usd_bn = 9_603

# Current USD to INR rate , We need this to convert the fair value from USD to INR
usd_to_inr = 94.5

# 1 troy ounce = 31,1035 grams
# We need this to convert prices per troy oz to prices per gram
grams_per_troy_oz = 31.1035

# Current Gold Silver Ratio - how many ounces of silver = 1 ounce of gold
# Right now in the market, 1 Gold = 47 Silver
current_gsr = 47

# Historical average GSR used for fair value calculation
# Based on long term historical average across Roman Empire , Medieval Europe, Modern era
fair_gsr = 60


# ============ Gold Valuation Engine ============
# Calculate fair value per troy oz in USD using M2
gold_fair_value_usd_us = (us_m2_usd_bn * 1_000_000_000) / total_gold_troy_oz
gold_fair_value_usd_eu = (eu_m2_usd_bn * 1_000_000_000) / total_gold_troy_oz

# Average of both to get the final value in USD per troy oz
gold_fair_value_usd_final = gold_fair_value_usd_us + gold_fair_value_usd_eu

# Convert USD per troy oz - INR per Gram
gold_fair_value_inr_per_gram = (gold_fair_value_usd_final / grams_per_troy_oz) * usd_to_inr


# ============ Gold Valuation Report ============
print("=" * 55)
print(" " * 6, "Gold Valuation Report ")
print("=" * 55)


print(f"\nTotal Gold Ever Mined: {total_gold_mined:,} tonnes")
print(f"Total Gold Still in Ground: {total_gold_reserves:,} tonnes")
print(f"Note: Underground reserves not used in valuation")
print(f"Total Gold in Troy Ounces: {total_gold_troy_oz:,.0f} troy oz")

print(f"\nUS M2 Money Supply: ${us_m2_usd_bn:,} Billion")
print(f"EU M2 Money Supply (50%): ${eu_m2_usd_bn:,} Billion")

# Fair value using only US Dollar - What gold would be worth against the US dollar alone
# gold_fair_usd_us is in USD/troy oz → dividing by grams_per_troy_oz
# gives USD/gram → multiplying by usd_to_inr gives INR/gram
print(f"\nFair Value US M2 basis: Rs.{gold_fair_value_usd_us * usd_to_inr / grams_per_troy_oz:,.2f} per gm")

# Same calculation but for EU money supply only ( use :,.2f for 2 decimal answer)
print(f"Fair Value EU M2 basis: Rs.{gold_fair_value_usd_eu * usd_to_inr / grams_per_troy_oz:,.2f} per gm")
print("-" * 55)
# Combined fair Value ( use :,.2f for 2 decimal answer)
print(f"\nFair Value of Gold: Rs.{gold_fair_value_inr_per_gram:,.2f} per gm")

# Your Input price for comparison ( use :,.2f for 2 decimal answer)
print(f"Current Gold Price: Rs.{gold_price:,.2f} per gm")

# Difference in price in Rs
print(f"Difference: Rs.{gold_price - gold_fair_value_inr_per_gram:+,.2f} per gm")
print("-" * 55)


# ============== The Verdict ( OverValued / UnderValued / Fairly Valued) =================
# We will calculate the percentage difference between market price and fair value
# Formula used to find percentage Gap = ((market price - fair value) / fair value) * 100
gold_pct_gap = ((gold_price - gold_fair_value_inr_per_gram) / gold_fair_value_inr_per_gram) * 100

if gold_pct_gap > 10:
    print(f" Gold Is OverValued by {gold_pct_gap:,.2f}% ")
elif gold_pct_gap < -10:
    print(f" Gold Is UnderValued by {gold_pct_gap:,.2f}% ")
else :
    print(f" Gold Is fairly Valued Within {gold_pct_gap:,.2f}% ")




# ============ Silver Valuation Engine ============
# Formula used : Fair price of silver = (fair price of gold ÷ fair gsr)
silver_fair_value = gold_fair_value_inr_per_gram / fair_gsr


# ============ Silver Valuation Report ============
print("\n" + "=" * 55)
print(" " *14, " SILVER VALUATION REPORT")
print("=" * 55)

print(f" Current Gold to Silver ratio: {current_gsr}")
print(" Historical Gold to Silver Ratio( Roman Empire, Ancient Greece, Ancient India): 8-12")
print(" After the shift from Gold Standard (1971): 17 -100")
print(" 21st Century GSR: 98-125")
print(f" Fair Gold to Silver Ratio, averaging all: {fair_gsr}")
print("-" * 55)

print (f" Fair value of Silver: Rs. {silver_fair_value:,.2f} per gm")
print(f" Current Silver Price: Rs.{silver_price:,.2f} per gm")
# Difference in price in Rs
print(f" Difference: Rs.{silver_price - silver_fair_value:+,.2f} per gm")
print("-" * 55)


# ============== The Verdict ( OverValued / UnderValued / Fairly Valued) =================
# We will calculate the percentage difference between market price and fair value
# Formula used to find Percentage Gap = ((market price - fair value) / fair value) * 100
silver_pct_gap = ((silver_price - silver_fair_value) / silver_fair_value) * 100

if silver_pct_gap > 10:
    print(f"Silver Is OverValued by {silver_pct_gap:,.2f}%")
elif silver_pct_gap < -10:
    print(f"Silver Is UnderValued by {silver_pct_gap:,.2f}%")
else:
    print(f" Silver Is fairly Valued Within {silver_pct_gap:,.2f}% ")





# ================ Save Report to File =====================
today = datetime.date.today() .strftime("%d-%B-%Y")
filename = f"{name}_Valuation_Report_{today}.txt"

with open(filename, "w",encoding="utf-8") as file:
    file.write("=" * 55 + "\n")
    file.write(" " * 6 + "Precious Metals fair Value Calculator \n")
    file.write("=" * 55 +"\n")
    
    file.write(f"Welcome {name}, Generating your valuation report....\n")
    file.write("Data Reference: World Gold Council & FRED, Feb 2026\n")
    
    file.write("=" * 55 +"\n")
    file.write(" " * 14 + "Gold Valuation Report \n")
    file.write("=" * 55 +"\n")
    
    file.write(f" Total Gold Ever Mined: {total_gold_mined:,} tonnes\n")
    file.write(f" Total Gold Still in Ground: {total_gold_reserves:,} tonnes\n")
    file.write(f" Note: Underground reserves not used in valuation\n")
    file.write(f" Total Gold in Troy Ounces: {total_gold_troy_oz:,.0f} troy oz\n")
    
    file.write(f" US M2 Money Supply: ${us_m2_usd_bn:,} Billion\n")
    file.write(f" EU M2 Money Supply (50%): ${eu_m2_usd_bn:,} Billion\n")
    
    file.write(f" Fair Value US M2 basis: Rs.{gold_fair_value_usd_us * usd_to_inr / grams_per_troy_oz:,.2f} per gm\n")
    file.write(f" Fair Value EU M2 basis: Rs.{gold_fair_value_usd_eu * usd_to_inr / grams_per_troy_oz:,.2f} per gm\n")
    file.write("-" * 55 + "\n")
    file.write(f" Fair Value of Gold: Rs.{gold_fair_value_inr_per_gram:,.2f} per gm\n")
    file.write(f" Current Gold Price: Rs.{gold_price:,.2f} per gm \n")
    file.write(f" Difference        : Rs.{gold_price - gold_fair_value_inr_per_gram:+,.2f} per gm\n")
    file.write("-" * 55 + "\n")
    
    if gold_pct_gap > 10:
        file.write(f" Gold Is OverValued by {gold_pct_gap:,.2f}% \n")
    elif gold_pct_gap < -10:
        file.write(f" Gold Is UnderValued by {gold_pct_gap:,.2f}% \n")
    else :
        file.write(f" Gold Is fairly Valued Within {gold_pct_gap:,.2f}% \n")
    file.write("-" * 55 + "\n")

    file.write("\n")
    file.write("\n")
    file.write("=" * 55 + "\n")
    file.write(" " * 13 + " SILVER VALUATION REPORT \n")
    file.write("=" * 55 + "\n")

    file.write(f" Current Gold to Silver ratio: {current_gsr} \n")
    file.write(" Historical Gold to Silver Ratio( Roman Empire, Ancient Greece, Ancient India): 8-12 \n")
    file.write(" After the shift from Gold Standard (1971): 17 -100 \n")
    file.write(" 21st Century GSR: 98-125 \n")
    file.write(f" Fair Gold to Silver Ratio, averaging all: {fair_gsr} \n")
    file.write("-" * 55 + "\n")

    file.write(f" Fair value of Silver: Rs.{silver_fair_value:,.2f} per gm \n")
    file.write(f" Current Silver Price: Rs.{silver_price:,.2f} per gm \n")
    file.write(f" Difference          : Rs.{silver_price - silver_fair_value:+,.2f} per gm \n")
    file.write("-" * 55 +"\n")

    if silver_pct_gap > 10:
        file.write(f" Silver Is OverValued by {silver_pct_gap:,.2f}% \n")
    elif silver_pct_gap < -10:
        file.write(f" Silver Is UnderValued by {silver_pct_gap:,.2f}% \n")
    else:
        file.write(f" Silver Is fairly Valued Within {silver_pct_gap:,.2f}% \n")

    file.write("-" * 55 + "\n")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("================== END OF REPORT =================== \n")


print("-" * 55)
print(f"Report saved as: {filename}")
print("-" * 55)