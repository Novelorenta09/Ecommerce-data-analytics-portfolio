import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# set page dashboard
st.set_page_config(
    page_title= "Ecommerce Dashboard 2018",
    page_icon="🐱‍🚀",
    layout="wide"
)

# set stye seaborn
sns.set_theme(style="whitegrid")

dashboard_df = pd.read_csv("all_table_df.zip")
dashboard_df['order_purchase_timestamp'] = pd.to_datetime(
    dashboard_df['order_purchase_timestamp']
)


# helper function
# no 1
def create_category_revenue_df(dashboard_df):
    category_revenue = (
        dashboard_df.dropna(subset=['product_category_name'])
        .groupby('product_category_name')
        .agg(
            total_orders=('order_id','nunique'),
            total_items_sold=('order_item_id','count'),
            total_revenue=('price','sum')
        )
        .reset_index()
        .sort_values(by='total_revenue', ascending=False)
    )
    return category_revenue

# no 2
def create_late_sellers_df(dashboard_df):
    df_late = dashboard_df[dashboard_df['order_delivered_carrier_date'] > dashboard_df['shipping_limit_date']]
    late_sellers = (
        df_late
        .groupby('seller_id')
        .agg(
            total_late_orders=('order_id', 'nunique'),
            total_late_items=('order_item_id','count')
        )
        .reset_index()
        .sort_values(by='total_late_orders', ascending=False)
    )
    return late_sellers

# no 3
def create_city_volume_df(dashboard_df):
    city_volume = (
        dashboard_df.groupby('customer_city')
        .agg(
            total_orders=('order_id','nunique'),
            total_customers=('customer_unique_id','nunique')
        )
        .reset_index()
        .sort_values(by='total_orders', ascending=False)
    )
    return city_volume

# filter tahun 2018 dan status delivered
df_2018 = dashboard_df[
    (dashboard_df['order_status'] == 'delivered') &
    (dashboard_df['order_purchase_timestamp'].dt.year == 2018)
].copy()

# memanggil helper 
category_revenue_df = create_category_revenue_df(df_2018)
late_sellers_df = create_late_sellers_df(df_2018)
city_volume_df = create_city_volume_df(df_2018)

# header dashboard
st.title("Ecommerce Performance Dashboard (2018)")
st.markdown("Analisis kategori produk, performa seller, distrubsi kota pelanggan")

# sidebar filter tanggal
with st.sidebar:
    st.image("https://pin.it/42e4uSEQB")
    st.header("filter")
    st.write("Data yg ditampilkan telah difilter khusus untuk pesanan berstatus 'delivered' pada tahun 2018")

# metric card
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    total_rev = category_revenue_df['total_revenue'].sum()
    st.metric("Total Revenue (2018)", f"R$ {total_rev:,.2f}")
with col_m2:
    total_orders = city_volume_df['total_orders'].sum()
    st.metric("Total Orders", f"{total_orders:,}")
with col_m3:
    total_cust = city_volume_df['total_customers'].sum()
    st.metric("Total Unique Customers", f"{total_cust:,}")

st.divider()

# no 1 revenue by produk
st.subheader("1. Revenue kategori produk")
top5_category = category_revenue_df.head(5)
bottom5_category = category_revenue_df.tail(5).sort_values(by='total_revenue', ascending=True)
fig_category, axes_category = plt.subplots(nrows=1, ncols=2, figsize=(16,5))
# top 5 chart
sns.barplot(
    data=top5_category, x='total_revenue', y='product_category_name',
    hue='product_category_name', palette='Blues_r', legend=False, ax=axes_category[0]
)
axes_category[0].set_title("Top 5 Categories by Revenue", fontweight='bold')
axes_category[0].set_xlabel("Total Revenue (BRL)")
axes_category[0].set_ylabel("Category")
for p in axes_category[0].patches:
    w = p.get_width()
    axes_category[0].annotate(f'R${w/1000:,.1f}k', (w, p.get_y() + p.get_height()/2.),
                         ha='left', va='center', xytext=(5, 0), textcoords='offset points')


# Bottom 5 Chart
sns.barplot(
    data=bottom5_category, x='total_revenue', y='product_category_name',
    hue='product_category_name', palette='Reds_r', legend=False, ax=axes_category[1]
)
axes_category[1].set_title("Bottom 5 Categories by Revenue", fontweight='bold')
axes_category[1].set_xlabel("Total Revenue (BRL)")
axes_category[1].set_ylabel("")
for p in axes_category[1].patches:
    w = p.get_width()
    axes_category[1].annotate(f'R${w:,.2f}', (w, p.get_y() + p.get_height()/2.),
                         ha='left', va='center', xytext=(5, 0), textcoords='offset points')
plt.tight_layout()
st.pyplot(fig_category)
st.divider()

# no 2
st.subheader("2. Top 10 Seller Terbanyak Keterlambatan Pengiriman")

top_10_late = late_sellers_df.head(10).copy()
top_10_late['seller_short_id'] = top_10_late['seller_id'].str[:8] + '...'

fig_late, ax_late = plt.subplots(figsize=(12, 5))
sns.barplot(
    data=top_10_late, x='total_late_orders', y='seller_short_id',
    hue='seller_short_id', palette='Reds_r', legend=False, ax=ax_late
)
ax_late.set_title("Top 10 Sellers with Most Delayed Carrier Deliveries", fontweight='bold')
ax_late.set_xlabel("Total Delayed Orders")
ax_late.set_ylabel("Seller ID (Truncated)")

for p in ax_late.patches:
    w = p.get_width()
    if w > 0:
        ax_late.annotate(f'{int(w)} orders', (w, p.get_y() + p.get_height()/2.),
                         ha='left', va='center', xytext=(5, 0), textcoords='offset points')

plt.tight_layout()
st.pyplot(fig_late)

st.divider()

# no 3
st.subheader("3. Top 10 Kota dengan Order & Customer Terbanyak")

top_10_cities = city_volume_df.head(10)

fig_city, axes_city = plt.subplots(nrows=1, ncols=2, figsize=(16, 5))

# Total Orders Chart
sns.barplot(
    data=top_10_cities, x='total_orders', y='customer_city',
    hue='customer_city', palette='Blues_r', legend=False, ax=axes_city[0]
)
axes_city[0].set_title("Top 10 Cities by Total Orders", fontweight='bold')
axes_city[0].set_xlabel("Total Orders")
axes_city[0].set_ylabel("City")
for p in axes_city[0].patches:
    w = p.get_width()
    axes_city[0].annotate(f'{int(w):,}', (w, p.get_y() + p.get_height()/2.),
                         ha='left', va='center', xytext=(5, 0), textcoords='offset points')

# Total Unique Customers Chart
sns.barplot(
    data=top_10_cities, x='total_customers', y='customer_city',
    hue='customer_city', palette='Purples_r', legend=False, ax=axes_city[1]
)
axes_city[1].set_title("Top 10 Cities by Unique Customers", fontweight='bold')
axes_city[1].set_xlabel("Total Unique Customers")
axes_city[1].set_ylabel("")
for p in axes_city[1].patches:
    w = p.get_width()
    axes_city[1].annotate(f'{int(w):,}', (w, p.get_y() + p.get_height()/2.),
                         ha='left', va='center', xytext=(5, 0), textcoords='offset points')

plt.tight_layout()
st.pyplot(fig_city)
