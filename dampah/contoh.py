import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title = "Superstore Dashboard",
    layout = "wide"
)

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQMqC_6fkaH6oZweJDIIYFDdE9o3P3G1hB0OKLzkGGf0pB-FjWJoAMoYca2iXV2ID5dE7hoklCSx6hE/pub?gid=0&single=true&output=csv')
df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])

df['order_year'] = df['order_date'].dt.year
CURR_YEAR = df['order_year'].max()
PREV_YEAR = CURR_YEAR - 1

st.title("Superstore Dashboard")

mx_data = pd.pivot_table(
    data = df,
    index='order_year',
    aggfunc={
        'sales':'sum',
        'profit':'sum',
        'order_id':pd.Series.nunique,
        'customer_id':pd.Series.nunique
    }
    ).reset_index()

mx_data['profit_ratio'] = 100.0 * mx_data['profit'] / mx_data['sales']

mx_sales, mx_order, mx_customer, mx_profit = st.columns(4)

with mx_sales:
    curr_sales = mx_data.loc[mx_data['order_year'] == CURR_YEAR, 'sales'].values[0]
    prev_sales = mx_data.loc[mx_data['order_year'] == PREV_YEAR, 'sales'].values[0]

    sales_diff_pct = 100.0 * (curr_sales - prev_sales) / prev_sales

    st.metric(
        label = 'Sales',
        value = f"{curr_sales:.2f}",
        delta = f"{sales_diff_pct:.2f}%"
    )

with mx_order:
    curr_order = mx_data.loc[mx_data['order_year'] == CURR_YEAR, 'order_id'].values[0]
    prev_order = mx_data.loc[mx_data['order_year'] == PREV_YEAR, 'order_id'].values[0]

    order_diff_pct = 100.0 * (curr_order - prev_order) / prev_order

    st.metric(
        label = 'Order',
        value = f"{curr_order}",
        delta = f"{order_diff_pct:.2f}%"
    )

with mx_customer:
    curr_cust = mx_data.loc[mx_data['order_year'] == CURR_YEAR, 'customer_id'].values[0]
    prev_cust = mx_data.loc[mx_data['order_year'] == PREV_YEAR, 'customer_id'].values[0]

    cust_diff_pct = 100.0 * (curr_cust - prev_cust) / prev_cust

    st.metric(
        label = 'Customer',
        value = f"{curr_cust}",
        delta = f"{cust_diff_pct:.2f}%"
    )

with mx_profit:
    curr_profit = mx_data.loc[mx_data['order_year'] == CURR_YEAR, 'profit_ratio'].values[0]
    prev_profit = mx_data.loc[mx_data['order_year'] == PREV_YEAR, 'profit_ratio'].values[0]

    profit_diff_pct = 100.0 * (curr_profit - prev_profit) / prev_profit

    st.metric(
        label = 'Profit',
        value = f"{curr_profit:.2f}",
        delta = f"{profit_diff_pct:.2f}%"
    )

freq = st.selectbox("Freq", ["Harian", "Bulanan"])

timeUnit = {
    'Harian':'yearmonthdate',
    'Bulanan':'yearmonth'
}

st.header("Sales trend")
# altair initiate chart
sales_line = alt.Chart(df[df['order_year'] == CURR_YEAR]).mark_line().encode(
    alt.X('order_date', title='Order Date', timeUnit=timeUnit[freq]),
    alt.Y('sales', title='Sales', aggregate='sum')
)

st.altair_chart(sales_line, use_container_width=True)

sales_bar = alt.Chart(df[df['order_year'] == CURR_YEAR]).mark_bar().encode(
    alt.X('order_date', title='Order Date', timeUnit=timeUnit[freq]),
    alt.Y('sales', title='Revenue', aggregate='sum')
)

st.altair_chart(sales_bar, use_container_width=True)

st.dataframe(df)

st.dataframe(mx_data, use_container_width=True)