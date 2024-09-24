# Engene's Rental Car

**Engene's Rental Car** adalah sebuah sistem manajemen rental mobil berbasis Python yang dirancang untuk memudahkan pengelolaan mobil, pemesanan, riwayat penyewaan, dan membership. Sistem ini dilengkapi dengan berbagai fitur yang memudahkan operasional rental mobil.

## Fitur Utama

1. **Sistem Login Admin**: Hanya pengguna yang terotorisasi yang dapat mengakses sistem menggunakan nama dan password.
2. **Menampilkan Daftar Mobil**: Menampilkan daftar mobil lengkap dengan detail seperti model, tahun, warna, plat nomor, merk, transmisi, jumlah penumpang, dan harga sewa harian.
3. **Menambah Mobil Baru**: Admin dapat menambah mobil baru dengan data lengkap, termasuk model, tahun produksi, plat nomor, merk, dan harga sewa harian.
4. **Mengedit Data Mobil**: Admin dapat mengubah informasi mobil yang telah terdaftar.
5. **Pemesanan Mobil**: Pengguna dapat memesan mobil dengan durasi tertentu, dan jika terdaftar sebagai member, pengguna akan mendapatkan diskon 30%.
6. **Riwayat Penyewaan**: Menampilkan riwayat penyewaan mobil oleh pelanggan.
7. **Pendaftaran Membership**: Pelanggan dapat mendaftar sebagai member untuk mendapatkan diskon saat melakukan penyewaan mobil.
8. **Menghapus Mobil**: Admin dapat menghapus mobil yang telah terdaftar dari sistem.

## Panduan Penggunaan

### 1. Login Admin
Setelah menjalankan program, Anda akan diminta untuk login menggunakan nama dan password. Hanya admin yang memiliki akses ke sistem ini.

### 2. Menu Utama
Setelah login berhasil, Anda akan dihadapkan dengan beberapa opsi menu:
- **1**: Menampilkan daftar mobil yang tersedia.
- **2**: Menambah data mobil baru.
- **3**: Mengedit data mobil yang tersedia.
- **4**: Booking mobil.
- **5**: Menampilkan riwayat peminjaman mobil.
- **6**: Mendaftarkan pelanggan sebagai member.
- **7**: Menghapus mobil.
- **8**: Keluar dari sistem.

### 3. Menambahkan Mobil Baru
Untuk menambah mobil baru, admin harus mengisi informasi berikut:
- **Model Mobil**
- **Tahun Produksi**
- **Warna**
- **Plat Nomor**
- **Merk**
- **Transmisi**
- **Jumlah Penumpang**
- **Harga Sewa Harian**

### 4. Mengedit Mobil
Admin dapat mengedit detail mobil yang sudah terdaftar dengan memasukkan model dan plat nomor mobil yang ingin diedit.

### 5. Pemesanan Mobil
Pengguna dapat memesan mobil yang tersedia dengan informasi berikut:
- **Nama Penyewa**
- **NIK**
- **Alamat**
- **Nomor Telepon**
- **Email**
- **Durasi Penyewaan**
- **Mobil yang ingin disewa**

Jika pengguna adalah member, diskon 30% akan otomatis diterapkan pada total biaya penyewaan.

### 6. Riwayat Penyewaan
Menampilkan riwayat penyewaan mobil yang telah dilakukan oleh para pelanggan.

### 7. Menghapus Mobil
Admin dapat menghapus mobil dari sistem dengan mengisi model dan plat nomor mobil yang ingin dihapus.

## Dependencies

Untuk menjalankan program ini, Anda perlu menginstal beberapa paket Python berikut:
- **PrettyTable**: Untuk menampilkan data dalam bentuk tabel.
- **Colorama**: Untuk memberikan warna pada output di terminal.
- **Datetime**: Untuk mengelola data tanggal.

### Cara Instalasi Dependencies

Jalankan perintah berikut untuk menginstal dependencies yang dibutuhkan:

```bash
pip install prettytable colorama

