import pandas as pd

# Load the dataset from a CSV file
df = pd.read_csv('water_quality_dataset.csv')

# Check for missing values in the dataset
df.isnull().sum()

# Create a boxplot for each water quality parameter
for col in df.columns:
    plt.boxplot(df[col])
    plt.title(col)
    plt.show()

# Create histograms of all water quality parameters
df.hist(figsize=(10, 10))
plt.show()

# Create a correlation matrix to identify correlations between water quality parameters
corr_matrix = df.corr()
plt.matshow(corr_matrix)
plt.show()

# Calculate the mean and standard deviation of each water quality parameter
df.describe()
