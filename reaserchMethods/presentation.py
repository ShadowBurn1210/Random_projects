import pprint

import numpy as np
import pandas as pd
from scipy.stats import ttest_ind, pearsonr, f_oneway, kruskal
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
all_data = pd.read_csv(r'./reaserchMethods/data.csv')
group_data = pd.read_csv(r'./reaserchMethods/Groups.csv')


# Descriptive Statistics
def descriptive_stats(groups, submission_data):
    invalid_values = ['Loading...', '#N/A']
    my_data = submission_data.replace(invalid_values, np.nan)

    # Merge the data
    groups = groups.rename(columns={'id': 'submission_id'})
    merged_data = pd.merge(groups, my_data, on='submission_id')
    # Convert columns to numeric (if they are not already)
    for col in merged_data.columns[1:]:  # Skip 'submission_id'
        merged_data[col] = pd.to_numeric(merged_data[col], errors='coerce')

    # Calculate t-test scores between groups
    group1 = merged_data[merged_data['group_id'] != -16]
    group2 = merged_data[merged_data['group_id'] != 2]
    # group1 = merged_data[merged_data['group_id']]

    # Extract kappa score columns (assuming they start from column 6)
    kappa_columns1 = group1.iloc[:, 5:10].apply(pd.to_numeric, errors='coerce')
    kappa_columns2 = group2.iloc[:, 5:10].apply(pd.to_numeric, errors='coerce')

    # Compute descriptive statistics for group1
    group1_descriptive_stats = kappa_columns1.describe()
    # Combine all kappa scores into a single column
    kappa_columns1 = kappa_columns1.stack()
    pprint.pprint(kappa_columns1)
    group11_descriptive_stats = kappa_columns1.describe()
    print(group11_descriptive_stats)

    group2_descriptive_stats = kappa_columns2.describe()
    # Combine all kappa scores into a single column
    kappa_columns2 = kappa_columns2.stack()
    group22_descriptive_stats = kappa_columns2.describe()
    print(group22_descriptive_stats)

    # Display results
    print("Overall Kappa Scores Statistics for Group 1:")
    print(group1_descriptive_stats)
    print("\nOverall Kappa Scores Statistics for Group 2:")
    print(group2_descriptive_stats)

    # Calculate t-test scores between groups
    t_test_result = ttest_ind(kappa_columns2, kappa_columns1, nan_policy='omit')

    # Store results
    t_test_results = {
        't_statistic': t_test_result.statistic,
        'p_value': t_test_result.pvalue
    }
    pprint.pprint(t_test_results)

    # Now create graphs for the data that shows the distribution of the kappa scores for each group
    # and the distribution of the kappa scores for each text


    # Create a boxplot for the kappa scores of each group
    sns.set(style="whitegrid", font="sans-serif", font_scale=1.2)

    # Create a figure with two subplots
    plt.figure(figsize=(14, 6))

    # First subplot for Group 1
    plt.subplot(1, 1, 1)
    sns.boxplot(data=group1[['text1_kappa', 'text2_kappa', 'text3_kappa', 'text4_kappa', 'text5_kappa']],
                color='skyblue')
    # plt.title('Group 1 Kappa Scores', fontsize=14, loc='left')  # APA style: left-aligned title
    plt.xlabel('Texts', fontsize=12)
    sns.despine()
    plt.ylabel('Kappa Score', fontsize=12)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

    # Second subplot for Group 2
    # plt.subplot(1, 2, 2)
    # sns.boxplot(data=group2[['text1_kappa', 'text2_kappa', 'text3_kappa', 'text4_kappa', 'text5_kappa']],
    #             color='skyblue')
    # plt.title('Group 2 Kappa Scores', fontsize=14, loc='left')  # APA style: left-aligned title
    # plt.xlabel('Texts', fontsize=12)
    # plt.ylabel('Kappa Score', fontsize=12)
    # plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Show the plot
    plt.show()


def correlation(data):
    # Clean the data: Replace invalid values with NaN
    invalid_values = ['Loading...', '#N/A']
    my_data = data.replace(invalid_values, np.nan)

    # Convert columns to numeric (if they are not already)
    for col in my_data.columns:
        my_data[col] = pd.to_numeric(my_data[col], errors='coerce')

    # Calculate correlations between textX_ai and textX_kappa
    ai_values = []
    kappa_values = []

    for i in range(1, 6):  # Loop through text1 to text5
        ai_col = f'text{i}_ai'
        kappa_col = f'text{i}_kappa'

        if ai_col in my_data.columns and kappa_col in my_data.columns:
            # Drop rows with NaN values in either column
            clean_data = my_data[[ai_col, kappa_col]].dropna().apply(pd.to_numeric, errors='coerce').dropna()

            ai_values.extend(clean_data[ai_col].tolist())
            kappa_values.extend(clean_data[kappa_col].tolist())

    # Calculate overall Pearson correlation
    if ai_values and kappa_values:
        my_correlation, p_value = pearsonr(ai_values, kappa_values)
        print(f"Overall AI vs Kappa Correlation:")
        print(f"  Correlation: {my_correlation:.3f}")
        print(f"  p-value: {p_value:.3f}")
        if p_value < 0.05:
            print("  Significant correlation (p < 0.05)")
        else:
            print("  No significant correlation (p >= 0.05)")
        print()

        # Create a regression plot to show the correlation between AI text amount and kappa score
        # plt.figure(figsize=(10, 6))
        # sns.regplot(x=ai_values, y=kappa_values, scatter_kws={'alpha': 0}, line_kws={'color': 'red'})
        # for x in np.unique(ai_values):
        #     kappa_values_for_x = [kappa_values[i] for i in range(len(ai_values)) if ai_values[i] == x]
        #     plt.scatter([x], [np.mean(kappa_values_for_x)], color='black', s=50)        
        # # set x step 1.0
        # plt.xticks(np.arange(min(ai_values), max(ai_values)+1, 1.0))
        # # plt.title('Kappa Score vs AI Text Amount', fontsize=16)
        # plt.xlabel('AI Sentence Count', fontsize=14)
        # plt.ylabel('Kappa Score', fontsize=14)
        # plt.grid(False)
        # plt.grid(which='major', axis='y', linewidth=0.5)
        # sns.despine()
        # plt.show()

        # Create a boxplot to visualize the distribution of kappa scores across AI categories
        # Convert ai_values into categorical bins for better visualization
        # ai_categories = pd.cut(ai_values, bins=3, labels=['Low', 'Medium', 'High'])
        category_data = pd.DataFrame({'AI Sentence Count': ai_values, 'Kappa Score': kappa_values})

        plt.figure(figsize=(10, 6))
        # sns.boxplot(x='AI Sentence Count', y='Kappa Score', data=category_data, color='skyblue')
        sns.boxplot(
            x='AI Sentence Count', 
            y='Kappa Score', 
            data=category_data, 
            color='skyblue',
            medianprops={'color': 'black', 'linewidth': 2}  # Set median to red and 5px thick
        )

        plt.xlabel('AI Sentence Count', fontsize=14)
        plt.ylabel('Kappa Score', fontsize=14)
        sns.despine()
        plt.show()



        # Group AI text amounts into categories for ANOVA and Kruskal-Wallis
        # Example: Divide AI text amounts into 3 categories (low, medium, high)
        ai_categories = pd.cut(ai_values, bins=3, labels=['Low', 'Medium', 'High'])
        category_data = pd.DataFrame({'AI Category': ai_categories, 'Kappa Score': kappa_values})

        # Perform one-way ANOVA
        anova_groups = [category_data[category_data['AI Category'] == cat]['Kappa Score'] for cat in category_data['AI Category'].unique()]
        f_statistic, p_value_anova = f_oneway(*anova_groups)
        print(f"One-way ANOVA Test:")
        print(f"  F-statistic: {f_statistic:.3f}")
        print(f"  p-value: {p_value_anova:.3f}")
        if p_value_anova < 0.05:
            print("  Significant difference between groups (p < 0.05)")
        else:
            print("  No significant difference between groups (p >= 0.05)")
        print()

        # # Perform Kruskal-Wallis test
        # h_statistic, p_value_kruskal = kruskal(*anova_groups)
        # print(f"Kruskal-Wallis Test:")
        # print(f"  H-statistic: {h_statistic:.3f}")
        # print(f"  p-value: {p_value_kruskal:.3f}")
        # if p_value_kruskal < 0.05:
        #     print("  Significant difference between groups (p < 0.05)")
        # else:
        #     print("  No significant difference between groups (p >= 0.05)")
        # print()
        #
        # # Create a boxplot to visualize the distribution of kappa scores across AI categories
        # plt.figure(figsize=(10, 6))
        # sns.boxplot(x='AI Category', y='Kappa Score', hue='AI Category', data=category_data, palette='Set2', legend=False)
        # plt.title('Distribution of Kappa Scores by AI Text Amount Category', fontsize=16)
        # plt.xlabel('AI Text Amount Category', fontsize=14)
        # plt.ylabel('Kappa Score', fontsize=14)
        # plt.grid(True)
        # plt.show()

        return {
            'Pearson correlation': {'correlation': my_correlation, 'p_value': p_value},
            'ANOVA': {'F-statistic': f_statistic, 'p_value': p_value_anova},
            # 'Kruskal-Wallis': {'H-statistic': h_statistic, 'p_value': p_value_kruskal}
        }

# Main
if __name__ == "__main__":
    # Drop the 'submission_id' column as it's not needed for analysis
    data = all_data.drop(columns=['submission_id'])
    # descriptive_stats(group_data, all_data)
    results = correlation(data)
    pprint.pprint(results)
