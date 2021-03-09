# workshop-python
<h2>Minggu 05</h2>
<b>Nama : Fahri Rahcmad Setyawan</b></br>
<b>NIM : 185410023</b>

# Input atau Ouput pada Python
Pada Input atau Output ada beberapa cara untuk mempresentasikan keluaran suatu program; data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke 
berkas untuk digunakan di masa mendatang. Bab ini akan membahas beberapa kemungkinan.
# 1.	Pemformatan Keluaran yang Lebih Menarik
Sejauh ini kami telah menemukan dua cara penulisan nilai: expression statements dan fungsi print(). (Cara ketiga menggunakan write() metode objek berkas; berkas 
standar keluaran dapat dirujuk sebagai sys.stdout.
Fungsi str() dimaksudkan untuk mengembalikan representasi nilai-nilai yang terbaca oleh manusia, sementara repr() dimaksudkan untuk menghasilkan representasi 
yang dapat dibaca oleh penerjemah (atau akan memaksa SyntaxError jika tidak ada sintaks yang setara). Untuk objek yang tidak memiliki representasi khusus untuk 
konsumsi manusia, str() akan mengembalikan nilai yang sama dengan repr(). Banyak nilai, seperti angka atau struktur seperti daftar dan kamus, memiliki representasi 
yang sama menggunakan kedua fungsi tersebut. String, khususnya, memiliki dua representasi berbeda.
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-05/gambar/1.png"/>

# a.	Literal String Terformat
Formatted string literals (juga disebut f-string) memungkinkan Anda menyertakan nilai ekspresi Python di dalam string dengan mengawali string dengan f atau F dan 
menulis ekspresi sebagai {expression}.
Pada penentu format opsional dapat mengikuti ekspresi. Ini memungkinkan kontrol yang lebih besar atas bagaimana nilai diformat. Contoh berikut ini pembulatan pi 
ke tiga tempat setelah desimal:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-05/gambar/2.png"/>

# b.	Metode String format()
Penggunaan dasar metode str.format() terlihat seperti ini:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-05/gambar/3.png"/>

Tanda kurung dan karakter di dalamnya (disebut fields format) diganti dengan objek yang diteruskan ke metode str.format().

# c.	Pemformatan String Manual
Inilah tabel kotak dan kubus yang sama, yang diformat secara manual:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-05/gambar/4.png"/>

(Perhatikan bahwa satu spasi di antara setiap kolom ditambahkan dengan cara print() berfungsi: selalu menambah spasi di antara argumennya.)

# d.	Pemformatan String Lama
Operator% (modulo) juga dapat digunakan untuk pemformatan string. Diberikan nilai% 'string', contoh% dalam string diganti dengan nol atau lebih elemen nilai. 
Operasi ini umumnya dikenal sebagai interpolasi string. Sebagai contoh:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-05/gambar/5.png"/>

# 2.	Membaca dan Menulis Berkas
open() mengembalikan sebuah file object, dan paling umum digunakan dengan dua argumen: open(filename, mode).
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-05/gambar/6.png"/>

Argumen pertama adalah string yang berisi nama file. Argumen kedua adalah string lain yang berisi beberapa karakter yang menggambarkan cara berkas akan digunakan. 
mode dapat 'r' ketika file hanya akan dibaca, 'w' untuk hanya menulis (berkas yang ada dengan nama yang sama akan dihapus), dan 'a' membuka berkas untuk ditambahkan;
setiap data yang ditulis ke file secara otomatis ditambahkan ke bagian akhir. 'r+' membuka berkas untuk membaca dan menulis. Argumen mode adalah opsional; 'r' akan 
diasumsikan jika dihilangkan.
Biasanya, file dibuka di text mode, yang berarti, Anda membaca dan menulis string dari dan ke file, yang dikodekan dalam pengkodean tertentu. Jika pengkodean tidak 
ditentukan, standarnya adalah bergantung platform (lihat :func: open). 'b' ditambahkan ke mode membuka berkas di binary mode: sekarang data dibaca dan ditulis dalam 
bentuk objek byte. Mode ini harus digunakan untuk semua file yang tidak mengandung teks.

# a.	Metode Objek Berkas
Untuk membaca konten file, panggil f.read(size), yang membaca sejumlah kuantitas data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam 
mode biner). size adalah argumen numerik opsional. Ketika size dihilangkan atau negatif, seluruh isi file akan dibaca dan dikembalikan; itu masalah Anda jika file 
tersebut dua kali lebih besar dari memori mesin Anda. Kalau tidak, paling banyak size karakter (dalam mode teks) atau size byte (dalam mode biner) dibaca dan 
dikembalikan. Jika akhir file telah tercapai, f.read() akan mengembalikan string kosong ('').
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-05/gambar/7.png"/>

# b.	Menyimpan Data Terstruktur dengan Json
String dapat dengan mudah ditulis dan dibaca dari file. Angka membutuhkan sedikit usaha, karena metode read() hanya mengembalikan string, yang harus diteruskan ke 
fungsi seperti int(), yang mengambil string seperti '123' dan mengembalikan nilai numerik 123. Ketika Anda ingin menyimpan tipe data yang lebih kompleks seperti 
daftar list dan dictionary bersarang, penguraian dan pembuatan serialisasi dengan tangan menjadi rumit. Jika Anda memiliki objek x, Anda dapat melihat representasi 
string JSON dengan baris kode sederhana:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-05/gambar/8.png"/>
