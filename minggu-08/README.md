# workshop-python
<h2>Minggu 08</h2>
<b>Nama : Fahri Rahcmad Setyawan</b></br>
<b>NIM : 185410023</b>

# PUSTAKA STANDAR PYTHON
# 1.	Antarmuka Sistem Operasi
Modul os menyediakan puluhan fungsi untuk berinteraksi dengan sistem operasi:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-08/gambar/1.png"/>

Pastikan untuk menggunakan gaya import os alih-alih from os import *. Ini akan menjaga os.open() dari membayangi shadowing fungsi bawaan open() yang beroperasi jauh berbeda.

# 2.	Berkas Wildcard
Modul glob menyediakan fungsi untuk membuat daftar berkas dari pencarian wildcard di direktori:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-08/gambar/2.png"/>

# 3.	Baris Perintah Berargumen
Skrip utilitas umum seringkali perlu memproses argumen baris perintah. Argumen-argumen ini disimpan dalam atribut argv dari modul sys sebagai daftar. Sebagai contoh, 
hasil keluaran berikut dari menjalankan python demo.py one two three di baris perintah
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-08/gambar/3.png"/>

# 4.	Pengalihan Ouput Kesalahan dan Pengakhiran Program
Modul sys juga memiliki atribut untuk stdin, stdout, dan stderr. Yang terakhir berguna untuk mengirimkan peringatan dan pesan kesalahan untuk membuatnya terlihat 
bahkan ketika stdout telah dialihkan:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-08/gambar/4.png"/>

Cara paling langsung untuk mengakhiri skrip adalah dengan menggunakan sys.exit().

# 5.	Pencocokan Pola String
Modul re menyediakan alat ekspresi reguler untuk pemrosesan string lanjutan. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang 
ringkas dan dioptimalkan:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-08/gambar/5.png"/>

# 6.	Matematika
Modul math memberikan akses ke fungsi-fungsi pustaka C yang mendasari untuk matematika angka pecahan floating point:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-08/gambar/6.png"/>

# 7.	Akses Internet
Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua yang paling sederhana adalah urllib.request untuk mengambil data dari URL dan smtplib 
untuk mengirim email:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-08/gambar/7.png"/>

# 8.	Tanggal dan Waktu
Modul datetime menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana dan kompleks. Sementara aritmatika tanggal dan waktu didukung, fokus 
implementasi adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi keluaran. Modul ini juga mendukung objek yang sadar zona waktu.
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-08/gambar/8.png"/>

# 9.	Kompresi Data
Format pengarsipan dan kompresi data umum didukung langsung oleh modul-modul yang ada antara lain: :mod: zlib, gzip, bz2, lzma, zipfile dan tarfile.
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-08/gambar/9.png"/>

# 10.	Pengukuran Kinerja
Python menyediakan alat pengukuran yang segera menjawab pertanyaan-pertanyaan itu.
Misalnya, mungkin tergoda untuk menggunakan fitur tuple packing dan unpacking daripada pendekatan tradisional untuk bertukar argumen. Modul :mod: timeit dengan cepat 
menunjukkan keunggulan kinerja secara sederhana:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-08/gambar/10.png"/>
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-08/gambar/11.png"/>

# 11.	Kontrol Kualitas
Salah satu pendekatan untuk mengembangkan perangkat lunak berkualitas tinggi adalah dengan menulis tes untuk setiap fungsi yang dikembangkan dan untuk sering 
menjalankan tes tersebut selama proses pengembangan.

Modul: mod:doctest menyediakan alat untuk memindai modul dan memvalidasi tes yang tertanam dalam dokumen program. Konstruksi pengujian sesederhana memotong dan 
menempel panggilan khas beserta hasilnya ke dalam docstring. Ini meningkatkan dokumentasi dengan memberikan contoh kepada pengguna dan memungkinkan modul doctest 
untuk memastikan kode tetap benar untuk dokumentasi:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-08/gambar/12.png"/>

# 12.	Dilengkapi Baterai
Python memiliki filosofi "dilengkapi baterai". Ini paling baik dilihat melalui kemampuan yang canggih dan kuat robust dengan dukungan paket-paket yang lebih besar. 
Sebagai contoh:
- Modul xmlrpc.client dan xmlrpc.server membuat penerapan panggilan prosedur jarak jauh menjadi tugas yang hampir sepele. Terlepas dari nama-nama modul, tidak 
diperlukan pengetahuan atau penanganan XML secara langsung.
- Paket email adalah pustaka untuk mengelola pesan email, termasuk MIME dan lainnya RFC 2822 dokumen pesan berbasis. Tidak seperti smtplib dan poplib yang 
benar-benar mengirim dan menerima pesan, paket email memiliki toolset lengkap untuk membangun atau mendekodekan struktur pesan kompleks (termasuk lampiran) dan 
untuk mengimplementasikan pengkodean internet dan protokol header.
- Paket json menyediakan dukungan kuat untuk mengurai format pertukaran data populer ini. Modul csv mendukung pembacaan dan penulisan berkas secara langsung 
dalam format Nilai Terpisah-Koma atau CSV, umumnya didukung oleh database dan spreadsheet. Pemrosesan XML didukung oleh paket xml.etree.ElementTree, xml.dom dan 
xml.sax. Bersama-sama, modul dan paket ini sangat menyederhanakan pertukaran data antara aplikasi Python dan alat lainnya.
- Modul sqlite3 adalah pembungkus untuk pustaka basis data SQLite, menyediakan basis data persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL 
yang sedikit tidak standar.
- Internasionalisasi didukung oleh sejumlah modul termasuk paket gettext, locale, dan codecs.
