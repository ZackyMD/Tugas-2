### Nama : Zacky Muchlas Dharmawan
### NPM  : 2106702296
### Link : 
### https://tugas2-pbp-zacky.herokuapp.com/mywatchlist/html/
### https://tugas2-pbp-zacky.herokuapp.com/mywatchlist/json/
### https://tugas2-pbp-zacky.herokuapp.com/mywatchlist/xml/

Saya di sini ingin menjelaskan beberapa pertanyaan yang diberikan di dalam web PBP Fasilkom UI, di antaranya adalah

----------------------------------------------------------------------------
## Jelaskan perbedaan JSON, XML, dan HTML!
----------------------------------------------------------------------------
JSON merupakan singkatan dari Javascript Object Notation, berfungsi untuk menyimpan, membaca, dan menukar informasi yang berasal dari web server dengan tujuan untuk memudahkan para pengguna untuk membaca kodenya, serta data yang tersimpan dalam format (key/value).

XML merupakan singkatan dari Extensible Markup Language, berfungsi untuk menyederhanakan proses pengiriman/pertukaran data antar server di dalam folder aplikasi web server tersebut, data XML tersimpan sebagai tree structure.

HTML singkatan dari HyperText Markup Language, berfungsi untuk menyusun bagian paragraf, heading, atau link yang nantinya akan ditampilkan pada aplikasi web yang sudah diinisiasi sebelumnya di dalam folder aplikasi web server tersebut.

----------------------------------------------------------------------------
## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
----------------------------------------------------------------------------
Data delivery digunakan di dalam pengimplementasian sebuah platform dengan tujuan agar program yang telah dibuat di dalam file dengan jenis yang berbeda-beda dapat digabung menjadi satu di dalam suatu file untuk ditampilkan pada aplikasi web. Jika tidak terdapat data delivery maka penyusunan file dengan tipe yang berbeda-beda serta data yang akan ditampilkan pada aplikasi web tidak akan terjadi.

----------------------------------------------------------------------------
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
----------------------------------------------------------------------------
Untuk checklist pertama, saya menambahkan aplikasi baru bernama mywatchlist dengan menggunakan perintah manage.py startapp nywatchlist dengan syarat sebelumnya menjalankan virtual environment terlebih dahulu. Setelah itu, menambahkan aplikasi mywatchlist di dalam settings.py di folder project_django.

Untuk checklist ke-2, saya menambahkan path untuk user dapat mengakses http://localhost:8000/mywatchlist/ di dalam urls.py di dalam folder project_django pada bagian urlpatterns dengan menambahkan path('mywatchlist/', include('mywatchlist.urls')),

Untuk checklist ke-3 sammpai ke-8, saya menambahkan atribut-atribut tersebut di dalam file models.py pada folder mywatchlist dengan menambahkan kelas BarangMyWatchlist dengan parameter models.Model serta atribut-atribut tersebut terdiri dari kode     watchedFilm = models.CharField(max_length=50)
titleWatched = models.TextField()
ratingWatched = models.TextField()
releaseDateWatched = models.TextField()
reviewWatched = models.TextField()

Untuk checklist ke-9, saya menambahkan 10 data objek dengan membuat folder baru bernama fixtures dengan file bernama initial_watchlist_data.json dengan isi 10 data objek sesuai dengan hal yang terinisiasi di dalam models.py seperti watchedFilm, titleWatched, ratingWatched, releaseWatched, dan reviewWatched.

Untuk checklist ke-10 sampai ke-13, saya menambahkan fungsi show_xml, show_json, dan show_mywatchlist (untuk HTMLnya) dengan menambahkan 
data = BarangMyWatchlist.objects.all()
return HttpResponse(serializers.serialize("xml atau json", data), content_type="application/xml atau json")
2 data tersebut untuk format xml dan json, sedangkan untuk html dengan menambahkan
data_barang_watchlist = BarangMyWatchlist.objects.all()
context = {
    'film': data_barang_watchlist,
    'nama': 'Zacky Muchlas Dharmawan',
    'npm' : '2106702296'
}
return render(request, "mywatchlist.html", context)

Untuk checklist ke-14 sampai ke-17, saya menambahkan urlpattern di dalam folder mywatchlist dengan file bernama urls.py untuk masing-masing format, seperti 
path('html/', show_mywatchlist name='show_mywatchlist'),
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
dengan tujuan agar ketiga format di atas dapat diakses melalui url mywatchlist/sesuai path di atas.

Untuk checklist ke-18 deployment ke Heroku. Step yang dilakukan adalah dengan membuat variabel HEROKU_API_KEY dan HEROKU_APP_NAME di dalam github secrets lalu ke bagian actions dan mengambil API KEY serta nama apps pada heroku. Terakhir, deploy di dalam github yang berada pada bagian actions di repository.

Untuk checklist ke-23, berikut adalah bukti screenshot di dalam web Postman:
![Gambar]('../../HTML_Postman.jpg?raw=true')
![Gambar]('../../JSON_Postman.jpg?raw=true')
![Gambar]('../../XML_Postman.jpg?raw=true')

Untuk checklist ke-24, saya menggunakan algoritma
class TestPy(TestCase):
    def testHtml(self):
        response = Client().get('http://localhost:8000/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    
    def testJson(self):
        response = Client().get('http://localhost:8000/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)

    def testXml(self):
        response = Client().get('http://localhost:8000/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

dengan tujuan/maksud test tersebut akan tercapai/sukses ketika response.status_code mencapai poin 200 yang mana hal yg di tes adalah link local host untuk ketiga format yang telah dibuat sebelumnya.

Sekian jawaban yang dapat saya berikan. Terima kasih atas perhatian dan kesempatannya.