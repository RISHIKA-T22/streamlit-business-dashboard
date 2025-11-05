import pandas as pd
import streamlit as st

# Set up the page
st.set_page_config(page_title="Superstore Analytics", layout="wide")
st.title("🏢 Superstore Sales Dashboard")
st.write("Real Business Analytics - Internship Project")

# Load the REAL business data
df = pd.read_csv('superstore_data.csv')
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'])

# ===== REAL BUSINESS KPIs =====
st.subheader("📈 Key Business Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Revenue", f"${df['Sales'].sum():,.0f}")

with col2:
    st.metric("Total Profit", f"${df['Profit'].sum():,.0f}")

with col3:
    profit_margin = (df['Profit'].sum() / df['Sales'].sum()) * 100
    st.metric("Profit Margin", f"{profit_margin:.1f}%")

with col4:
    st.metric("Total Orders", f"{len(df):,}")

# ===== BUSINESS FILTERS =====
st.subheader("🔍 Business Intelligence Filters")

col1, col2, col3 = st.columns(3)

with col1:
    selected_region = st.selectbox("Business Region", 
                                  ['All Regions'] + list(df['Region'].unique()))

with col2:
    selected_category = st.selectbox("Product Category", 
                                    ['All Categories'] + list(df['Category'].unique()))

with col3:
    selected_segment = st.selectbox("Customer Segment", 
                                   ['All Segments'] + list(df['Segment'].unique()))

# Apply business filters
filtered_df = df.copy()
if selected_region != 'All Regions':
    filtered_df = filtered_df[filtered_df['Region'] == selected_region]
if selected_category != 'All Categories':
    filtered_df = filtered_df[filtered_df['Category'] == selected_category]
if selected_segment != 'All Segments':
    filtered_df = filtered_df[filtered_df['Segment'] == selected_segment]

# ===== BUSINESS ANALYTICS =====
st.subheader("📊 Business Performance")

# Chart 1: Sales by Category (Business View)
st.write("**Revenue by Product Category**")
category_sales = filtered_df.groupby('Category')['Sales'].sum()
st.bar_chart(category_sales)

# Chart 2: Monthly Revenue Trend
st.write("**Monthly Revenue Trend**")
monthly_sales = filtered_df.groupby(pd.Grouper(key='Order_Date', freq='M'))['Sales'].sum()
st.line_chart(monthly_sales)

# Chart 3: Regional Performance
st.write("**Regional Business Performance**")
region_performance = filtered_df.groupby('Region').agg({'Sales': 'sum', 'Profit': 'sum'})
st.bar_chart(region_performance)

# ===== BUSINESS INSIGHTS =====
st.subheader("💡 Business Insights")

# Top performing products
st.write("**Top 5 Products by Profit**")
top_products = filtered_df.groupby('Sub_Category')['Profit'].sum().nlargest(5)
st.bar_chart(top_products)

# Customer segments analysis
st.write("**Customer Segment Performance**")
segment_performance = filtered_df.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'})
st.dataframe(segment_performance.style.format("${:,.2f}"))

# ===== DETAILED BUSINESS DATA =====
st.subheader("📋 Order Details")
st.dataframe(filtered_df, use_container_width=True)

st.success("🎉 Professional Business Dashboard Ready for Executive Review!")