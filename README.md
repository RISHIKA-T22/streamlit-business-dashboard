
# Universal Business Analytics Dashboard

A Streamlit-based dashboard for exploring sales data, tracking key business metrics, and visualizing business performance using Python.

## Overview

This project analyzes a sample Superstore sales dataset and presents business metrics, interactive filters, charts, and detailed order records through a web-based dashboard.

The dashboard uses Pandas for data processing and Streamlit for the interface and visualizations.

## Features

- **Key Business Metrics:** Displays total revenue, total profit, profit margin, and total number of records.
- **Interactive Filters:** Filter the data by region, product category, and customer segment.
- **Revenue by Category:** Visualizes sales across product categories using a bar chart.
- **Monthly Revenue Trend:** Displays monthly sales trends using a line chart.
- **Regional Performance:** Compares sales and profit across regions.
- **Profit Analysis:** Identifies the top five subcategories by total profit.
- **Customer Segment Analysis:** Summarizes sales and profit by customer segment in a table.
- **Order Details:** Displays the filtered dataset in a table.

## Technologies Used

- **Programming Language:** Python
- **Dashboard Framework:** Streamlit
- **Data Processing:** Pandas
- **Data Generation:** NumPy
- **Data Storage:** CSV

## Dataset

The project includes `superstore_data.csv`, a sample dataset generated using Python, NumPy, and Pandas.

The dataset contains 1,000 simulated records with fields such as:

- Order ID
- Order Date and Ship Date
- Customer ID and Segment
- Region and State
- Product Category and Subcategory
- Sales, Quantity, Discount, and Profit

The dataset is synthetic and is intended for demonstration and analytics practice.

## Project Structure

```text
streamlit-business-dashboard/
├── app.py
├── download_data.py
├── superstore_data.csv
├── sales_data.csv
├── README.md
├── LICENSE
└── .gitignore
```

## Getting Started

### Prerequisites

- Python
- pip package manager

### 1. Clone the repository

```bash
git clone https://github.com/RISHIKA-T22/streamlit-business-dashboard.git
cd streamlit-business-dashboard
```

### 2. Install the required libraries

```bash
pip install streamlit pandas numpy
```

### 3. Run the dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser. If it does not open automatically, use the local URL displayed in the terminal.

## Data Generation

To regenerate the sample Superstore dataset, run:

```bash
python download_data.py
```

This creates `superstore_data.csv` in the project directory. Running this script again replaces the existing generated dataset.

## Author

**T Rishika**

GitHub: [RISHIKA-T22](https://github.com/RISHIKA-T22)

## License

This project is licensed under the MIT License.






