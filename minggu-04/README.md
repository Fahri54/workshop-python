# workshop-python
<h2>Minggu 04</h2>
<b>Nama : Fahri Rahcmad Setyawan</b></br>
<b>NIM : 185410023</b>

# Modul pada Pyhton
Pada modul python ini jika anda berhenti dari interpreter Python dan memasukkannya lagi, definisi yang anda buat (fungsi dan variabel) 
akan hilang. Karena itu, jika anda ingin menulis program yang agak lebih panjang, anda lebih baik menggunakan editor teks untuk menyiapkan 
input bagi penerjemah dan menjalankannya dengan file itu sebagai input. Ini dikenal sebagai membuat script. Saat program anda menjadi lebih 
panjang, Anda mungkin ingin membaginya menjadi beberapa file untuk pengelolaan yang lebih mudah. Anda mungkin juga ingin menggunakan fungsi 
praktis yang anda tulis di beberapa program tanpa menyalin definisi ke setiap program. Untuk mendukung ini, Python memiliki cara untuk meletakkan 
definisi dalam file dan menggunakannya dalam skrip atau dalam contoh interaktif dari interpreter.

Modul adalah file yang berisi definisi dan pernyataan Python. Nama berkas adalah nama modul dengan akhiran .py diakhirnya. Dalam sebuah modul, nama 
modul (sebagai string) tersedia sebagai nilai variabel global __name__. Misalnya, gunakan editor teks favorit Anda untuk membuat bernama bernama 
fibo.py di direktori saat ini dengan konten berikut:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-04/gambar/1.png"/>

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-04/gambar/2.png"/>

# 1.	Lebih lanjut tentang Modul
Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Mereka dieksekusi 
hanya first kali nama modul ditemui dalam pernyataan impor. 1 (Mereka juga dijalankan jika file dieksekusi sebagai skrip.)

Setiap modul memiliki tabel simbol pribadi sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. Dengan 
demikian, penulis modul dapat menggunakan variabel global dalam modul tanpa khawatir tentang bentrokan tidak disengaja dengan variabel global pengguna. 
Di sisi lain, jika anda tahu apa yang anda lakukan, anda dapat menyentuh variabel global modul dengan notasi yang sama yang digunakan untuk merujuk ke 
fungsinya, modname.itemname.

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-04/gambar/3.png"/>

Ini mengimpor semua nama kecuali yang dimulai dengan garis bawah (_). Dalam kebanyakan kasus, programmer Python tidak menggunakan fasilitas ini karena 
ia memperkenalkan sekumpulan nama yang tidak diketahui ke dalam interpreter, mungkin menyembunyikan beberapa hal yang sudah anda definisikan.

# a.	Mengoperasikan modul sebagai skrip
Ketika anda mengoperasikan modul Python yaitu dengan berikut:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-04/gambar/4.png"/>
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-04/gambar/5.png"/>
Kode diatas dalam modul akan dieksekusi, sama seperti jika anda mengimpornya, tetapi dengan __name__ diatur ke "__main__". Itu berarti bahwa dengan 
menambahkan kode ini di akhir modul anda.

# b.	Jalur pencarian modul
Ketika sebuah modul bernama spam diimpor, interpreter pertama-tama mencari modul bawaan dengan nama itu. Jika tidak ditemukan, ia kemudian mencari 
berkas bernama spam.py dalam daftar direktori yang diberikan oleh variabel sys.path. sys.path diinisialisasi dari lokasi ini:
1)	Direktori yang berisi skrip masukan (atau direktori saat ini ketika tidak ada file ditentukan).
2)	 PYTHONPATH (daftar nama direktori, dengan sintaksis yang sama dengan variabel shell PATH).
3)	Bawaan yang bergantung pada instalasi.

# c.	Berkas python “Compiled”
Untuk mempercepat memuat modul, Python menyimpan cache versi terkompilasi dari setiap modul di direktori __pycache__ dengan nama module. version.pyc, 
di mana versi menyandikan format berkas terkompilasi; umumnya berisi nomor versi Python. Misalnya, dalam rilis CPython 3.3 versi yang dikompilasi dari 
spam.py akan di-cache sebagai __pycache__/spam.cpython-33.pyc. Konvensi penamaan ini memungkinkan modul yang dikompilasi dari rilis yang beragam dan 
versi Python yang berbeda untuk hidup berdampingan.
Python memeriksa tanggal modifikasi sumber terhadap versi yang dikompilasi untuk melihat apakah itu kedaluwarsa dan perlu dikompilasi ulang. Ini adalah 
proses yang sepenuhnya otomatis. Juga, modul yang dikompilasi adalah platform-independen, sehingga perpustakaan yang sama dapat dibagi di antara sistem 
dengan arsitektur yang berbeda.

# 2.	Modul standar
Python dilengkapi dengan pustaka modul standar, yang dijelaskan dalam dokumen terpisah, Referensi Pustaka Python ("Library Reference" selanjutnya). Beberapa 
modul dibangun ke dalam interpreter; ini menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk 
menyediakan akses ke sistem operasi primitif seperti pemanggilan sistem.

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-04/gambar/6.png"/>

Kedua variabel ini hanya ditentukan jika interpreter dalam mode interaktif.

# 3.	Fungsi dir()
Fungsi bawaan dir() digunakan untuk mencari tahu nama-nama yang ditentukan oleh modul. Ia mengembalikan list string yang diurutkan:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-04/gambar/7.png"/>

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-04/gambar/8.png"/>

dir() tidak mencantumkan nama fungsi dan variabel bawaan. Jika Anda ingin daftar itu, mereka didefinisikan dalam modul standar builtins:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-04/gambar/9.png"/>

# 4.	Paket 
Paket adalah cara penataan namespace modul Python dengan menggunakan "dotted module names". Sebagai contoh, nama modul A.B menetapkan submodule bernama B dalam 
sebuah paket bernama A. Sama seperti penggunaan modul menyelamatkan penulis modul yang berbeda dari harus khawatir tentang nama variabel global masing-masing, 
penggunaan nama modul bertitik menyelamatkan penulis paket multi-modul seperti NumPy atau Pillow dari harus khawatir tentang nama modul masing-masing.
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-04/gambar/10.png"/>

# a.	Mengimpor * dari paket
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-04/gambar/11.png"/>
Ini berarti bahwa from sound.effects import * akan mengimpor tiga submodul bernama dari paket sound.

# b.	Referensi Intra-paket
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-04/gambar/12.png"/>
Dalam contoh ini, modul echo dan surround diimpor dalam namespace saat ini karena mereka didefinisikan dalam paket sound.effects ketika paket from...import 
Pernyataan dieksekusi. (Ini juga berfungsi ketika __all__ didefinisikan.)
Meskipun modul-modul tertentu dirancang hanya untuk mengekspor nama-nama yang mengikuti pola tertentu ketika anda menggunakan import *, itu masih dianggap 
praktik buruk dalam lingkungan kode produksi production.

# c.	Paket di Beberapa Direktori
Paket mendukung satu atribut khusus lagi, __path__. Ini diinisialisasi menjadi daftar yang berisi nama direktori yang menyimpan file paket: __init__.py sebelum 
kode dalam file tersebut dieksekusi. Variabel ini dapat dimodifikasi; hal itu memengaruhi pencarian modul dan subpackage di masa depan yang terkandung dalam paket. 
Meskipun fitur ini tidak sering dibutuhkan, fitur ini dapat digunakan untuk memperluas rangkaian modul yang ditemukan dalam suatu paket.
