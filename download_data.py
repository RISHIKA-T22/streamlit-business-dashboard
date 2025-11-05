import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("Creating Realistic Superstore Dataset...")

# Create realistic business data similar to actual Superstore dataset
np.random.seed(42)

# Business segments, categories, and sub-categories (like real superstore data)
segments = ['Consumer', 'Corporate', 'Home Office']
categories = {
    'Furniture': ['Chairs', 'Tables', 'Bookcases', 'Furnishings'],
    'Office Supplies': ['Storage', 'Art', 'Labels', 'Supplies'],
    'Technology': ['Phones', 'Machines', 'Accessories', 'Copiers']
}
regions = ['West', 'East', 'South', 'Central']
states = ['California', 'Texas', 'New York', 'Florida', 'Illinois', 'Ohio', 'Georgia', 'Michigan']

# Generate 1000 realistic orders
data = []
order_id = 1000

for _ in range(1000):
    order_date = datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365))
    ship_date = order_date + timedelta(days=np.random.randint(1, 10))
    
    segment = np.random.choice(segments)
    region = np.random.choice(regions)
    state = np.random.choice(states)
    
    category = np.random.choice(list(categories.keys()))
    sub_category = np.random.choice(categories[category])
    
    # Realistic pricing based on category
    if category == 'Technology':
        sales = np.random.uniform(200, 2000)
    elif category == 'Furniture':
        sales = np.random.uniform(100, 1500)
    else:  # Office Supplies
        sales = np.random.uniform(10, 500)
    
    quantity = np.random.randint(1, 10)
    discount = np.random.uniform(0, 0.3)  # 0-30% discount
    profit = sales * np.random.uniform(0.1, 0.4) - (sales * discount)
    
    data.append({
        'Order_ID': f'CA-{order_id}',
        'Order_Date': order_date,
        'Ship_Date': ship_date,
        'Customer_ID': f'CG-{np.random.randint(1000, 9999)}',
        'Segment': segment,
        'Region': region,
        'State': state,
        'Category': category,
        'Sub_Category': sub_category,
        'Sales': round(sales, 2),
        'Quantity': quantity,
        'Discount': round(discount, 2),
        'Profit': round(profit, 2)
    })
    
    order_id += 1

# Create DataFrame
df = pd.DataFrame(data)
df.to_csv('superstore_data.csv', index=False)

print("✅ Realistic Superstore dataset created!")
print(f"📊 Total orders: {len(df)}")
print(f"📅 Date range: {df['Order_Date'].min().date()} to {df['Order_Date'].max().date()}")
print(f"💰 Total Sales: ${df['Sales'].sum():,.2f}")
print(f"🎯 Segments: {df['Segment'].unique()}")
print(f"🏷️ Categories: {df['Category'].unique()}")