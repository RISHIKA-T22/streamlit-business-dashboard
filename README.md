

# Universal Business Analytics Dashboard

A Python-based business analytics dashboard built using Streamlit and Pandas to explore sales data, monitor business metrics, and visualize sales performance.

## Overview

This project presents sales information from a sample Superstore dataset through an interactive web dashboard. It displays key business metrics, provides filters for exploring data, and generates charts and tables to summarize sales and profit performance.

## Features

- **Key Business Metrics:** Displays total revenue, total profit, profit margin, and total number of records.
- **Interactive Filters:** Filter the dataset by business region, product category, and customer segment.
- **Revenue by Product Category:** Displays total sales for each product category using a bar chart.
- **Monthly Revenue Trend:** Visualizes monthly sales using a line chart.
- **Regional Business Performance:** Compares regional sales and profit using a bar chart.
- **Profit Analysis:** Displays the five subcategories with the highest total profit.
- **Customer Segment Performance:** Summarizes sales and profit by customer segment in a table.
- **Order Details:** Displays the filtered dataset in a table.

**Note:** The KPI cards display metrics calculated from the full dataset. The charts and tables use the filtered dataset.

## Technologies Used

- **Python** – Application programming language
- **Streamlit** – Dashboard interface and charts
- **Pandas** – Data loading, filtering, grouping, and aggregation
- **NumPy** – Used by the data-generation script
- **CSV** – Dataset storage format

## Dataset

The dashboard loads `superstore_data.csv`.

The repository also contains `sales_data.csv` and `download_data.py`.

The data-generation script creates a sample Superstore dataset containing 1,000 simulated records. The dataset includes fields such as:

- Order ID
- Order Date
- Ship Date
- Customer ID
- Customer Segment
- Region and State
- Product Category and Subcategory
- Sales
- Quantity
- Discount
- Profit

The generated data is synthetic and is intended for demonstration and analytics practice, not as verified real-world business data.

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

### File Description

- `app.py` – Main Streamlit dashboard application.
- `download_data.py` – Script for generating the sample Superstore dataset.
- `superstore_data.csv` – Dataset loaded by the dashboard.
- `sales_data.csv` – Additional CSV file included in the repository.
- `README.md` – Project documentation.
- `LICENSE` – MIT License.
- `.gitignore` – Git ignore configuration.

## Getting Started

### Prerequisites

- Python
- pip package manager

### 1. Clone the Repository

```bash
git clone https://github.com/RISHIKA-T22/streamlit-business-dashboard.git
cd streamlit-business-dashboard
```

### 2. Install Dependencies

```bash
pip install streamlit pandas numpy
```

### 3. Run the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser. If it does not open automatically, use the local URL displayed in the terminal.

## Generate the Sample Dataset

To regenerate `superstore_data.csv`, run:

```bash
python download_data.py
```

This runs the data-generation script and creates or replaces the generated dataset.

## Author

**T Rishika**

GitHub: [RISHIKA-T22](https://github.com/RISHIKA-T22)

## License

This project is licensed under the MIT License.
