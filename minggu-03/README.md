# workshop-python
<h2>Minggu 03</h2>
<b>Nama : Fahri Rahcmad Setyawan</b></br>
<b>NIM : 185410023</b>

# A.	Stuktur Data Python
Pada bab ini menjelaskan beberapa hal yang telah anda pelajari secara lebih mendetail, 
dan menambahkan beberapa hal baru juga. Dibawah ini ada bagian bagian struktur data.

# B.	Bagian bagian dari Stuktur Data Python
# 1.Daftar list
- List.append(x) 
Tambahkan item ke akhir daftar list. Setara dengan a[len(a):] = [x].
- List.ectend(iterable)
Perpanjang daftar list dengan menambahkan semua item dari iterable. Setara dengan a[len(a):] = iterable.
- List.insert(i,x)
Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen sebelum memasukkan, jadi a.insert(0, x) 
memasukkan di bagian depan daftar list, dan a.insert(len(a), x) sama dengan a.append(x).
- List.remove(x)
Hapus item pertama dari daftar list yang nilainya sama dengan x. Ini memunculkan ValueError jika tidak ada item seperti itu.
- List.pop([i])
Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop() 
menghapus dan mengembalikan item terakhir dalam daftar.
- List.clear()
Hapus semua item dari daftar list. Setara dengan del a[:].
- List.index(x[,start[,end]])
Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x. Menimbulkan ValueError jika tidak ada item seperti itu.
- List.count(x)
Kembalikan berapa kali x muncul dalam daftar.
- List.sort()
Urutkan item daftar di tempat (argumen dapat digunakan untuk mengurutkan ubahsuaian customization, lihat sorted() untuk penjelasannya).
- List.reverse()
Balikkan elemen daftar list di tempatnya.
- List.copy()
Kembalikan salinan daftar list yang dangkal. Setara dengan a[:]. Contoh yang menggunakan sebagian besar metode daftar list:

<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-03/gambar/1.png"/>

# -	Menggunakan daftar list sebagai tumpukan Stacks
Pada penggunaan Metode daftar membuatnya sangat mudah untuk menggunakan daftar lust sebagai tumpukan stack, di mana elemen terakhir 
yang ditambahkan adalah elemen pertama yang diambil ("last-in, first-out"). Untuk menambahkan item ke atas tumpukan, gunakan append().
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-03/gambar/2.png"/>

# -	Menggunakan daftar list sebagai antrian Queues
Dimungkinkan juga untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil 
("first-in, first-out"); namun, daftar tidak efisien untuk tujuan ini. Sementara menambahkan dan muncul dari akhir daftar cepat, melakukan 
memasukkan atau muncul dari awal daftar lambat (karena semua elemen lain harus digeser satu).

Untuk mengimplementasikan antrian, gunakan collections.deque yang dirancang untuk menambahkan dan muncul dengan cepat dari kedua ujungnya. Sebagai contoh:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-03/gambar/3.png"/>

# -	Daftar list Comprehensions
Pemahaman daftar list comprehensions menyediakan cara singkat untuk membuat daftar. Aplikasi umum adalah membuat daftar baru di mana setiap elemen 
adalah hasil dari beberapa operasi yang diterapkan pada setiap anggota dari urutan lain atau iterable, atau untuk membuat urutan elemen-elemen yang 
memenuhi kondisi tertentu.
Contohnya:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-03/gambar/4.png"/>

# -	Pemahaman daftar list Comprehensions Bersarang
Pada ekspresi awal dalam pemahaman daftar list comprehension dapat berupa ekspresi acak arbitrary, termasuk pemahaman daftar list comprehension lainnya.

Pada contoh dibawah ini matriks 3x4 diimplementasikan sebagai daftar list 3 dari daftar list panjang 4
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-03/gambar/5.png"/>
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-03/gambar/6.png"/>
Pada program di atas sebagai contoh anda harus memilih fungsi bawaan untuk pernyataan aliran flow yang kompleks. Fungsi zip() akan melakukan pekerjaan 
yang baik untuk kasus penggunaan ini:

# 2.	Pernyataan del
Ada cara untuk menghapus item dari daftar yang diberikan indeksnya, bukan nilainya: pernyataan del. Ini berbeda dari metode pop() yang mengembalikan 
nilai. Pernyataan del juga dapat digunakan untuk menghapus irisan dari daftar list atau menghapus seluruh daftar list (yang kami lakukan sebelumnya 
dengan menetapkan daftar kosong pada slice). Sebagai contoh:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-03/gambar/7.png"/>
Biasanya del juga dapat digunakan untuk menghapus seluruh variable, contohnya:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-03/gambar/8.png"/>

# 3.	Tupels dan urutan Sequences
Kita melihat bahwa daftar list dan string memiliki banyak properti yang sama, seperti operasi pengindeksan dan pemotongan. Mereka adalah dua contoh 
tipe data sequence (lihat Sequence Types --- list, tuple, range). Karena Python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan. 
Ada juga tipe data urutan standar lain: tuple.

Dimana sebuah tuple terdiri dari sejumlah nilai yang dipisahkan oleh koma, contoh:
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-03/gambar/9.png"/>

# 4.	Himpunan set
Python juga menyertakan tipe data untuk sets. Himpunan atau Set adalah koleksi yang tidak terurut tanpa elemen duplikat. Penggunaan dasar termasuk 
pengujian keanggotaan dan menghilangkan entri duplikat.
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-03/gambar/10.png"/>

# 5.	Kamus Dictionaries
Tipe data lain yang berguna yang dibangun ke dalam Python adalah dictionary (lihat Mapping Types --- dict). Kamus dictionary kadang-kadang ditemukan 
dalam bahasa lain sebagai "assosiative memories" atau "assosiative array". Tidak seperti urutan sequences, yang diindeks oleh sejumlah angka, kamus 
dictionary diindeks oleh keys, yang dapat berupa jenis apa pun yang tidak dapat diubah immutable type; string dan angka selalu bisa menjadi kunci key. 
Tuples dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tuple; jika sebuah tuple berisi objek yang bisa berubah baik secara langsung 
atau tidak langsung, itu tidak dapat digunakan sebagai kunci key. Anda tidak dapat menggunakan daftar list sebagai kunci, karena daftar dapat dimodifikasi 
di tempat menggunakan penugasan indeks, penugasan slice, atau metode seperti append() dan extend().
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-03/gambar/11.png"/>

# 6.	Teknik perulangan
Saat mengulang kamus dictionaries, kunci key dan nilai value terkait dapat diambil pada saat yang sama menggunakan metode items().
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-03/gambar/12.png"/>

# 7.	Lebih lanjut tentang kondisi
Kondisi yang digunakan dalam pernyataan while dan if dapat berisi operator apa pun, bukan hanya perbandingan. Operator perbandingan in dan not in memeriksa 
apakah suatu nilai terjadi (tidak terjadi) secara berurutan. Operator is dan is not membandingkan apakah dua objek benar-benar objek yang sama; ini hanya 
penting untuk objek yang dapat diubah seperti daftar list. Semua operator pembanding memiliki prioritas yang sama, yang lebih rendah daripada semua operator numerik.
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-03/gambar/13.png"/>

# 8.	Membandingkan urutan Sequences dan jenis lainya
Objek urutan sequence biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingan menggunakan pengurutan lexicographical: 
pertama dua item pertama dibandingkan, dan jika mereka berbeda ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan 
seterusnya, sampai urutan mana pun habis.
<img src="https://github.com/Fahri54/workshop-python/blob/main/minggu-03/gambar/14.png"/>
