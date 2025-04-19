```markdown
# AstaScannerV1 🚀

**AstaScannerV1** adalah alat pemindaian web yang dirancang untuk mengumpulkan informasi dan melakukan eksploitasi otomatis terhadap situs web. Dibangun menggunakan Python, alat ini dapat digunakan untuk berbagai tujuan seperti mengumpulkan informasi WHOIS, melakukan pemindaian DNS, mendeteksi CMS atau framework yang digunakan, mencari panel admin, serta melakukan pemindaian dengan alat seperti Nmap dan Nuclei.

🔍 **AstaScannerV1** cocok untuk profesional keamanan siber, penguji penetrasi, dan pengembang yang ingin memetakan dan mengidentifikasi potensi kerentanannya dengan cepat.

## Fitur 🎯

- **WHOIS Information**: Mengumpulkan informasi tentang kepemilikan domain dan data terkait lainnya.
- **DNS Lookup**: Melakukan pencarian DNS untuk menemukan alamat IP yang terkait dengan domain target.
- **CMS/Framework Detection**: Menentukan sistem manajemen konten (CMS) atau framework yang digunakan oleh situs web (misalnya WordPress, Joomla, Drupal, dll).
- **Admin Panel Finder**: Mencari panel admin yang dapat diakses di situs web target, seperti `/admin`, `/wp-admin`, dll.
- **Nmap Scan**: Melakukan pemindaian port untuk mengecek status port terbuka (misalnya port 21, 22, 80, 443, dll.).
- **Nuclei Scan**: Menjalankan pemindaian kerentan dengan Nuclei untuk mendeteksi potensi celah keamanan.
- **Auto Exploit**: Secara otomatis menjalankan eksploitasi terhadap CMS yang terdeteksi (tergantung pada script eksploitasi yang ada).

## Prasyarat ⚙️

Pastikan Anda memenuhi semua prasyarat berikut sebelum menjalankan **AstaScannerV1**:

- **Python 3.6+** (Disarankan menggunakan `venv` untuk manajemen lingkungan virtual).
- **Paket Python yang diperlukan**:
  - `requests`
  - `whois`
  - `nmap`
  - `dns.resolver`
  - `termcolor`
  - `beautifulsoup4`
  - `pyfiglet`
- **Nmap** dan **Nuclei** harus diinstal di sistem Anda.

## Instalasi 🔧

Ikuti langkah-langkah di bawah ini untuk menginstal dan menyiapkan **AstaScannerV1**:

1. **Clone atau unduh proyek ini**:

    ```bash
    git clone https://github.com/username/asta-scanner.git
    cd asta-scanner
    ```

2. **(Opsional) Buat dan aktifkan lingkungan virtual**:

    - **Linux/macOS**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    - **Windows**:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Instal dependensi yang diperlukan**:

    ```bash
    pip install -r requirements.txt
    ```

## Penggunaan 💻

Setelah instalasi selesai, Anda dapat menjalankan **AstaScannerV1** dengan mengikuti langkah-langkah berikut:

1. Jalankan skrip `asta.py`:

    ```bash
    python asta.py
    ```

2. Masukkan **domain** atau **IP** target yang ingin Anda pindai dan pilih protokol yang sesuai (`http` atau `https`).

## Penjelasan Fitur 📝

### 1. WHOIS Information

Alat ini mengumpulkan informasi tentang siapa yang memiliki domain dan informasi terkait lainnya, seperti alamat email atau kontak administratif. Sangat berguna untuk mendapatkan gambaran tentang pemilik situs.

### 2. DNS Lookup

Memungkinkan Anda untuk memeriksa alamat IP yang terkait dengan domain target. Ini penting untuk pemetaan jaringan atau analisis lebih lanjut mengenai konfigurasi server.

### 3. CMS/Framework Detection

AstaScannerV1 dapat mendeteksi apakah situs web menggunakan CMS atau framework tertentu (seperti WordPress, Joomla, atau Drupal). Ini membantu mengidentifikasi teknologi yang digunakan dan potensi kerentanannya.

### 4. Admin Panel Finder

Fitur ini mencari URL yang sering digunakan untuk panel admin, seperti `/admin` atau `/wp-admin`, untuk mengekspos kemungkinan titik masuk ke sistem.

### 5. Nmap Scan

Melakukan pemindaian port untuk menemukan port penting yang terbuka, seperti port untuk SSH, HTTP, HTTPS, dan FTP. Ini dapat membantu dalam menemukan layanan yang berjalan pada server target.

### 6. Nuclei Scan

Pemindaian kerentan menggunakan **Nuclei** untuk mendeteksi potensi kerentanannya berdasarkan template eksploitasi yang sudah ada.

### 7. Auto Exploit

Ketika CMS terdeteksi, AstaScannerV1 dapat mencoba untuk mengeksekusi eksploitasi otomatis terhadap CMS tersebut, jika skrip eksploitasi sudah tersedia di dalam alat.

## Catatan ⚠️

- **Izin**: Pastikan Anda memiliki izin eksplisit untuk melakukan pemindaian terhadap situs web yang Anda tuju. Melakukan pemindaian tanpa izin dapat melanggar hukum.
- **Penggunaan Etis**: Gunakan alat ini secara etis dan hanya untuk tujuan yang sah, seperti uji penetrasi dengan izin atau penelitian keamanan.
- **Ketersediaan Dependensi**: Pastikan bahwa semua dependensi yang diperlukan sudah terinstal dengan benar sebelum menjalankan alat ini.

## Kontribusi 🤝

Jika Anda tertarik untuk berkontribusi pada pengembangan **AstaScannerV1**, Anda dapat mengajukan **pull request** atau melaporkan bug dengan membuka **issue**.

### Cara Berkontribusi:

1. Fork repositori ini.
2. Buat branch baru untuk fitur atau perbaikan Anda:

    ```bash
    git checkout -b feature/your-feature
    ```

3. Lakukan perubahan yang diperlukan.
4. Commit perubahan Anda:

    ```bash
    git commit -am 'Add new feature'
    ```

5. Push ke branch tersebut:

    ```bash
    git push origin feature/your-feature
    ```

6. Buka **pull request** di GitHub.

## Lisensi 📄

Proyek ini dilisensikan di bawah **MIT License**. Lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.
```
