# 🔐 Caesar Cipher Web Application

Aplikasi web interaktif untuk enkripsi dan dekripsi menggunakan Caesar Cipher dengan UI yang menarik dan modern.

## ✨ Fitur

- **Enkripsi & Dekripsi**: Mudah beralih antara mode encrypt dan decrypt
- **Shift Slider**: Kontrol shift value dari 1-25 dengan slider interaktif
- **Real-time Processing**: Hasil langsung terlihat saat mengetik
- **Brute Force Analysis**: Coba semua kemungkinan shift untuk dekripsi
- **Copy to Clipboard**: Salin hasil dengan satu klik
- **Responsive Design**: Tampil sempurna di desktop dan mobile
- **Keyboard Shortcuts**: Shortcut untuk akses cepat
- **Animasi Smooth**: Transisi dan animasi yang halus
- **Toast Notifications**: Feedback visual untuk setiap aksi

## 🚀 Cara Menjalankan

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Jalankan Aplikasi
```bash
python app.py
```

### 3. Buka Browser
Aplikasi akan berjalan di: `http://localhost:5000`

## 🎮 Keyboard Shortcuts

- `Ctrl + E`: Switch ke mode Encrypt
- `Ctrl + D`: Switch ke mode Decrypt  
- `Ctrl + Enter`: Process text
- `Ctrl + B`: Brute force analysis
- `Ctrl + L`: Clear all text

## 🔧 Cara Menggunakan

1. **Pilih Mode**: Klik tombol "Encrypt" atau "Decrypt"
2. **Masukkan Text**: Ketik pesan yang ingin diproses
3. **Atur Shift**: Gunakan slider untuk mengatur nilai shift (1-25)
4. **Process**: Klik tombol "Encrypt/Decrypt" atau gunakan Ctrl+Enter
5. **Copy Result**: Klik tombol copy untuk menyalin hasil

### Brute Force Analysis
Jika Anda memiliki teks terenkripsi dan tidak tahu shift value-nya:
1. Masukkan teks terenkripsi
2. Klik tombol "Brute Force"
3. Lihat semua kemungkinan dekripsi
4. Klik hasil yang paling masuk akal

## 📁 Struktur Project

```
caesar-cipher/
├── app.py              # Flask application
├── caesar_cipher.py    # Caesar cipher logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Main HTML template
├── static/
│   ├── style.css      # CSS styling
│   └── script.js      # JavaScript functionality
└── README.md          # Documentation
```

## 🎨 Teknologi yang Digunakan

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS dengan Flexbox & Grid
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins)

## 🔒 Tentang Caesar Cipher

Caesar Cipher adalah salah satu teknik enkripsi tertua dan paling sederhana. Teknik ini bekerja dengan menggeser setiap huruf dalam alfabet dengan jumlah posisi yang tetap.

**Contoh dengan shift 3:**
- A → D
- B → E  
- C → F
- ...
- X → A
- Y → B
- Z → C

## 🎯 Fitur Tambahan

- **Case Preservation**: Huruf besar/kecil tetap dipertahankan
- **Non-alphabetic Characters**: Angka, spasi, dan simbol tidak berubah
- **Input Validation**: Validasi input untuk mencegah error
- **Error Handling**: Penanganan error yang user-friendly
- **Loading States**: Indikator loading untuk feedback visual

## 🐛 Troubleshooting

Jika mengalami masalah:

1. **Port sudah digunakan**: Ubah port di `app.py` atau hentikan aplikasi lain
2. **Module not found**: Pastikan sudah install dependencies dengan `pip install -r requirements.txt`
3. **Browser tidak terbuka**: Buka manual di `http://localhost:5000`

## 📝 License

Project ini dibuat untuk tujuan edukasi dan pembelajaran kriptografi.

---

**Selamat menggunakan Caesar Cipher! 🎉**
