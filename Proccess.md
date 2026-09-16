# Proyek Analisis Data: E-Commerce Dataset

---
## A. Menentukan Pertanyaan Bisnis
*(Bagian ini dapat diisi setelah merumuskan pertanyaan bisnis)*

## B. Data Wrangling
Data Wrangling adalah proses mengumpulkan, menilai, dan membersihkan data agar siap digunakan untuk analisis.

1. Gathering Data: Pada tahap ini, kita memuat dataset E-Commerce dari file lokal `.csv` ke dalam DataFrame menggunakan pustaka `pandas`.

2. Assessing Data: Pada tahap ini, kita mengevaluasi kualitas data dengan mengecek:
   - Tipe Data masing-masing kolom
   - Missing Value (nilai yang hilang)
   - Data Duplikat
   - Inaccurate Value (nilai tidak akurat / anomali)

   #### 🔍 Ringkasan Temuan Evaluasi Data (Assessing Data Summary)
   Berdasarkan pengecekan yang telah dilakukan, berikut adalah ringkasan masalah kualitas data yang ditemukan:


| Nama DataFrame | Tipe Data | Missing Value | Duplicate Data | Inaccurate Value / Anomali |
| :--- | :---: | :--- | :---: | :--- |
| `customers_df` | OK | - | 0 | - |
| `geolocation_df` | OK | - | **261,831** | - |
| `order_items_df` | OK | - | 0 | - |
| `order_payments_df` | OK | - | 0 | - |
| `order_reviews_df` | OK | • `review_comment_title`: 87,656<br>• `review_comment_message`: 58,247 | 0 | - |
| `orders_df` | OK | • `order_approved_at`: 160<br>• `order_delivered_carrier_date`: 1,783<br>• `order_delivered_customer_date`: 2,965 | 0 | - |
| `product_cate_name_df` | OK | - | 0 | - |
| `products_df` | OK | • `product_category_name`: 610<br>• `product_name_lenght`: 610<br>• `product_description_lenght`: 610<br>• `product_photos_qty`: 610<br>• `product_weight_g`: 2<br>• `product_length_cm`: 2<br>• `product_height_cm`: 2<br>• `product_width_cm`: 2 | 0 | Terdapat *inaccurate value* pada kolom `product_weight_g` |
| `sellers_df` | OK | - | 0 | - |

---

3. Cleaning Data: Pada tahap ini, menangani (*handling*) masalah-masalah kualitas data yang telah ditemukan pada proses *Assessing Data* sebelumnya.







**Strategi Pembersihan:**
- **Pembersihan Data Duplikat**: Menghapus baris duplikat pada `geolocation_df`.
- **Handling Missing Values**: Imputasi atau pengananganan nilai yang hilang pada `order_reviews_df`, `orders_df`, dan `products_df`.
- **Fixing Inaccurate Values & Tipe Data**: Penyesuaian nilai anomali berat produk dan konversi tipe data ke format yang sesuai (misal: `datetime`).
