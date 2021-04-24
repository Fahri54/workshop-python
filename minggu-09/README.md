# workshop-python
<h2>Minggu 09</h2>
<b>Nama : Fahri Rahcmad Setyawan</b></br>
<b>NIM : 185410023</b>

# Virtual Environment dan Package Manager
# 1.	Pengantar Lingkungan dan Paket Virtual
Aplikasi Python akan sering menggunakan paket dan modul yang tidak datang sebagai bagian dari pustaka standar. Aplikasi kadang-kadang membutuhkan versi pustaka tertentu, karena aplikasi mungkin mensyaratkan bug tertentu telah diperbaiki atau aplikasi dapat ditulis menggunakan versi usang dari antarmuka pustaka.

Ini berarti tidak mungkin bagi satu instalasi Python untuk memenuhi persyaratan setiap aplikasi. Jika aplikasi A membutuhkan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka persyaratannya bertentangan dan menginstal versi 1.0 atau 2.0 akan membuat satu aplikasi tidak dapat berjalan.

Solusi untuk masalah ini adalah membuat virtual environment, sebuah struktur direktori mandiri yang berisi instalasi Python untuk versi tertentu dari Python, serta sejumlah paket tambahan.

# 2.	Menciptakan Lingkungan Virtual
Modul yang digunakan untuk membuat dan mengelola lingkungan virtual disebut venv. venv biasanya akan menginstal versi Python terbaru yang Anda miliki. Jika Anda memiliki beberapa versi Python di sistem Anda, Anda dapat memilih versi Python tertentu dengan menjalankan python3 atau versi mana pun yang Anda inginkan.


Untuk membuat lingkungan virtual, tentukan direktori tempat Anda ingin meletakkannya, dan jalankan modul venv sebagai skrip dengan jalur direktori:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-09/gambar/1.png"/>

Ini akan membuat direktori tutorial-env jika tidak ada, dan juga membuat direktori di dalamnya yang berisi salinan interpreter Python, pustaka standar, dan berbagai berkas pendukung.

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-09/gambar/2.png"/>

Setelah Anda membuat lingkungan virtual, Anda dapat mengaktifkannya. Di Windows, operasikan:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-09/gambar/3.png"/>

Mengaktifkan lingkungan virtual akan mengubah prompt shell Anda untuk menunjukkan lingkungan virtual apa yang Anda gunakan, dan memodifikasi lingkungan sehingga menjalankan python akan membuat Anda mendapatkan versi dan instalasi Python tertentu. Sebagai contoh:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-09/gambar/4.png"/>

# 3.	Mengelola Paket dengan pip
Anda dapat menginstal, mengupgrade, dan menghapus paket menggunakan program yang disebut pip. Secara default pip akan menginstal paket dari Python Package Index, https://pypi.org. Anda dapat menelusuri Indeks Paket Python dengan membukanya di browser web Anda. Sebagai contoh anda dapat menginstal versi terbaru dari suatu paket dengan menyebutkan nama suatu paket:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-09/gambar/5.png"/>

Selanjutnya kita akan menampilkan paket yang sudah di install

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-09/gambar/6.png"/>
