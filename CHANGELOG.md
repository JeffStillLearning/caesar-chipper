# 📝 Caesar Cipher - Changelog

## 🔧 Perbaikan Terbaru (v1.1)

### ✅ **Issue #1: Input Text Tidak Clear Saat Switch Mode**
**Masalah**: Saat berpindah dari encrypt ke decrypt, text di input field masih tersimpan.

**Solusi**: 
- Input field sekarang otomatis di-clear saat switch mode
- Muncul notifikasi: "Switched to [mode] mode. Enter new text to process."

**File yang diubah**: `static/script.js` - fungsi `setMode()`

### ✅ **Issue #2: Brute Force Display Membingungkan**
**Masalah**: User bingung dengan tampilan "Shift 1" di brute force, mengira itu hasil dari encrypt shift 1.

**Solusi**:
- Ubah label dari "Shift X" menjadi "Key X" 
- Tambah hint text "(decrypt key: X)"
- Tambah penjelasan di atas hasil brute force
- Perbaiki pesan toast saat menggunakan hasil

**File yang diubah**: 
- `static/script.js` - fungsi `displayBruteForceResults()`
- `templates/index.html` - tambah penjelasan brute force

### 🎯 **Behavior Sekarang:**

#### Mode Switching:
1. **Encrypt Mode** → **Decrypt Mode**:
   - ✅ Input field di-clear
   - ✅ Output field di-clear  
   - ✅ Muncul toast notification
   - ✅ User harus input text baru

2. **Decrypt Mode** → **Encrypt Mode**:
   - ✅ Input field di-clear
   - ✅ Output field di-clear
   - ✅ Muncul toast notification
   - ✅ User harus input text baru

#### Brute Force Analysis:
- ✅ Label "Key X" lebih jelas dari "Shift X"
- ✅ Hint text menjelaskan bahwa itu decrypt key
- ✅ Penjelasan di atas hasil: "Click on any result to use it"
- ✅ Toast message lebih informatif saat menggunakan hasil

### 🧪 **Cara Test:**

#### Test 1: Mode Switching
```
1. Masukkan text "Hello" di mode Encrypt
2. Klik tombol "Decrypt" 
3. Expected: Input kosong + toast "Switched to decrypt mode..."
4. Masukkan text baru untuk decrypt
```

#### Test 2: Brute Force Clarity  
```
1. Encrypt "Hello" dengan shift 3 → hasil "Khoor"
2. Input "Khoor" dan klik "Brute Force"
3. Expected: Melihat "Key 3: Hello" sebagai jawaban yang benar
4. Klik pada "Key 3: Hello"
5. Expected: Hasil di-copy ke output + toast informatif
```

### 📊 **Penjelasan Brute Force Logic:**

**Contoh**: Text "Hello" di-encrypt dengan shift 3 → "Khoor"

Brute force akan mencoba semua kemungkinan decrypt key:
- Key 1: Jgnnq (salah)
- Key 2: Ifmmp (salah)  
- **Key 3: Hello** ✅ (benar - ini decrypt key yang tepat)
- Key 4: Gdkkn (salah)
- dst...

**Key 3** artinya: "Gunakan shift 3 untuk decrypt 'Khoor' kembali ke 'Hello'"

### 🎉 **Status:**
- ✅ Input clearing saat switch mode: **FIXED**
- ✅ Brute force display clarity: **IMPROVED** 
- ✅ User experience: **ENHANCED**

---

## 📋 **Previous Changes (v1.0)**

### ✅ **Issue: Real-time Processing**
- Disabled auto-processing saat mengetik
- Tombol Encrypt/Decrypt sekarang berfungsi dengan benar
- Output hanya muncul setelah klik tombol

### ✅ **Issue: Shift Value Changes**
- Output di-clear saat mengubah shift value
- User harus klik process lagi untuk melihat hasil baru

---

**🔐 Caesar Cipher Web App - Always Improving!**
