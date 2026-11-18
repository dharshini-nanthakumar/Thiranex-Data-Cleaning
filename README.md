# Data Cleaning and Visualization Project

## Project Overview
This project focuses on cleaning, processing, analyzing, and visualizing sales data using Python. It demonstrates essential data preprocessing techniques and generates meaningful insights through graphical representations.

## Objectives
- Identify and handle missing values.
- Correct invalid data entries.
- Standardize inconsistent data.
- Detect potential duplicate records.
- Identify outliers using the IQR method.
- Calculate total sales.
- Visualize sales trends and patterns.
- Generate a data insights report and dashboard.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Project Structure

```text
Thiranex_Data_Cleaning/
│
├── data/
│   └── sales_data.csv
│
├── outputs/
│   ├── cleaned_sales_data.csv
│   ├── sales_by_product.png
│   ├── sales_by_city.png
│   ├── correlation_heatmap.png
│   ├── insights_report.txt
│   └── sales_dashboard.png
│
├── main.py
├── README.md
└── venv/
```

## Data Cleaning Techniques

1. Missing Values: Filled missing Quantity values using the median and missing City values with "Unknown".
2. Invalid Data: Converted invalid Quantity entries into missing values using Pandas.
3. Data Standardization: Standardized city names using string operations.
4. Duplicate Detection: Identified potential duplicate records for further investigation.
5. Data Type Conversion: Converted Quantity into integer format.

## Outlier Detection

The Interquartile Range (IQR) method was used to identify outliers in:
- Quantity
- Price
- Total Sales

No outliers were detected in the sample dataset.

## Data Visualization

The project generates the following visualizations:

- Bar Chart: Total sales by product.
- Pie Chart: Sales distribution by city.
- Heatmap: Correlation between numerical variables.
- Dashboard: Combined sales analysis visualizations.

## Key Insights

- Total Records: 9
- Total Sales: ₹4,38,000
- Best-Selling Product: Laptop
- Lowest-Selling Product: Tablet
- Highest-Sales City: Chennai

## How to Run the Project

1. Clone or download the project.
2. Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

3. Run the Python program:

```bash
python main.py
```

4. View the generated files in the outputs folder.

## Expected Outcome

This project demonstrates practical knowledge of data cleaning, preprocessing, exploratory data analysis, data visualization, and basic data storytelling using Python.

## Dataset Note

The dataset used in this project is a small sample sales dataset created for learning and demonstration purposes. It is not an official company dataset.