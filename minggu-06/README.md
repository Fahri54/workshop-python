# workshop-python
<h2>Minggu 06</h2>
<b>Nama : Fahri Rahcmad Setyawan</b></br>
<b>NIM : 185410023</b>

# Kesalahan Errors dan Pengecualian exceptions
Sampai sekarang pesan kesalahan belum lebih dari yang disebutkan, tetapi jika Anda telah mencoba contohnya, Anda mungkin telah melihat beberapa. Ada (setidaknya) dua 
jenis kesalahan yang dapat dibedakan: syntax errors dan exceptions.

# 1.	Kesalahan sintaksis
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-06/gambar/1.png"/>

Pengurai parser mengulangi baris yang menyinggung dan menampilkan sedikit 'arrow' yang menunjuk pada titik paling awal di baris di mana kesalahan terdeteksi. Kesalahan
disebabkan oleh (atau setidaknya terdeteksi pada) token preceding panah: dalam contoh, kesalahan terdeteksi pada fungsi print(), karena titik dua (':')) hilang sebelum
itu. Nama file dan nomor baris dicetak sehingga Anda tahu ke mana harus mencari kalau-kalau masukan berasal dari skrip.

# 2.	Pegecualian
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-06/gambar/2.png"/>

Baris terakhir dari pesan kesalahan menunjukkan apa yang terjadi. Pengecualian ada berbagai jenis yang berbeda, dan tipe dicetak sebagai bagian dari pesan: tipe dalam 
contoh adalah ZeroDivisionError, NameError dan TypeError. String yang dicetak sebagai jenis pengecualian adalah nama pengecualian bawaan yang terjadi. Ini berlaku 
untuk semua pengecualian bawaan, tetapi tidak harus sama untuk pengecualian yang dibuat pengguna (meskipun ini adalah konvensi yang bermanfaat). Nama pengecualian 
standar adalah pengidentifikasi bawaan (bukan kata kunci yang dipesan reserved keyword).

Sisa baris menyediakan detail berdasarkan jenis pengecualian dan apa yang menyebabkannya.

# 3.	Menangani pengecualian
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-06/gambar/3.png"/>

Pernyataan try berfungsi sebagai berikut:
- Pertama, try clause (pernyataan(-pernyataan) di antara kata kunci try dan except) dieksekusi.
- Jika tidak ada pengecualian terjadi, except clause dilewati dan eksekusi pernyataan :keyword: try selesai.
- Jika pengecualian terjadi selama eksekusi klausa try, sisa klausa dilewati. Kemudian jika jenisnya cocok dengan pengecualian yang dinamai dengan kata kunci 
- exception, klausa except dioperasikan, dan kemudian eksekusi berlanjut setelah pernyataan try.
- Jika terjadi pengecualian yang tidak cocok dengan pengecualian yang disebutkan dalam klausa kecuali, itu diteruskan ke luar pernyataan try; jika tidak ada 
- penangan yang ditemukan, ini adalah unhandled exception dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.

# 4.	Memunculkan pengecualian
Pernyataan raise memungkinkan programmer untuk memaksa pengecualian yang ditentukan terjadi. Sebagai contoh:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-06/gambar/4.png"/>

# 5.	Pengecualian yang ditentukan pengguna
Program dapat memberi nama pengecualian mereka sendiri dengan membuat kelas pengecualian baru (lihat tut-class untuk informasi lebih lanjut tentang kelas Python). 
Pengecualian biasanya berasal dari kelas Exception, baik secara langsung atau tidak langsung.

Kelas pengecualian dapat didefinisikan yang melakukan apa saja yang dapat dilakukan oleh kelas lain, tetapi biasanya tetap sederhana, seringkali hanya menawarkan 
sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan sebagai pengecualian. Saat membuat modul yang dapat menimbulkan beberapa kesalahan berbeda, praktik yang umum adalah membuat kelas dasar untuk pengecualian yang ditentukan oleh modul itu, dan mensubkelaskan kelas itu untuk membuat kelas pengecualian khusus untuk kondisi kesalahan yang berbeda:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-06/gambar/5.png"/>

# 6.	Mendefinisikan tindakan pembersihan
Pernyataan try memiliki klausa opsional lain yang dimaksudkan untuk menentukan tindakan pembersihan yang harus dijalankan dalam semua keadaan. Sebagai contoh:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-06/gambar/6.png"/>

# 7.	Tindakan pembersihan yang sudah ditentukan
Beberapa objek mendefinisikan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek 
berhasil atau gagal. Lihatlah contoh berikut, yang mencoba membuka berkas dan mencetak isinya ke layar.

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-06/gambar/7.png"/>

Masalah dengan kode ini adalah bahwa ia membiarkan berkas terbuka untuk jumlah waktu yang tidak ditentukan setelah bagian kode ini selesai dieksekusi. Ini bukan 
masalah dalam skrip sederhana, tetapi bisa menjadi masalah untuk aplikasi yang lebih besar. Pernyataan with memungkinkan objek seperti berkas digunakan dengan cara 
yang memastikan mereka selalu dibersihkan secepatnya dan dengan benar.

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-06/gambar/8.png"/>

Masalah dengan kode ini adalah bahwa ia membiarkan berkas terbuka untuk jumlah waktu yang tidak ditentukan setelah bagian kode ini selesai dieksekusi. Ini bukan 
masalah dalam skrip sederhana, tetapi bisa menjadi masalah untuk aplikasi yang lebih besar. Pernyataan with memungkinkan objek seperti berkas digunakan dengan 
cara yang memastikan mereka selalu dibersihkan secepatnya dan dengan benar.
