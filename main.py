import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("\n\n\t\t\t\t\t\t\tDATASET: ZOMATO RESTAURANTS DATA\n\t\t\t\t\t\t\t***********************************************")
# Loading the  dataset
df = pd.read_excel("D:/SEMESTER4/numpypython/PythonProject/zomato.xlsx")
print(df.describe(),"/n/n/n")
print(df.info(),"/n/n/n")
print(df.isnull().sum(),"/n/n/n") 

columns_to_keep = ["Restaurant ID", "Restaurant Name", "Cuisines", "Has Table booking", "Has Online delivery", "Aggregate rating", "Price range",
"Average Cost for two", "Votes", "Latitude", "Longitude","City","Country Code"]

#cleaning
df_cleaned = df[columns_to_keep].copy()
df_cleaned.fillna(df_cleaned.mean(numeric_only=True), inplace=True)

# BASIC INFORMATION OF DATA
print("\n\n HEAD OF DATASET\n\n", df_cleaned.head(), "\n\n\n")
print("\n\n TAIL OF DATASET\n\n", df_cleaned.tail(), "\n\n\n")
print("\n\n SUMMARY STATISTICS OF DATASET\n\n", df_cleaned.describe(), "\n\n\n")
print("\n\n INFORMATION OF DATASET\n\n")
print(df_cleaned.info())
print("\n\n COLUMN NAMES\n\n", df_cleaned.columns, "\n\n\n")
print("\n\n SHAPE OF DATASET\n\n", df_cleaned.shape, "\n\n\n")
print("\n\n COUNT OF MISSING VALUES OF EACH COLUMN\n\n", df_cleaned.isnull().sum(), "\n\n\n")
print("\n\n DUPLICATE ROWS = ", df_cleaned.duplicated().sum(), "\n\n\n")

country_map = {
    1: 'India', 14: 'Australia', 30: 'Brazil', 37: 'Canada', 94: 'Indonesia',
    148: 'New Zealand', 162: 'Philippines', 166: 'Qatar', 184: 'Singapore',
    189: 'South Africa', 191: 'Sri Lanka', 208: 'Turkey', 214: 'UAE',
    215: 'United Kingdom', 216: 'United States'
}
df_cleaned['Country'] = df_cleaned['Country Code'].map(country_map)
print(df_cleaned.head(),"\n\n\n")

# CORRELATION AND COVARIANCE
print("\n\n CORRELATION MATRIX:\n", df_cleaned.corr(numeric_only=True), "\n\n\n")
print("\n\n COVARIANCE MATRIX:\n", df_cleaned.cov(numeric_only=True), "\n\n\n")
heatmap_cols = ["Aggregate rating", "Votes", "Average Cost for two", "Longitude", "Latitude", "Country Code", "Restaurant ID"]
corr_matrix = df_cleaned[heatmap_cols].corr()

# Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f")
plt.title("Heatmap of Selected Numerical Columns")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Outlier
numerical_cols = ['Aggregate rating', 'Votes', 'Average Cost for two', 'Longitude', 'Latitude', 'Country Code', 'Restaurant ID']
outliers_iqr = {}
for col in numerical_cols:
    Q1 = df_cleaned[col].quantile(0.25)
    Q3 = df_cleaned[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outlier_rows = df_cleaned[(df_cleaned[col] < lower_bound) | (df_cleaned[col] > upper_bound)]
    outliers_iqr[col] = outlier_rows.index.tolist()

    print(f"\nOutliers in '{col}': {len(outlier_rows)} found")

