# Proyek Analisis Data: E-Commerce Dataset
- **Nama:** [Nama Kamu]
- **Email:** [Email Dicoding Kamu]
- **ID Dicoding:** [ID Dicoding Kamu]

---
## Menentukan Pertanyaan Bisnis
*(Bagian ini dapat diisi setelah merumuskan pertanyaan bisnis)*

## Data Wrangling
Data Wrangling adalah proses mengumpulkan, menilai, dan membersihkan data agar siap digunakan untuk analisis.

### 1. Gathering Data
Pada tahap ini, kita memuat dataset E-Commerce dari file lokal `.csv` ke dalam DataFrame menggunakan pustaka `pandas`.

### 2. Assessing Data
Pada tahap ini, kita mengevaluasi kualitas data dengan mengecek:
1. **Tipe Data** masing-masing kolom
2. **Missing Value** (nilai yang hilang)
3. **Data Duplikat**
4. **Inaccurate Value** (nilai tidak akurat / anomali)

#### 📌 Rangkuman Temuan Evaluasi Data (Assessing Data Result)

Berdasarkan pengecekan yang telah dilakukan, berikut adalah ringkasan masalah kualitas data yang ditemukan:

1. **`geolocation_df`**:
   - Terdapat **261,831** data duplikat.
2. **`order_reviews_df`**:
   - Terdapat *missing value* pada kolom `review_comment_title` (87,656) dan `review_comment_message` (58,247).
3. **`orders_df`**:
   - Terdapat *missing value* pada kolom tanggal delivery/approval (`order_approved_at`, `order_delivered_carrier_date`, `order_delivered_customer_date`).
   - Tipe data kolom tanggal masih berbentuk `object`/`string`, perlu diubah menjadi `datetime`.
4. **`products_df`**:
   - Terdapat *missing value* pada kategori produk, deskripsi, dimensi, dan foto.
   - Terdapat *inaccurate value* / anomali pada kolom `product_weight_g`.

### 3. Cleaning Data
Pada tahap ini, kita akan menangani (*handling*) masalah-masalah kualitas data yang telah ditemukan pada proses *Assessing Data* sebelumnya.

**Strategi Pembersihan:**
- **Pembersihan Data Duplikat**: Menghapus baris duplikat pada `geolocation_df`.
- **Handling Missing Values**: Imputasi atau pengananganan nilai yang hilang pada `order_reviews_df`, `orders_df`, dan `products_df`.
- **Fixing Inaccurate Values & Tipe Data**: Penyesuaian nilai anomali berat produk dan konversi tipe data ke format yang sesuai (misal: `datetime`).
