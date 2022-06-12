import pandas as pd

df = pd.read_csv('salaries-by-college-major.csv')
# pd.options.display.float_format = '{:,.2f}'.format
# df.head()
# df.tail()
# df.shape
# df.columns
clean_df = df.dropna()

# idx_max = clean_df['Mid-Career Median Salary'].idxmax()
# idx_min = clean_df['Mid-Career Median Salary'].idxmin()
# min_sal = clean_df['Starting Median Salary'].idxmin()
# clean_df.loc[min_sal]

spread = clean_df['Mid-Career 90th Percentile Salary'] - \
    clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread)

# low_risk = clean_df.sort_values('Spread',ascending=False)
# low_risk[['Undergraduate Major', 'Spread']].head()

# high_potenty = clean_df.sort_values('Mid-Career 90th Percentile Salary',ascending=False)
# high_potenty.head()


clean_df.groupby('Group').mean()
