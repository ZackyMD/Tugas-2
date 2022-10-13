### Nama : Zacky Muchlas Dharmawan
### NPM  : 2106702296
### Link : https://tugas2-pbp-zacky.herokuapp.com/todolist/show_json/

Saya di sini ingin menjelaskan beberapa pertanyaan yang diberikan di dalam web PBP Fasilkom UI, di antaranya adalah

--------------------------------------------------
### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming!

--------------------------------------------------
synchronus programming adalah proses jalnnya program berdasarkan antrian eksekusi program, sedangkan asynchronus programming adalah proses jalannya program dapat dilakukan secara bersamaan.

--------------------------------------------------
### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini!

--------------------------------------------------
paradigma Event-Driven Programming adalah paradigma program yang cara kerjanya berjalan secara real time atau saat event tersebut terjadi sehingga program berjalan secara asynchronus (tidak perlu menunggu antrian). Contoh di dalam program ini adalah ketika menambahkan task baru, program langsung berjalan ketika button tersebut ditekan atau di dalam kodingannya menggunakan kode `document.getElementById("addNewTask").onclick = addTodolistModal` untuk mentrigger event.

--------------------------------------------------
### Jelaskan penerapan asynchronous programming pada AJAX!
--------------------------------------------------
penerapan asynchronus programming pada AJAX adalah ketika suatu event ketrigger dan program akan berjalan secara real-time. Program akan memanggil AJAX POST untuk mengirim data ke server kemudian program akan menangkap data yang telah diolah pada server tanpa harus melakukan refresh pada halaman web.

--------------------------------------------------
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
--------------------------------------------------
Pertama-tama saya membuat script link yang menghubungkan bootstrap dengan program yang saya akan buat di dalam file html. Pada file views.py saya membuat fungsi seperti di bawah ini
# tampilan baru untuk /json 
@login_required(login_url='/todolist/login/')
def show_json(request:HttpResponse):
    dataToDoList = Task.objects.filter(user=request.user)
    context = {
        'nama' : request.user.username,
        'todolist' : dataToDoList,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist_ajax.html", context)

# get data AJAX
def get_json(request):
    dataToDoList = Task.objects.filter(user=request.user)

    return HttpResponse(serializers.serialize("json", dataToDoList), content_type="application/json")

# add Task di modal
def create_todolist(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        date=datetime.datetime.now()
        user=request.user

        Task.objects.create(
            title=title,
            description=description,
            date=date,
            user=user,

        )

    return HttpResponse(b"CREATED", status=201)

dengan tujuan agar pembuatan json dapat menampilkan data-data yang diperlukan pada file html. Pada program ini, saya memanggil title dan description sebagai nama pada input sehingga akan membuat jembatan antara views.py dan file html sehingga memungkinkan untuk penyimpanan data. Selain itu, di dalam file html, saya juga menambahkan href untuk menuju url create_todolist pada button submit di dalam modal dengan tujuan yang sama dengan pemanggilan title dan description sebelumnya. Untuk di dalam file urls.py, saya menambahkan 3 path terbaru, yaitu 
### 1. path('json/', get_json, name='get_json'),
### 2. path('create_todolist/', create_todolist name='create_todolist'),
### 3. path('show_json/', show_json, name='show_json'),

pembuatan path tersebut nantinya digunakan untuk mengakses fungsi yang diinginkan.

Untuk htmlnya sendiri, setelah saya menambahkan modal dari template bootstrap dan melakukan modifikasi agar sesuai dengan output yang diinginkan, saya melakukan kodingan dengan script, di dalam script, saya melakukan pengambilan data json yang nantinya akan digunakan untuk mengirimnya kepada fungsi addTodolistModal(). Sebelum data ditampilkan, pastinya terdapat tombol yang mentrigger program document.getElementById("addNewTask").onclick = addTodolistModal sehingga data yang diambil dari proses GET (input) dapat ditampilkan pada halaman web. 