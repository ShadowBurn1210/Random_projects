import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.dates import YearLocator, DateFormatter

#
# # Real GDP Growth (Year-on-Year %)
# years_gdp = ['2019', '2020', '2021', '2022', '2023', '2024', '2025']
# gdp_growth = [1.9, -2.4, 4.7, 3.7, 1.8, 1.3, 1.8]  # In %
#
# plt.figure(figsize=(10, 6))
# plt.plot(years_gdp, gdp_growth, marker='o', linestyle='-', color='b')
# plt.title('Australia Real GDP Growth (Year-on-Year %)')
# plt.xlabel('Year')
# plt.ylabel('GDP Growth (%)')
# plt.grid(True)
# plt.show()
#
# # Headline Inflation (Year-on-Year %)
# years_inflation = ['2019', '2020', '2021', '2022', '2023', '2024', '2025']
# inflation_rates = [1.6, 0.9, 3.5, 6.6, 5.5, 2.8, 2.3]  # In %
#
# plt.figure(figsize=(10, 6))
# plt.plot(years_inflation, inflation_rates, label='Australia', marker='o')
# plt.title('Australia Headline Inflation (Year-on-Year %)')
# plt.xlabel('Year')
# plt.ylabel('Inflation (%)')
# plt.legend()
# plt.grid(True)
# plt.show()
#
# # Official Policy Rates (%)
# dates = pd.date_range(start='2019-01-01', periods=84, freq='ME')  # Monthly data from 2019 to 2025
# policy_rates = [
#     1.50, 1.50, 1.25, 1.25, 1.25, 1.25, 1.00, 1.00, 0.75, 0.75, 0.75, 0.75,  # 2019
#     0.75, 0.50, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.10, 0.10,  # 2020
#     0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10,  # 2021
#     0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.35, 0.60, 0.85, 1.10, 1.35,  # 2022
#     1.60, 1.85, 2.10, 2.35, 2.60, 2.85, 3.10, 3.35, 3.60, 3.85, 4.10, 4.10,  # 2023
#     4.10, 4.10, 4.10, 4.10, 4.10, 4.10, 4.10, 4.10, 4.10, 4.10, 4.10, 4.10,  # 2024
#     4.10, 4.10, 4.10, 4.10, 4.10, 4.10, 4.10, 4.10, 4.10, 4.10, 4.10, 4.10   # 2025
# ]  # RBA cash rate
#
# plt.figure(figsize=(10, 6))
# plt.plot(dates, policy_rates, label='Australia', marker='o')
# plt.title('Australia Official Policy Rates (%) (2019-2025)')
# plt.xlabel('Date')
# plt.ylabel('Interest Rate (%)')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
#
# # Federal Government Fiscal Balance (% of GDP)
# years_fiscal = ['2019', '2020', '2021', '2022', '2023', '2024', '2025']
# deficit = [-0.5, -4.3, -6.4, -1.4, 0.9, 0.6, -0.5]  # % of GDP
#
# plt.figure(figsize=(10, 6))
# plt.plot(years_fiscal, deficit, marker='o', color='r')
# # plt.fill_between(years_fiscal, deficit, 0, where=np.array(deficit) < 0, color='red', alpha=0.3)
# plt.title('Australia Federal Government Fiscal Balance (% of GDP)')
# plt.xlabel('Year')
# plt.ylabel('Fiscal Balance (%)')
# plt.grid(True)
# plt.show()
#
#
# # Data
# years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
# gdp_growth = [2.8, 1.9, -2.4, 4.7, 3.7, 1.8, 1.3, 1.8]
# inflation_rates = [1.9, 1.6, 0.9, 3.5, 6.6, 5.5, 2.8, 2.3]
# fiscal_balance = [0.1, -0.5, -4.3, -6.4, -1.4, 0.9, 0.6, -0.5]
# policy_rates = [1.50, 1.50, 0.10, 0.10, 1.35, 3.85, 4.10, 4.10]  # Using yearly data
#
# # # First figure: GDP Growth and Inflation
# # fig, ax1 = plt.subplots(figsize=(12, 6))
# # ax1.set_xlabel('Year')
# # ax1.set_ylabel('Percentage (%)', color='b')
# # ax1.plot(years, gdp_growth, marker='o', linestyle='-', color='b', label='Real GDP Growth')
# # ax1.plot(years, inflation_rates, marker='s', linestyle='--', color='g', label='Inflation Rate')
# # ax1.tick_params(axis='y', labelcolor='b')
# # ax1.grid(True)
# # ax1.legend(loc='upper left')
# # plt.title('Australia GDP Growth and Inflation (2018-2025)')
# # plt.show()
# #
# # Second figure: Policy Rates and Fiscal Balance
# fig, ax2 = plt.subplots(figsize=(12, 6))
# ax2.set_xlabel('Year')
# ax2.set_ylabel('Policy Rate / Fiscal Balance (% of GDP)', color='r')
# ax2.plot(years, policy_rates, marker='^', linestyle='-', color='r', label='Policy Rate (RBA)')
# ax2.plot(years, fiscal_balance, marker='d', linestyle=':', color='orange', label='Fiscal Balance')
# ax2.tick_params(axis='y', labelcolor='r')
# ax2.grid(True)
# ax2.legend(loc='upper left')
# plt.title('Australia Policy Rate and Fiscal Balance (2018-2025)')
# plt.show()

# # Data
# years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
#
# # Unemployment Rates (%)
# aus_unemployment = [5.3, 5.2, 6.9, 5.1, 3.8, 3.7, 4.1, 4.2]
# us_unemployment = [3.9, 3.7, 8.1, 5.4, 3.6, 3.5, 3.8, 4.0]
# eu_unemployment = [6.8, 6.7, 7.5, 7.0, 6.2, 6.0, 6.3, 6.4]
#
# # Inflation Rates (%)
# aus_inflation = [1.9, 1.6, 0.9, 3.5, 6.6, 5.5, 2.8, 2.3]
# us_inflation = [2.4, 1.8, 1.2, 4.7, 8.0, 4.9, 3.2, 2.5]
# eu_inflation = [1.7, 1.4, 0.3, 2.6, 8.4, 5.3, 3.0, 2.7]
#
# # First Figure: Unemployment Comparison
# fig, ax1 = plt.subplots(figsize=(12, 6))
# ax1.set_xlabel('Year')
# ax1.set_ylabel('Unemployment Rate (%)')
# ax1.plot(years, aus_unemployment, marker='o', linestyle='-', color='b', label='Australia')
# ax1.plot(years, us_unemployment, marker='s', linestyle='--', color='g', label='USA')
# ax1.plot(years, eu_unemployment, marker='d', linestyle=':', color='r', label='EU')
# ax1.legend(loc='upper left')
# ax1.grid(True)
# plt.title('Unemployment Rate Comparison (2018-2025)')
# plt.show()
#
# # Second Figure: Inflation Comparison
# fig, ax2 = plt.subplots(figsize=(12, 6))
# ax2.set_xlabel('Year')
# ax2.set_ylabel('Inflation Rate (%)')
# ax2.plot(years, aus_inflation, marker='o', linestyle='-', color='b', label='Australia')
# ax2.plot(years, us_inflation, marker='s', linestyle='--', color='g', label='USA')
# ax2.plot(years, eu_inflation, marker='d', linestyle=':', color='r', label='EU')
# ax2.legend(loc='upper left')
# ax2.grid(True)
# plt.title('Inflation Rate Comparison (2018-2025)')
# plt.show()
# Generate monthly data from 2018 to 2025
dates = pd.date_range(start='2018-01', periods=78, freq='ME')

# Policy Rates (96 months)
policy_rates_monthly = [
    # 2018
    1.50, 1.50, 1.50, 1.50, 1.50, 1.50, 1.50, 1.50, 1.50, 1.50, 1.50, 1.50,
    # 2019
    1.50, 1.50, 1.25, 1.25, 1.25, 1.25, 1.00, 1.00, 0.75, 0.75, 0.75, 0.75,
    # 2020
    0.75, 0.50, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.10, 0.10,
    # 2021
    0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10,
    # 2022
    0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.35, 0.60, 0.85, 1.10, 1.35,
    # 2023
    1.60, 1.85, 2.10, 2.35, 2.60, 2.85, 3.10, 3.35, 3.60, 3.85, 4.10, 4.10,
    # 2024-2025
    *[4.10]*6
]

# Simplified fiscal balance data (4 key points)
fiscal_points = {
    '2018-01': 0.1,
    '2020-01': -4.3,
    '2022-01': -1.4,
    '2024-01': -0.5
}

# Create interpolation
fiscal_dates = pd.to_datetime(list(fiscal_points.keys()))
fiscal_values = list(fiscal_points.values())

x = (fiscal_dates - dates[0]).days.to_numpy()
x_new = (dates - dates[0]).days.to_numpy()
fiscal_balance_monthly = np.interp(x_new, x, fiscal_values)
# Plotting
fig, ax = plt.subplots(figsize=(12, 6))

# Plot both series
ax.plot(dates, policy_rates_monthly, marker='o', linestyle='-', color='#1f77b4', markersize=5, label='Policy Rate (RBA)')
ax.plot(dates, fiscal_balance_monthly, linestyle='--', color='#ff7f0e', linewidth=2, label='Fiscal Balance')

# Set explicit axis limits to remove empty space
ax.set_xlim([dates[0], dates[-1]])  # Critical fix to eliminate 2026
ax.set_ylim(-6, 5)

# Formatting
ax.xaxis.set_major_locator(YearLocator())
ax.xaxis.set_major_formatter(DateFormatter('%Y'))
plt.xticks(rotation=45)
plt.title('Australia Policy Rate and Fiscal Balance (2018-2025)')

ax.set_xlabel('Year')
ax.set_ylabel('Policy Rate / Fiscal Balance (% of GDP)')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
