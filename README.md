# AstaScannerV1

AstaScannerV1 adalah alat pemindaian web yang dirancang untuk mengumpulkan informasi dan melakukan eksploitasi otomatis terhadap situs web. Dibangun menggunakan Python, alat ini dapat digunakan untuk berbagai tujuan, seperti mengumpulkan informasi WHOIS, melakukan pemindaian DNS, mendeteksi CMS atau framework yang digunakan, mencari panel admin, dan melakukan pemindaian dengan alat seperti Nmap dan Nuclei.

## Fitur

- **WHOIS Information**: Mengumpulkan informasi tentang kepemilikan domain dan data terkait lainnya.
- **DNS Lookup**: Melakukan pencarian DNS untuk menemukan alamat IP yang terkait dengan domain target.
- **CMS/Framework Detection**: Menentukan sistem manajemen konten (CMS) atau framework yang digunakan oleh situs web (seperti WordPress, Joomla, Drupal, dll).
- **Admin Panel Finder**: Mencari panel admin yang dapat diakses di situs web target, seperti `/admin`, `/wp-admin`, dll.
- **Nmap Scan**: Melakukan pemindaian port penting untuk mengecek status port terbuka (misalnya port 21, 22, 80, 443, dll.).
- **Nuclei Scan**: Menjalankan pemindaian kerentan dengan Nuclei untuk mendeteksi potensi celah keamanan.
- **Auto Exploit**: Secara otomatis menjalankan eksploitasi terhadap CMS yang terdeteksi (tergantung pada script eksploitasi yang ada).

## Prasyarat

Sebelum menjalankan AstaScannerV1, pastikan Anda memenuhi semua prasyarat berikut:

1. **Python 3.6+** (Disarankan menggunakan venv untuk manajemen lingkungan virtual).
2. **Paket Python yang diperlukan**:
   - `requests`
   - `whois`
   - `nmap`
   - `dns.resolver`
   - `termcolor`
   - `beautifulsoup4`
   - `pyfiglet`
3. **Nmap** dan **Nuclei** harus diinstal di sistem Anda.

## Instalasi

Ikuti langkah-langkah di bawah ini untuk menginstal dan menyiapkan AstaScannerV1:

1. **Clone atau unduh proyek ini**:
   git clone https://github.com/username/asta-scanner.git
   cd asta-scanner
   
2. **(Opsional) Buat dan aktifkan lingkungan virtual**:
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   
3. **Instal dependensi yang diperlukan**:
   pip install -r requirements.txt

Penggunaan
Setelah instalasi selesai, Anda dapat menjalankan AstaScannerV1 dengan mengikuti langkah-langkah berikut:

Jalankan skrip asta.py:

bash
Salin
Edit
python asta.py
Masukkan domain atau IP target yang ingin Anda pindai dan pilih protokol yang sesuai (http atau https).

Penjelasan Fitur
WHOIS Information: Alat ini dapat membantu Anda mendapatkan informasi tentang siapa yang memiliki domain dan informasi terkait lainnya seperti alamat email atau kontak administratif.

DNS Lookup: Memungkinkan Anda untuk memeriksa alamat IP yang terkait dengan domain target, berguna untuk pemetaan jaringan atau analisis lebih lanjut.

CMS/Framework Detection: AstaScannerV1 dapat mendeteksi apakah situs web menggunakan CMS atau framework tertentu (misalnya, WordPress, Joomla, atau Drupal).

Admin Panel Finder: Fitur ini mencari URL yang sering digunakan untuk panel admin, seperti /admin atau /wp-admin, untuk mengekspos kemungkinan titik masuk ke sistem.

Nmap Scan: AstaScannerV1 dapat menjalankan pemindaian port dengan Nmap untuk menemukan port penting yang terbuka, seperti port untuk SSH, HTTP, HTTPS, dan FTP.

Nuclei Scan: Pemindaian kerentan menggunakan Nuclei untuk menemukan potensi kerentanannya berdasarkan template eksploitasi yang sudah ada.

Auto Exploit: Ketika CMS terdeteksi, AstaScannerV1 dapat mencoba untuk mengeksekusi eksploitasi otomatis terhadap CMS tersebut, jika script eksploitasi sudah tersedia.

Catatan
Izin: Pastikan Anda memiliki izin eksplisit untuk melakukan pemindaian terhadap situs web yang Anda tuju. Melakukan pemindaian tanpa izin dapat melanggar hukum.

Penggunaan Etis: Gunakan alat ini secara etis dan hanya untuk tujuan yang sah, seperti uji penetrasi dengan izin atau penelitian keamanan.

Ketersediaan Dependensi: Pastikan bahwa semua dependensi yang diperlukan sudah terinstal dengan benar sebelum menjalankan alat ini.

Kontribusi
Jika Anda tertarik untuk berkontribusi pada pengembangan AstaScannerV1, Anda dapat mengajukan pull request atau melaporkan bug dengan membuka issue.

Cara Berkontribusi:
Fork repositori ini.

Buat branch baru untuk fitur atau perbaikan Anda (git checkout -b feature/your-feature).

Lakukan perubahan yang diperlukan.

Commit perubahan Anda (git commit -am 'Add new feature').

Push ke branch tersebut (git push origin feature/your-feature).

Buka pull request di GitHub.

Lisensi
Proyek ini dilisensikan di bawah MIT License. Lihat file LICENSE untuk detail lebih lanjut.

Catatan: Jika ada fitur tambahan atau pertanyaan lebih lanjut, jangan ragu untuk membuka issue di repositori ini!

