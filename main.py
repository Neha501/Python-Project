import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel('zomato.xlsx', sheet_name='zomato')

# Step 1: Remove duplicate rows
df = df.drop_duplicates()

# Step 2: Fill missing values in 'Cuisines' column
df['Cuisines'] = df['Cuisines'].fillna('Unknown')

# Step 3: Trim whitespace in string columns and standardize casing if needed
text_columns = df.select_dtypes(include='object').columns
df[text_columns] = df[text_columns].apply(lambda x: x.str.strip())

# Step 4: Map 'Country Code' to actual country names
country_map = {
    1: 'India', 14: 'Australia', 30: 'Brazil', 37: 'Canada', 94: 'Indonesia',
    148: 'New Zealand', 162: 'Philippines', 166: 'Qatar', 184: 'Singapore',
    189: 'South Africa', 191: 'Sri Lanka', 208: 'Turkey', 214: 'UAE',
    215: 'United Kingdom', 216: 'United States'
}
df['Country'] = df['Country Code'].map(country_map)
