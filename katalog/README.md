# Tugas 2 Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 

### Nama        : Zacky Muchlas Dharmawan
### NPM         : 2106702296
### Link Heroku : http://tugas2-pbp-zacky.herokuapp.com/katalog/

-----------------------------------------------
Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

-----------------------------------------------
![Gambar]('../../Pola_Django.png?raw=true')

-----------------------------------------------
Jelaskan kenapa menggunakan virtual environment! Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

-----------------------------------------------
Penjelasan:

Penggunaan virtual environment pada tugas pbp ini bertujuan agar pengoperasian spesifik ke proyek tugas 2. Selain itu, fungsi dari virtual environment adalah agar program dari luar tidak bisa mengakses proyek di dalam virtual environment. Aplikasi web berbasis Django tanpa menggunakan virtual envinronment tetap dapat digunakan tetapi penggunaan virtual environment untuk memastikan versi yang digunakan tidak bergantung pada environment yang ada pada internal komputer sehingga dapat digunakan di berbagai komputer (kompatibel di berbagai komputer).

-----------------------------------------------
Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas!

-----------------------------------------------
Penjelasan:

### views.py
pada file views.py saya menginisiasi nama dan npm di dalam sebuah dictionary bernama context yang berada di fungsi show_katalog dengan tujuan agar bisa ditampilkan di dalam file katalog.html.

### urls.py
Pada file urls.py yang terdapat di folder project_django, urls.py bertujuan untuk menghubungkan file tersebut dengan urls.py pada folder katalog. Urls.py pada folder katalog memiliki fungsi agar function show_katalog yang berada pada views.py dapat ditampilkan pada url ....katalog/ 

### katalog.html
Pada file katalog.html, saya mengambil data dengan memanggil key atau variabel yang berada pada views.py di folder katalog. Selain itu, saya melakukan loop terhadap list_barang yang diambil dari key list_barang di views.py dan mengambil data dari katalog.models.

### deploy
Penggunaan deploy diimplementasikan dengan cara menghubungkan repository github dengan heroku. Step yang dilakukan adalah dengan membuat variabel HEROKU_API_KEY dan HEROKU_APP_NAME di dalam github secrets lalu ke bagian actions dan mengambil API KEY serta nama apps pada heroku. Terakhir, deploy di dalam github yang berada pada bagian actions di repository.