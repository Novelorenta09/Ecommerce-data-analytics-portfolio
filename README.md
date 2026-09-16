# Ecommerce-data-analytics-portfolio
Final project submission for Dicoding's "Belajar Fundamental Analisis Data" course. Features exploratory data analysis (EDA), data wrangling, and an interactive Streamlit dashboard.

## 🛠️ Tahapan Analisis Data
### 1. Data Wrangling
* **Gathering Data**: Memuat dan membaca dataset E-Commerce dari file lokal (.csv) menggunakan pustaka Pandas.
* **Assessing Data**: Menilai dan mengevaluasi kualitas data, meliputi:
  * Pengecekan tipe data
  * Identifikasi *missing value*
  * Pengecekan data duplikat (*duplicate entries*)
  * Identifikasi nilai tidak akurat / anomali (*inaccurate values*)
* **Cleaning Data**: Melakukan pembersihan data berdasarkan temuan pada proses *Assessing Data*.

#### 🔍 Ringkasan Temuan Evaluasi Data (Assessing Data Summary)

Berikut adalah tabel ringkasan hasil *Assessing Data* pada dataset E-Commerce yang digunakan:

| Nama DataFrame | Tipe Data | Missing Value | Duplicate Data | Inaccurate Value / Anomali |
| :--- | :---: | :--- | :---: | :--- |
| `customers_df` | OK | - | 0 | - |
| `geolocation_df` | OK | - | **261,831** | - |
| `order_items_df` | OK | - | 0 | - |
| `order_payments_df` | OK | - | 0 | - |
| `order_reviews_df` | OK | • `review_comment_title`: 87,656<br>• `review_comment_message`: 58,247 | 0 | - |
| `orders_df` | OK | • `order_approved_at`: 160<br>• `order_delivered_carrier_date`: 1,783<br>• `order_delivered_customer_date`: 2,965 | 0 | - |
| `product_category_name_translation_df` | OK | - | 0 | - |
| `products_df` | OK | • `product_category_name`: 610<br>• `product_name_lenght`: 610<br>• `product_description_lenght`: 610<br>• `product_photos_qty`: 610<br>• `product_weight_g`: 2<br>• `product_length_cm`: 2<br>• `product_height_cm`: 2<br>• `product_width_cm`: 2 | 0 | Terdapat *inaccurate value* pada kolom `product_weight_g` |
| `sellers_df` | OK | - | 0 | - |

---

## 🚀 Rencana Langkah Selanjutnya
- [x] Data Gathering
- [x] Data Assessing
- [ ] Data Cleaning (Handling Missing Values, Duplicates, & Inaccurate Data)
- [ ] Exploratory Data Analysis (EDA)
- [ ] Data Visualization & Dashboarding (Streamlit)
