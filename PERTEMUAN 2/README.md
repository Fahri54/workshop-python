# workshop-python
<h2>Minggu 02</h2>
<b>Nama : Fahri Rahcmad Setyawan</b></br>
<b>NIM : 185410023</b>

# PENGENDALIAN ALIRAN PROGRAM

# A. Banyak alat pengatur aliran control flow
Yang mana selain pernyataan while yang baru saja diperkenalkan, bahasa Python menggunakan pernyataan 
kontrol aliran biasa yang dikenal dari bahasa lain, dengan beberapa perubahan.

# B.	If statements
<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/1.png"/>
Pada bagian elif ada nol atau lebih bagian elif, dan pada bagian else yaitu opsional. Pada kata kunci 
‘elif’ adalah kependekan dari ‘else if’ dan berguna untuk menghindari indentasi yang berlebihan. Yang 
mana pada if, elif, adalah urutan pengganti untuk pernyataan switch atau case yang ditemukan dalam bahasa lain.

# C.	For statements
<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/2.png"/>
Pada for statements ini memodifikasi koleksi collection sambil mengulangi koleksi yang sama bisa sulit 
diperbaiki. Biasanya untuk mengganti lebih mudah untuk mengulang salinan koleksi atau membuat koleksi baru.

# D.	Fungsi range
<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/3.png"/>
-	Pada hasil yang ditampilkan yaitu urutan pregressions aritmatika

<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/4.png"/>
-	Pada range (5,10) menghasilkan 5 sampai 9 yang mana indeks sah legal untuk item dengan urutan panjang sampai 
10 dan nilai 10 tidak tertampil.

<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/5.png"/>
<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/6.png"/>
-	Yang mana akan dibiarkan rentang mulai dari nomor lain, lalu untuk menentukan kenaikan yang berbeda.

<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/7.png"/>
-	Selanjutnya jika akan beralih pada indeks urutan, dapat menggabungkan range() dan len() sebagi berikut

# E.	Pernyataan break dan continue, dan else klausa pada perulangan Loops
<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/8.png"/>
Pada pernyataan perulangan loop mungkin memiliki klausa else: itu dieksekusi ketika loop berakhir melalui 
selesainya exhaustion iterable (dengan for) atau ketika kondisi menjadi salah (dengan while), tetapi tidak 
ketika loop diakhiri oleh pernyataan break. Ini dicontohkan oleh perulangan berikut, yang mencari bilangan prima:

<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/9.png"/>
Ketika digunakan dengan sebuah perulangan, klausa else memiliki lebih banyak kesamaan dengan klausa else dari 
pernyataan try dibandingkan dengan pernyataan if: sebuah klausa else pernyataan try berjalan ketika tidak ada 
pengecualian terjadi, dan klausa else perulangan berjalan ketika tidak ada break terjadi.

# F.	Pass statements
<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/10.png"/>
Pada pass statements tidak terjadi hasil apa-apa yang mana ini dapat digunakan ketika pernyataan diperlukan 
secara sintaksis tetapi program tidak memerlukan tindakan. 

# G.	Mendesfinisikan fungsi
<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/11.png"/>
Pada kata kunci def memperkenalkan fungsi definition. Itu harus diikuti oleh nama fungsi dan daftar parameter 
formal yang di dalam tanda kurung. Pernyataan yang membentuk tubuh fungsi mulai dari baris berikutnya, dan harus diberi indentasi.

Pada hasil di bawah sangat mudah untuk menulis fungsi yang mengembalikan daftar list nomor seri Fibonacci, alih-alih mencetaknya:
<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/12.png"/>

# H.	Lebih lanjut tentang fungsi
<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/13.png"/>
-	Merupakan argument bawaan

<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/14.png"/>
-	Merupakan argument kata kunci keyword 

<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/15.png"/>
-	Merupakan parameter spesial 

<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/16.png"/>
-	Merupakan daftar argument yang dapat berubah ubah arbitrary 

<img src="https://github.com/Fahri54/workshop-python/blob/main/PERTEMUAN%202/gambar/17.png"/>
-	Merupakan pembukaan paket unpacking daftar argumen 
