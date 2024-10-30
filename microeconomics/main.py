import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress

# Path to the Excel file
excel_file = r'C:\Users\Admin\PycharmProjects\RandomProjects\Choose_the_Price2024-09-20_02_21_07.xlsx'


def read_excel():
    """Reads the Excel file and returns a DataFrame."""
    print("Reading excel file")
    try:
        df = pd.read_excel(excel_file)
    except FileNotFoundError:
        print("File not found")
        return None
    return df


def get_ending_price(user_id, df):
    """Returns the ending price based on user_id from the DataFrame."""
    user_row = df[df.iloc[:, 9] == user_id]  # The 10th column has index 9

    if user_row.empty:
        return None  # Handle the case where user_id is not found

    # Extract relevant column values
    fifth_col_value = user_row.iloc[0, 4]
    sixth_col_value = user_row.iloc[0, 5]
    seventh_col_value = user_row.iloc[0, 6]

    # Check if any of these columns contain "Buy"
    if "Buy" in str(fifth_col_value):
        return str(fifth_col_value).split(",")[0], 1
    elif "Buy" in str(sixth_col_value):
        return str(sixth_col_value).split(",")[0], 2
    elif "Buy now" in str(seventh_col_value):
        return str(seventh_col_value).split(",")[0], 3

    # If no "Buy" or "Buy now" found, return the value in the 8th column
    return user_row.iloc[0, 7], 4


def organize_file(df):
    """Organizes data from the DataFrame and exports to Excel."""
    results_dict = {}

    # Extract relevant columns
    forth_col = df.iloc[:, 3]
    ninth_col = df.iloc[:, 9]

    # Loop through each chosen_tires and use the 9th column as the key
    for chosen_tires, user_id in zip(forth_col, ninth_col):
        # Ensure that `results_dict[user_id]` is a dictionary before assigning values
        if user_id not in results_dict:
            results_dict[user_id] = {}  # Initialize an empty dictionary for the user

        if isinstance(chosen_tires, str):  # Ensure chosen_tires is a string
            results_dict[user_id]["starting_price"] = chosen_tires[-7:-1]
            ending_price, week = get_ending_price(user_id, df)
            results_dict[user_id]["ending_price"] = ending_price
            results_dict[user_id]["week"] = week
            results_dict[user_id]["difference_in_price"] = round(
                float(results_dict[user_id]["ending_price"]) - float(results_dict[user_id]["starting_price"]), 2)
            results_dict[user_id]["difference_in_price_procentile"] = round(
                (float(results_dict[user_id]["ending_price"]) - float(results_dict[user_id]["starting_price"])) / float(
                    results_dict[user_id]["starting_price"]) * 100, 2)

    # Convert the results_dict to a DataFrame
    organized_df = pd.DataFrame.from_dict(results_dict, orient='index')
    #
    # # Export to Excel
    # organized_excel_file = 'organized_data.xlsx'  # Specify the filename
    # organized_df.to_excel(organized_excel_file)

    return organized_df


def calculated_elasticity(organized_excel):
    quantity_demanded = {i: 0 for i in range(11, -12, -1)}
    elasticity_graph = {}
    market_demand = 30
    for value in organized_excel.iloc[:, 4]:
        for key in quantity_demanded:
            if value > key:
                quantity_demanded[key] += 1

    elasticities = {}
    price_changes = list(range(11, -12, -1))

    print(market_demand)
    print(quantity_demanded)
    for price_change in price_changes:
        new_demand = quantity_demanded[price_change]
        change_in_quantity = round((new_demand - market_demand) / market_demand * 100, 2)

        print(
            f"quantity demanded at the price: {new_demand}, "
            f"raw change: {new_demand - market_demand} "

            f"change_in_quantity: {change_in_quantity}%, "
            f"price_change: {price_change}%"
        )

        # TODO: try midpoint method
        if price_change == 0 or price_change == -1:
            continue
        elasticity = abs(change_in_quantity) / abs(price_change)
        elasticities[f'PED_{price_change}'] = elasticity

        elasticity_graph[price_change] = round(elasticity, 2)
    for key, value in elasticities.items():
        print(f"{key}: {round(value, 2)}")

    # get the average elasticity
    average_elasticity = sum(elasticities.values()) / len(elasticities)
    print(elasticity_graph)
    return elasticity_graph, quantity_demanded, round(average_elasticity, 2)


def plot_graphs(elasticity_graph, quantity_demanded, average_elasticity):
    """Plots graphs for elasticity and quantity demanded and exports them as PNG files."""

    # Plot quantity demanded
    fig1, ax1 = plt.subplots()
    ax1.set_xlabel('Price Change From Initial Price (%)')
    ax1.set_ylabel('Quantity Demanded', color='tab:blue')
    ax1.plot(quantity_demanded.keys(), quantity_demanded.values(), color='tab:blue', label='Quantity Demanded')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    plt.title('Quantity Demanded vs. Price Change')

    # Linear regression for quantity demanded
    slope, intercept, r_value, p_value, std_err = linregress(list(quantity_demanded.keys()), list(quantity_demanded.values()))
    ax1.plot(quantity_demanded.keys(), [slope * x + intercept for x in quantity_demanded.keys()], color='tab:orange', linestyle='--', label=f'Linear Regression (slope={slope:.2f})')
    ax1.legend()

    fig1.tight_layout()
    # Add equilibrium point A with values in the legend
    ax1.scatter(0, quantity_demanded[0], color='tab:purple', label='A (0,29)')
    ax1.legend()

    plt.savefig('quantity_demanded.png')
    plt.close(fig1)

    # Plot elasticity
    fig2, ax2 = plt.subplots()
    ax2.set_xlabel('Price Change From Initial Price (%)')
    ax2.set_ylabel('Elasticity', color='tab:red')
    ax2.set_ylim(-15, 15)
    ax2.plot(elasticity_graph.keys(), elasticity_graph.values(), color='tab:red', label='Elasticity')
    ax2.tick_params(axis='y', labelcolor='tab:red')
    plt.title('Elasticity vs. Price Change')

    # Linear regression for elasticity
    slope, intercept, r_value, p_value, std_err = linregress(list(elasticity_graph.keys()), list(elasticity_graph.values()))
    ax2.plot(elasticity_graph.keys(), [slope * x + intercept for x in elasticity_graph.keys()], color='tab:green', linestyle='--', label=f'Linear Regression (slope={slope:.2f})')

    # Add average elasticity line
    ax2.axhline(y=average_elasticity, color='tab:blue', linestyle='-', label=f'Average Elasticity ({average_elasticity:.2f})')

    # # Add equilibrium point A
    # ax2.scatter(0, elasticity_graph[0], color='tab:purple', label='Equilibrium Point A (0, 0)')
    ax2.legend()

    fig2.tight_layout()
    plt.savefig('elasticity.png')
    plt.close(fig2)


def main():
    """Main function to orchestrate the reading, organizing, and elasticity calculation."""
    df = read_excel()

    if df is not None:  # Ensure the DataFrame is valid
        organized_excel = organize_file(df)

        elasticity_graph, quantity_demanded, average_elasticity = calculated_elasticity(organized_excel)
        print(f"The average elasticity is: {average_elasticity}")

        plot_graphs(elasticity_graph, quantity_demanded, average_elasticity)

        # elasticity, elasticity1, elasticity2 = calculated_elasticity(organized_excel)
        #
        # print(f"The elasticity is: {elasticity}")
        # print(f"The elasticity is: {elasticity1}")
        # print(f"The elasticity is: {elasticity2}")


if __name__ == "__main__":
    main()
