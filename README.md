# Data-engineering-toolkitt
Simple Python scripts for data cleaning, transformation, and loading.

## Purpose
Basic data processing tools for beginners.

## Documentation
Three Python scripts:
* simple_data_cleaning.py - Removes duplicates and missing values
* data_transformation.py - Normalizes data and creates new columns
* data_loading.py - Loads and saves data to different formats

  ## Code Examples
  # Clean data
df = pd.read_csv('data.csv')
df = df.drop_duplicates().dropna()

  # Transform data  
df['age'] = df['age'] / 100
df['age_doubled'] = df['age'] * 2

  # Save data
df.to_parquet('final_data.parquet')

## Contribution Guide

* Fork the repo
* Create feature branch: git checkout -b feature/name
* Make changes and commit
* Push and create Pull Request to develop branch

* Install: pip install pandas
