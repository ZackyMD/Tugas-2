### Nama : Zacky Muchlas Dharmawan
### NPM  : 2106702296
### Link : https://tugas2-pbp-zacky.herokuapp.com/todolist/
### Alternative link if keyerror happened : https://tugas2-pbp-zacky.herokuapp.com/todolist/login/
### Akun Berisi Dummy Data :
### Username 1 : Apaaja
### Pass 1     : Y9uGLcsdkpJSieW
### Username 2 : Terserah
### Pass 2     : eZ8gUZLg3KzH8nb

Saya di sini ingin menjelaskan beberapa pertanyaan yang diberikan di dalam web PBP Fasilkom UI, di antaranya adalah

-----------------------------------------------------
 ### Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?
-----------------------------------------------------
Kegunaan dari csrf-token adalah untuk mencegah serangan CSRF. Pencegahan tersebut membuat penyerang tidak dapat melakukan permintaan HTTP yang valid dan cocok untuk diumpankan kepada calon korban. 

Jika tidak terdapat potongan kode tersebut program tidak bisa digunakan untuk menambahkan sesuatu pada server sesuai dengan fungsi dari form (program akan error) karena aplikasi di sisi server akan menolak permintaan form jika CSRF tidak ada.

-----------------------------------------------------
### Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual
-----------------------------------------------------
Iya, kita dapat membuat elemen form secara manual tanpa menggunakan generator tersebut. Gambaran besar cara membuat form secara manual adalah dengan menambahkan td (standart data cells) di dalam kode table dengan tujuan untuk menambahkan To Do dan Description di dalam baris yang sama, lalu untuk inputnya bertipe "text" dengan class form-control.

-----------------------------------------------------
### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
-----------------------------------------------------
Ketika pengguna memberikan input pada form, maka yang terjadi adalah pada todolist.html, ketika menambahkan task baru langsung mereferensi kepada urlnya get_task yang mana di dalam method get_task pada views.py mengambil informasi pada show_todolist dan disimpan di dalam sebuah variabel dan mendirect kembali dengan fungsi show_todolist. Setelah itu, di dalam todolist.html, akan dilakukan loop dan mengambil data title, date, dan description yang nantinya akan ditampilkan di dalam web. 

-----------------------------------------------------
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
-----------------------------------------------------
Saya menambahkan aplikasi baru bernama todolist dengan menggunakan perintah manage.py startapp todolist dengan syarat sebelumnya menjalankan virtual environment terlebih dahulu. Setelah itu, menambahkan aplikasi todolist di dalam settings.py di folder project_django.

Setelah itu, saya menambahkan path untuk user dapat mengakses http://localhost:8000/todolist/ di dalam urls.py di dalam folder project_django pada bagian urlpatterns dengan menambahkan path('todolist/', include('todolist.urls')),

Lalu, saya menambahkan atribut-atribut tersebut di dalam file models.py pada folder todolist dengan menambahkan kelas Task dengan parameter models.Model serta atribut-atribut tersebut terdiri dari kode
user = models.ForeignKey(
    User,
    on_delete=models.CASCADE)
date = models.DateField(auto_now=True)
title = models.TextField()
description = models.TextField()
finish = models.BooleanField(default=False)

Untuk membuat form registrasi, login, dan logout, saya menggunakan cara seperti pada tutorial lab3, dimulai dari registrasi, saya melakukan import hal-hal yang diperlukan lalu saya membuat fungsi register pada views.py sesuai dengan yang sudah diberikan pada lab3 (hanya digant nama folder aplikasinya), kemudian saya membuat register.html di dalam folder templates pada folder todolist yang kodenya persis sama dengan tutorial lab 3, serta yang terakhir untuk pembuatan form registrasi dengan membuat path di dalam urls.py untuk registrasi. 

Untuk pembuatan form login, kurang lebih sama dengan pembuatan form registrasi untuk tahapannya, tentunya dengan isi file html, path, dan fungsi yang berbeda dengan registrasi.

Untuk pembuatan form logout, kurang lebih sama dengan pembuatan form registrasi dan login untuk tahapannya, tentunya dengan isi file html, path, dan fungsi yang berbeda dengan registrasi dan login serta menambahkan tombol logout di dalam file todolist.html.

Kemudian saya merestriksi akses halaman todolist yang mana ketika mengakses link todolist maka akan dioper ke dalam link login. Selain itu, saya juga menambahkan cookies dengan mengganti beberapa kode pada views.py yang sudah ada sebelumnya dengan kode yang diberikan di dalam tutorial lab3 serta menambahkan waktu terakhir login di dalam file todolist.html.

Untuk pembuatan halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task dilakukan di dalam file todolist.html dengan membuat Nama : {{nama}} untuk menampilkan user lalu membuat tabel berisi judul, tanggal, dan deskripsi yang informasinya didapat dengan melakukan loop pada app todolist yang mengambil datanya dari models.py dan mengopernya ke dalam fungsi show_todolist di dalam file views.py. Di luar tabel, dibuat tombol Tambah Task dan logout.

Untuk membuat halaman form pada pembuatan task yang berisi judul task dan deskripsi task, dibuat di dalam create-task.html dengan form yang dibuat secara manual dengan menambahkan td (standart data cells) di dalam kode table dengan tujuan untuk menambahkan To Do dan Description di dalam baris yang sama, lalu untuk inputnya bertipe "text" dengan class form-control.

--------------------------------------------------
### Apa perbedaaan dari inline, internal, dan external CSS? apa saja kelebihan dan kekurangan dari masing-masing style?
--------------------------------------------------
inline = diletakkan di dalam file HTML dengan atribut < style > .
Kelebihan = permintaan HTTP yang lebih kecil, baik diterapkan jika ingin menguji dan melihat perubahan.
Kekurangan = inline css harus diterapkan pada setiap elemen.

internal = diletakkan di dalam < head > pada file html dengan class dan id merujuk pada kode CSS.
Kelebihan = Perubahan terjadi di 1 halaman saja, css dan html digunakan di dalam 1 file, class dan id bisa digunakan oleh internal stylesheet.
Kekurangan = Meningkatkan waktu akses website.

external = membuat file css tersendiri di luar html dengan memberikan link rujukan di dalam file html.
Kelebihan = ukuran file html menjadi lebih kecil dan lebih rapi, penerapan desain pada file css dapat digunakan di banyak halaman.
Kekurangan = Halaman belum tampil secara sempurna hingga file CSS selesai dipanggil.

--------------------------------------------------
### Jelaskan tag HTML5 yang kamu ketahui!
--------------------------------------------------
< html > = untuk membuat sebuah dokumen HTML
< title > = untuk membut judul dari sebuah halaman
< body > = untuk membuat isi dari sebuah halaman
< h1 > sampai < h6 > = untuk membuat heading
< p > = untuk membuat paragraf
< br > = untuk menandakan akhir dari sebuah baris
< link > = untuk menghubungkan antara dokumen dan sumber daya eksternal
< img > = untuk membuat gambar
< table > = untuk membuat tabel

--------------------------------------------------
### Jelaskan tipe-tipe CSS selector yang kamu ketahui!
--------------------------------------------------
Tag Selector = menggunakan tag HTML untuk mengaksesnya (contoh = h5 {}).
ID Selector = menggunakan nama id untuk mengaksesnya (menggunakan '#(nama id)').
Class Selector = menggunakan nama class untuk mengaksesnya (menggunakan '.(nama class)').
Universal Selector = untuk menggunakan seluruh tag yang ada di dalam file (menggunakan tanda '*').

--------------------------------------------------
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
--------------------------------------------------
Saya menggunakan css dengan styel inline karena saya ingin membut desain masing-masing pada setiap halaman. Untuk menggunakan cards pada todolist saya mengambil codenya dari bootstrap (template) yang kemudian saya edit untuk memasukkan hal-hal yang diperlukan. Selain itu, saya juga mengkustomisasi tampilan pada template bootstrap tersebut. Untuk menjadikannya responsive saya hanya menghubungkannya pada link bootstrap dan secara otomatis halaman menjadi responsive.