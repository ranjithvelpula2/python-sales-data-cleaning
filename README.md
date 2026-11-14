 # Sales Data Cleaning (Python)

Beginner project built to practise Python and pandas. The sales data is sample data I created for practice.

## What it does
- Loads a CSV file with pandas
- Removes duplicate rows
- Fixes inconsistent text ("north" to "North")
- Fills a missing quantity with the median
- Calculates revenue and summarises it by product and region
- Saves a cleaned file (sales_clean.csv)

## How to run
pip install pandas
python3 analysis.py

## Finding
Laptops earned the most revenue (1800) and the North region was the top region (1650), out of a total of 3045. One missing quantity was filled with median (3.5).
