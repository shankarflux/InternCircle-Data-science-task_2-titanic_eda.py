import pandas as pd
import numpy as np

# 1. Load the Titanic dataset from public raw URL
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 2. DataFrame Operations
print("--- First 5 Rows ---")
print(df.head())

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

# 3. Handling Missing Values and Duplicates
print("\n--- Missing Values Count ---")
print(df.isnull().sum())

# Fill missing Age values with median age
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing Embarked values with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop Cabin column due to high percentage of missing values
df = df.drop(columns=['Cabin'])

# Remove duplicate rows if any exist
df = df.drop_duplicates()

print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())

# 4. Grouping and Aggregation Analysis
print("\n--- Survival Rate by Gender ---")
gender_survival = df.groupby('Sex')['Survived'].mean() * 100
print(gender_survival)

print("\n--- Survival Rate by Passenger Class ---")
class_survival = df.groupby('Pclass')['Survived'].mean() * 100
print(class_survival)

print("\n--- Average Age and Fare by Survival Status ---")
grouped_stats = df.groupby('Survived')[['Age', 'Fare']].mean()
print(grouped_stats)