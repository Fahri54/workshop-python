# workshop-python
<h2>Minggu 07</h2>
<b>Nama : Fahri Rahcmad Setyawan</b></br>
<b>NIM : 185410023</b>

# OOP PYHTON
# 1. Classes
Classes atau kelas-kelas adalah menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama. Membuat sebuah class baru menghasilkan objek dengan type baru,
memungkinkan dibuat instance baru dari tipe itu. Setiap instance dari class dapat memiliki atribut yang melekat padanya untuk mempertahankan kondisinya. Instance dari 
sebuah class juga dapat memiliki metode (ditentukan oleh class) untuk memodifikasi kondisinya.

# a. Sepatah Kata Tentang Nama dan Objek
Objek memiliki individualitas, dan banyak nama (dalam berbagai lingkup) dapat terikat ke objek yang sama. Ini dikenal sebagai aliasing dalam bahasa lain. Ini biasanya 
tidak dihargai pada pandangan pertama pada Python, dan dapat diabaikan dengan aman ketika berhadapan dengan tipe dasar yang tidak dapat diubah (angka, string, tuple). 
Namun, aliasing memiliki efek yang mungkin mengejutkan pada semantik kode Python yang melibatkan objek yang bisa berubah seperti daftar list, kamus dictionary, dan 
sebagian besar jenis lainnya. Ini biasanya digunakan untuk kepentingan program, karena alias berperilaku seperti pointers dalam beberapa hal. Sebagai contoh, 
melewatkan objek adalah murah karena hanya sebuah pointer dilewatkan oleh implementasi; dan jika suatu fungsi memodifikasi objek yang dilewatkan sebagai argumen, 
pemanggil akan melihat perubahan --- ini menghilangkan kebutuhan untuk dua mekanisme yang berbeda melewatkan argumen argument passing seperti dalam Pascal.

# b. Lingkup Python dan Namespaces
Sebelum memperkenalkan kelas, pertama-tama saya harus memberi tahu Anda tentang aturan ruang lingkup scope Python. Definisi kelas memainkan beberapa trik rapi dengan 
ruang nama namespaces, dan Anda perlu tahu bagaimana ruang lingkup dan ruang nama namespaces bekerja untuk sepenuhnya memahami apa yang terjadi. Kebetulan, pengetahuan
tentang subjek ini berguna untuk programmer Python tingkat lanjut.

# 1. Contoh Lingkup Scopes dan Ruang Nama Namespaces
Ini adalah contoh yang menunjukkan cara mereferensikan lingkup scopes dan ruang nama namespaces yang berbeda, dan bagaimana global dan nonlocal memengaruhi pengikatan 
variabel:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/1.png"/>

Perhatikan bagaimana pemberian nilai local (yang bawaan) tidak mengubah scope_tests pengikatan spam. Pemberian nilai nonlocal mengubah scope_test's pengikatan spam, 
dan pemberian nilai global mengubah pengikatan level modul.
Anda juga dapat melihat bahwa tidak ada pengikatan sebelumnya untuk spam sebelum pemberian nilai global.

# c. Pandangan Pertama tentang Kelas
Kelas memperkenalkan sedikit sintaks baru, tiga tipe objek baru, dan beberapa semantik baru.

# 1. Sintaks Definisi Kelas
Bentuk definisi kelas paling sederhana terlihat seperti ini:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/2.png"/>

Definisi kelas, seperti definisi fungsi (pernyataan def) harus dieksekusi sebelum mereka memiliki efek. (Anda dapat menempatkan definisi kelas di cabang dari 
pernyataan if, atau di dalam suatu fungsi.)

# 2. Objek Kelas Class Objects
Attribute references menggunakan sintaks standar yang digunakan untuk semua referensi atribut dalam Python: obj.name. Nama atribut yang valid adalah semua nama yang 
ada di namespace kelas saat objek kelas dibuat. Jadi, jika definisi kelas tampak seperti ini:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/3.png"/>

kemudian MyClass.i dan MyClass.f adalah referensi atribut yang valid, masing-masing mengembalikan integer dan objek fungsi. Atribut kelas juga dapat ditetapkan, 
sehingga Anda dapat mengubah nilai MyClass.i oleh penugasan. __doc__ juga merupakan atribut yang valid, mengembalikan docstring milik kelas: "A simple example class".

# 3. Objek Instance
data attributes sesuai dengan "variabel instan" di Smalltalk, dan "data members" di C++. Atribut data tidak perlu dinyatakan; seperti variabel lokal, mereka muncul 
ketika mereka pertama kali ditugaskan. Misalnya, jika x adalah turunan dari MyClass yang dibuat di atas, bagian kode berikut akan mencetak nilai 16, tanpa meninggalkan
jejak:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/4.png"/>

# 4. Metode Objek
Biasanya, metode dipanggil tepat setelah itu terikat:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/5.png"/>

Dalam contoh MyClass, ini akan mengembalikan string 'hello world'. Namun, tidak perlu memanggil metode segera: x.f adalah metode objek, dan dapat disimpan dan 
dipanggil di lain waktu. Sebagai contoh:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/6.png"/>

# 5. Variabel Kelas dan Instance
Secara umum, variabel instance adalah untuk data unik untuk setiap instance dan variabel kelas adalah untuk atribut dan metode yang dibagikan oleh semua instance 
kelas:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/7.png"/>

# d. Keterangan acak
Jika nama atribut yang sama muncul di kedua instance dan di kelas, maka pencarian atribut memprioritaskan instance:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/8.png"/>

Atribut data dapat dirujuk oleh metode dan juga oleh pengguna biasa ("clients") dari suatu objek. Dengan kata lain, kelas tidak dapat digunakan untuk 
mengimplementasikan tipe data abstrak murni.

# e. Pewarisan
Tentu saja, fitur bahasa tidak akan layak untuk nama "class" tanpa mendukung pewarisan. Sintaks untuk definisi kelas turunan terlihat seperti ini:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/9.png"/>

# 1. Pewarisan Berganda
Python mendukung bentuk pewarisan berganda juga. Definisi kelas dengan beberapa kelas dasar terlihat seperti ini:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/9.png"/>

# 1. Variabel Privat
Name mangling sangat membantu untuk membiarkan subclass menimpa metode tanpa memutus panggilan metode intraclass. Sebagai contoh:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/10.png"/>

# g. Barang Sisa Odds and Ends
Kadang-kadang berguna untuk memiliki tipe data yang mirip dengan "record" Pascal atau "struct" C, menyatukan beberapa item data bernama. Definisi kelas kosong 
akan menghasilkan hal tersebut dengan baik:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/11.png"/>

# h. Iterators
Sekarang Anda mungkin telah memperhatikan bahwa sebagian besar objek penampung container dapat dibuat perulangan menggunakan pernyataan for:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/12.png"/>

# i. Pembangkit Generator
Generator adalah alat sederhana dan kuat untuk membuat iterator. Mereka ditulis seperti fungsi biasa tetapi menggunakan pernyataan hasil kapan pun mereka ingin 
mengembalikan data. Setiap kali next () dipanggil, generator melanjutkan di mana ia tinggalkan (ia mengingat semua nilai data dan pernyataan mana yang terakhir 
dieksekusi). Sebuah contoh menunjukkan bahwa generator dapat dibuat dengan sangat mudah:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/13.png"/>

# j. Ekspresi Pembangkit Generator
Beberapa pembangkit generators sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaksis yang mirip dengan pemahaman daftar list comprehensions 
tetapi dengan tanda kurung bukan dengan tanda kurung siku. Ungkapan-ungkapan ini dirancang untuk situasi di mana generator digunakan segera oleh fungsi penutup. 
Ekspresi generator lebih kompak tetapi kurang fleksibel daripada definisi generator penuh dan cenderung lebih ramah memori daripada pemahaman daftar list 
comprehensions setara. Contoh:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-07/gambar/14.png"/>
