import pandas as pd

df = pd.read_csv("100 days of code//day 71//salaries_by_college_major.csv")

clean_df = df.dropna()
print(clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary']))

