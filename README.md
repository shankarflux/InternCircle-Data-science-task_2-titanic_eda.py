# InternCircle-Data-science-task_2-titanic_eda.py
# Titanic Exploratory Data Analysis

This repository contains a Python script for conducting Exploratory Data Analysis on the Titanic dataset using Pandas and NumPy.

## Project Overview

The objective of this project is to analyze passenger data from the Titanic to uncover key patterns related to passenger survival rates based on demographic characteristics and ticket details.

## Key Features

- **Dataset Loading:** Fetches raw data directly from an online CSV source.
- **Data Inspection:** Displays dataset shape, column types, and summary statistics.
- **Data Cleaning:** Fills missing values in Age and Embarked columns, drops unnecessary features, and removes duplicate rows.
- **Grouping and Aggregation:** Computes survival percentages grouped by Gender, Passenger Class, and Embarkation Port.
- **Feature Engineering:** Calculates total Family Size to analyze its effect on survival rate.

## Technologies Used

- Python
- Pandas
- NumPy

## How to Run

1. Open Google Colab or a local Python environment.
2. Clone or download `titanic_eda.py` from this repository.
3. Execute the script to view analysis outputs:

```bash
python titanic_eda.py
