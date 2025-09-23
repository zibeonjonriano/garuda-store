Nama  : Zibeon Jonriano Wisnumoerti
Kelas : PBP D
NPM   : 2406355634

### Tautan Web        : https://zibeon-jonriano-garudastore.pbp.cs.ui.ac.id/
### Tautan Repositori : https://github.com/zibeonjonriano/garuda-store

---

# Tugas 2: Implementasi Model-View-Template (MVT) pada Django

## "1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)."

### "A. Membuat sebuah proyek Django baru."

        1. Saya membuka akun GitHub dan membuat repositori proyek untuk Tugas Individu 2 yang bertemakan footballshop ini dengan nama "garuda-store". Saya buat repositori tersebut bersifat public.

        2. Lalu saya memilih lokasi penyimpanan di penyimpanan lokal komputer saya untuk melakukan clonning repo dengan menggunakan "cd {lokasi}" dan "git clone https://github.com/zibeonjonriano/garuda-store.git".

        3. Membuat virtual environment dengan "python -m venv env" dan mengaktifkannya dengan "env\Scripts\activate".

        4. Lalu dalam direktori yang sama, saya membuat file "requirements.txt" yang berisikan : 
            django
            gunicorn
            whitenoise
            psycopg2-binary
            requests
            urllib3
            python-dotenv

        5. Lalu saya menginstall semua hal yang diperlukan dengan melakukan command "pip install -r requirements.txt"

        6. Setelah berhasil terinstall, saya membuat proyek django baru bernama "garuda_store" dengan command "django-admin startproject garuda_store ."

        7. Setelah berhasil membuat projek django baru, saya melakukan konfigurasi environtments variables dan proyek, dengan membuat file ".env" di dalam direktori root proyek (di mana file manage.py berada). Lalu menambahkan konfigurasi ini "PRODUCTION=False".

        8. Saya juga membuat file .env.prod di direktori yang sama untuk konfigurasi production : 
            DB_NAME=<nama database>
            DB_HOST=<host database>
            DB_PORT=<port database>
            DB_USER=<username database>
            DB_PASSWORD=<password database>
            SCHEMA=tugas_individu <- sesuai ketentuan>
            PRODUCTION=True
        Dimana setiap datanya mengikuti kredensial database yang sudah diberikan di email UI.

        9. Saya memodifikasi file "settings.py" dengan menambahkan kode berikut di bagian atas file (setelah import path) : 
            import os
            from dotenv import load_dotenv
            # Load environment variables from .env file
            load_dotenv()
        Hal ini dilakukan untuk menggunakan environment variables.

        10. Setelah itu saya menambahkan "ALLOWED_HOSTS = ["localhost", "127.0.0.1"]" di "settings.py" untuk keperluan development, sebab bagian tadi berfungsi sebagai daftar host yang diizinkan untuk mengakses aplikasi web. (dengan menambahkan bagian tsb, artinya saya bisa mengakses web secara lokal saja).

        11. Menambahkan konfigurasi "PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'" tepat diatas kode DEBUG dalam "settings.py".

        12. Mengubah konfigurasi database di "settings.py". Ganti kode bagian DATABASES dengan kode :
            # Database configuration
            if PRODUCTION:
                # Production: gunakan PostgreSQL dengan kredensial dari environment variables
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.postgresql',
                        'NAME': os.getenv('DB_NAME'),
                        'USER': os.getenv('DB_USER'),
                        'PASSWORD': os.getenv('DB_PASSWORD'),
                        'HOST': os.getenv('DB_HOST'),
                        'PORT': os.getenv('DB_PORT'),
                        'OPTIONS': {
                            'options': f"-c search_path={os.getenv('SCHEMA', 'public')}"
                        }
                    }
                }
            else:
                # Development: gunakan SQLite
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': BASE_DIR / 'db.sqlite3',
                    }
                }

        13. Buka CMD dan pastikan lokasi terkini adalah direktori yang setara dengan keberadaan berkas "manage.py" lalu jalan kan migrasi dengan perintah "python manage.py migrate". dan jalankan server django dengan perintah "python manage.py runserver".

        14. Buka http://localhost:8000 pada browser dan dapat dilihat bahwa aplikasi django telah berhasil dibuat.

        15. Jika ingin menonaktifkan virtual environment bisa langsung CTRL + C pada CMD atau jalankan perintah "deactivate" pada CMD.

        16. Sebelum setiap progres di push ke repo GitHub, saya membuat file .gitignore terlebih dahulu supaya berkas berkas lain tidak ikut ter-push ke repo GitHub saya.

        17. Buat branch utama dengan nama master "git branch -M master".

        18. Lalu lakukan add, commit dan push dari direktori lokal ke repo GitHub.
            git add .
            git commit -m "Create new project for Tugas 2"
            git push origin master

### "B. Membuat aplikasi dengan nama main pada proyek tersebut."

        1. Pertama saya masuk ke direktori proyek, dengan menuliskan perintah "cd garuda-store" di CMD.

        2. Sebelum saya membuat aplikasi main pada proyek saya, saya mengaktifkan virtual environment terlebih dahulu, dengan cara "env\Scripts\activate".

        3. Buat aplikasi baru dengan nama "main" dengan menggunakan perintah "python manage.py startapp main".

        4. Mendaftarkan apliaksi main ke dalam proyek, dengan membuka berkas settings.py dalam direktori "garuda-store", tambahkan "main" dalam daftar aplikasi yang terdapat pada variabel INSTALLED_APP. Maka aplikasi main berhasil dibuat.

### "C. Melakukan routing pada proyek agar dapat menjalankan aplikasi main."

        1. Saya mengonfigurasi routing URL proyek dengan membuat berkas "urls.py" pada level proyek, hal ini dilakukan supaya proyek dapat melakukan pemetaan ke rute URL pada aplikasi main.

        2. Buka "urls.py" dalam direktori "garuda_store", lalu import fungsi include dari django.urls seperti "from django.urls import path, include".

        3. Tambahkan rute URL berikut :
            urlpatterns = [
                ...
                path('', include('main.urls')),
                ...
            ]
        supaya dapat mengarahkan ke tampilan main dalam urlpatterns.

### "D. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib."

        1. Buka berkas "models.py" pada direktori aplikasi main.

        2. Lalu isi berkas "models.py" dengan class Product dan atribut-atribut wajib sesuai ketentuan. Seperti berikut :
            from django.db import models
            # Create your models here.
            class Product(models.Model):
                #atribut wajib 
                name = models.CharField(max_length=200)
                price = models.IntegerField()
                description = models.TextField()
                thumbnail = models.URLField()
                category = models.CharField(max_length=100)
                is_featured = models.BooleanField(default=False)

                #atribut opsional
                size = models.CharField(max_length=20, blank=True) # S, M, L, XL
                stock = models.IntegerField(default=0)


            def __str__(self):
                return f"{self.name} ({self.team})"
            # itu fungsinya buat nge-representasikan object Product jadi string yang lebih gampang dibaca.
        
        3. Setelah membuat model, setiap perubahan pada model basis data yang dibuat harus di migrasi untuk menghindari terjadinya error akibat tidak singkronnya kode dengan database.

        4. Caranya dengan menjalankan perintah "python manage.py makemigrations" yang menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data.

        5. Lalu jalankan perintah "python manage.py migrate" untuk melakukan pengaplikasian perubahan model yang tercantum dalam berkas migrasi ke basis data. 

### "E. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas saya."

        1. Buka berkas "views.py" yang ada pada aplikasi "main".

        2. Tambahkan "from django.shortcuts import render" jika belum ada.

        3. Tambahkan fungsi "show_main" yang menerima parameter request yang dimana fungsi ini akan mengatur permintaan HTTP dan mengembalikan yang sesuai. Seperti ini :
            # main/views.py
            from django.shortcuts import render

            def show_main(request):
                context = {
                    "app_name": "Garuda Store",
                    "student_name": "ZIbeon Jonriano Wisnumoerti",
                    "class_name": "PBP D"
                }
                return render(request, "main.html", context)
            
            variabel context disini adalah dictionary yang berisi data yang akan ditampilkan yaitu nama aplikasi, nama saya dan asal kelas saya (sesuai ketentuan).

            return render(request, "main.html", context) disini berguna untuk merender tampilan main.html. Request disini artinya objek permintaan HTTP yang dikirim oleh user. Lalu main.html adalah nama berkas templatenya.

        4. Buat folder atau direktori dengan nama "templates" dalam direktori main. Lalu buat & buka berkas "main.html" dan isi menggunakan kode yang menampilkan nama aplikasi, nama mahasiswa, dan asal kelasnya seperti berikut ini :
            <!-- main/templates/main/home.html -->
            <h1>{{ app_name }}</h1>
            <p>Nama Mahasiswa   : {{ student_name }}</p>
            <p>Kelas            : {{ class_name }}</p>

### "F. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py."

        1. Pertama saya mengonfigurasi routing URL aplikasi main dengan cara membuat berkas "urls.py" di dalam direktori main.

        2. Isi urls.py dengan kode : 
            from django.urls import path
            from main.views import show_main

            app_name = 'main'

            urlpatterns = [
                path('', show_main, name='show_main'),
            ]
        routing pada aplikasi main sudah selesai dilakukan.

        3. Jalankan proyek django dengan "python manage.py runserver" di CMD.

        4. Bukalah http://localhost:8000/ di web browser untuk melihat halaman yang telah dibuat.

### "G. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat."

        1. Buka halaman PWS pada https://pbp.cs.ui.ac.id.

        2. Login dengan akun SSO UI.

        3. Buat proyek baru dengan menekan tombol "Create New Project" dan buat project dengan nama "garudastore". Lalu tekan "Create New Project" di bawahnya.

        4. Setelah muncul dua informasi baru, yaitu mengenai Project Credentials dan Project Command. Simpan/salin credentials yang tampil ke tempat yang aman, karena seterusnya credentials ini tidak akan bisa kamu lihat lagi. Jangan jalankan dulu instruksi Project Command.

        5. Kemudian pada sidebar pilih proyek yang teolah dibuat, lalu buka tab "Environs". Klik "Raw Editor" dan copy paste isi file ".env.prod" yang ada pada direktori proyek di lokal komputer.
        6. Klik "Update All Variables".

        7. Pada "settings.py" di proyek Django yang sudah dibuat tadi, tambahkan URL deployment PWS "https://zibeon-jonriano-garudastore.pbp.cs.ui.ac.id/" pada ALLOWED_HOSTS menjadi seperti ini :
            ALLOWED_HOSTS = ["localhost", "127.0.0.1","zibeon-jonriano-garudastore.pbp.cs.ui.ac.id"]

        8. Setelah itu Lakukan git add, commit, dan push perubahan ini ke repositori GitHub.
            git add .
            git commit -m "Create model Product and deployment to PWS"
            git push origin master

        9. Jalankan perintah yang terdapat pada informasi Project Command pada halaman PWS. Ketika melakukan push ke PWS, akan ada window yang meminta username dan password. Masukkan username dan password yang sebelumnya disalin dari tahap ke 4.

        10. Pada side bar situs PWS, klik proyek yang telah dibuat. Disana juga dapat melihat status deployment proyek saat ini. Apabila statusnya "Building", artinya proyek masih dalam proses deployment. Apabila statusnya "Running", maka proyek sudah bisa diakses pada URL deployment. Selain itu, kita juga bisa menekan tombol "View Project" yang terdapat pada halaman proyek untuk melihat tampilan web yang sudah dibuat.

        11. Terakhir lakukan "git push pws master".


## "2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html."

![Bagan](./BaganRequestClient.png)

    Penjelasan Alur Sepemahaman Saya:
        1. Client (Browser) -> User mengirim request ke server (misalnya membuka https://zibeon-jonriano-garudastore.pbp.cs.ui.ac.id/).

        2. URL Configuration (urls.py) -> "urls.py" berfungsi sebagai router, ia akan mencocokan url yang diminta client dengan pola yang ada di "urlpatterns".

        3. Views (views.py) -> "views.py" ini berisi logika aplikasi, setelah menerima request dari "urls.py", view bisa langsung merender HTML (jika tidak butuh data dari database) ataupun meminta data dari "models.py".

        4. Models (models.py) -> "models.py" adalah representasi tabel database, jika view butuh data (misalnya daftar produk), view akan melakukan query ke model. Model lalu berkomunikasi dengan database untuk ambbil/simpan data.

        5. Database -> adalah tempat penyimpanan data sebenarnya, model akan melakukan data transaction (CRUD: Create, Read, Update, Delete). Hasil query dikembalikan ke "views.py".

        6. Template (HTML file) -> Setelah data dari model diterima, view akan memilih template HTML untuk merender data.

        7. Response -> Template yang sudah diisi data dikembalikan sebagai web page ke browser, dan client akhirnya melihat hasil tampilan di halaman web.

## "3. Jelaskan peran settings.py dalam proyek Django!".

    Dalam proyek Django, settings.py berfungsi sebagai pusat konfigurasi aplikasi. File ini mengatur berbagai aspek penting, seperti daftar aplikasi yang digunakan (INSTALLED_APPS), middleware, konfigurasi database, lokasi file statis dan media, kunci keamanan (SECRET_KEY), mode debug, host yang diizinkan (ALLOWED_HOSTS), serta pengaturan bahasa dan zona waktu. Singkatnya, settings.py menentukan bagaimana proyek Django dijalankan, berinteraksi dengan database, menangani keamanan, dan menampilkan konten ke pengguna.

## "4.Bagaimana cara kerja migrasi database di Django?".

    Menyinkronkan perubahan yang dibuat pada "models.py" dengan struktur tabel di database disebut migrasi database. Caranya: 

        1. Ketika kita mengubah atau menambah model, Django mencatat perubahan tersebut dalam file migrasi melalui perintah "python manage.py makemigrations". File migrasi ini berisi instruksi perubahan skema database. 

        2. Selanjutnya, perintah "python manage.py migrate" menjalankan instruksi tersebut ke database sehingga tabel dan kolom sesuai dengan definisi model terbaru. Dengan begitu, database selalu konsisten dengan kode model yang kita buat.

## "5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?".

    Django dijadikan framework pengantar dalam pembelajaran pengembangan perangkat lunak karena mudah dipelajari namun lengkap. Framework ini menyediakan banyak fitur bawaan seperti ORM, autentikasi, admin panel, dan templating, sehingga mahasiswa dapat fokus memahami konsep fundamental web development tanpa harus membuat semuanya dari nol. Dengan arsitektur Model-View-Template (MVT), Django membantu pemula mempelajari pemisahan tugas antara data, logika aplikasi, dan tampilan dengan jelas. Selain itu, Django mendorong praktik pengembangan perangkat lunak yang baik, seperti prinsip DRY (Don’t Repeat Yourself), serta memiliki dokumentasi lengkap dan komunitas besar. Framework ini juga relevan di dunia industri, sehingga pembelajaran Django memberi dasar yang kuat sekaligus pengalaman yang berguna untuk proyek nyata.

## "6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?".

    Untuk tutorial 1 yang telah saya kerjakan sebelumnya, menurut saya semua instruksi dan penjelasan terkait tutorial sudah disampaikan dengan baik dan detail, dan layanan bantuan jika mahasiswa mengalami masalah selama tutorial berlangsung juga sangat membantu mahasiswa dalam mengerjakan tutorial. Mungkin saran saya upaya ini bisa terus dipertahankan atau ditingkatkan lebih lagi untuk menunjang pengalaman belajar mahasiswa yang efektif dan menyenangkan, Terimakasih.

---

# Tugas 3: Implementasi Form dan Data Delivery pada Django

## 1.Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

    Data delivery misalnya XML/JSON memungkinkan pengiriman dan pertukaran data antar sistem yang berbeda dengan cara yang terstruktur dan terstandarisasi. Data delevery ini memungkinkan backend menyediakan data yang bisa dikonsumsi oleh klien lain (web, mobile, service lain). Ini penting untuk integrasi antar-sistem dan pemisahan frontend-backend.

## 2.Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?  

    Menurut saya, JSON umumnya lebih disukai untuk aplikasi web karena formatnya yang ringan, deskriptif, mudah dibaca, dan kompatibel dengan kerangka kerja JavaScript, serta mendukung penguraian yang cepat. Sebaliknya, XML lebih cocok untuk aplikasi yang membutuhkan representasi data yang kompleks dan validasi data yang mendalam. XML juga menawarkan deskripsi yang lebih rinci dan berbagai fitur tambahan. Jadi pemilihan antara JSON dan XML sangat bergantung pada kebutuhan spesifik proyek. 

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    
    Method `is_valid()` pada form Django berfungsi untuk memeriksa apakah data yang diinput pengguna sesuai dengan aturan validasi yang telah ditentukan pada form. Jika valid, method ini akan mengembalikan nilai `True` sehingga data dapat diproses atau disimpan ke database, sedangkan jika tidak valid, method ini mengembalikan `False` dan menyimpan pesan error yang bisa ditampilkan kepada pengguna. Dengan demikian, `is_valid()` penting untuk menjaga integritas data, mencegah error, serta memberikan umpan balik ketika terjadi kesalahan input.

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

    Kita membutuhkan csrf_token saat membuat form di Django karena token ini berfungsi sebagai mekanisme keamanan untuk mencegah Cross-Site Request Forgery (CSRF), yaitu serangan di mana penyerang mencoba mengirim request berbahaya ke server atas nama pengguna tanpa sepengetahuan mereka. Jika csrf_token tidak ditambahkan, form menjadi rentan dieksploitasi, penyerang dapat membuat halaman berisi form tersembunyi yang secara otomatis mengirim request ke aplikasi kita ketika pengguna yang sedang login membukanya. Akibatnya, data bisa dimanipulasi atau transaksi berbahaya dilakukan tanpa izin. Dengan csrf_token, server akan memverifikasi bahwa setiap request POST berasal dari form sah yang dibuat aplikasi, sehingga serangan semacam ini bisa dicegah.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    1. Pertama-tama saya memastikan terdapat model `Product` yang sudah dibuat sebelumnya di models.py.

    2. Saya membuat folder templates dan mengisinya dengan `base.html` di directory ROOT Project, yang nantinya bisa di extends oleh file html lainnya.

    3. Lalu saya menambahkan kode:
        ...
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
                'APP_DIRS': True,
                ...
            }
        ]
        ...
        Agar file `base.html` terdeteksi sebagai file template.

    4. Selanjutnya saya membuat beberapa fungsi di `main\views.py` yaitu :
        def products_json(request):
            products = Product.objects.all()
            data = serializers.serialize("json", products)
            return HttpResponse(data, content_type="application/json")

        def products_xml(request):
            products = Product.objects.all()
            data = serializers.serialize("xml", products)
            return HttpResponse(data, content_type="application/xml")

        def product_json_by_id(request, id):
            product = get_object_or_404(Product, pk=id)
            data = serializers.serialize("json", [product])
            return HttpResponse(data, content_type="application/json")

        def product_xml_by_id(request, id):
            product = get_object_or_404(Product, pk=id)
            data = serializers.serialize("xml", [product])
            return HttpResponse(data, content_type="application/xml")
        
    5. Membuat routing URL untuk masing-masing fungsi yang baru ditambahkan di `views.py` tadi, dengan :
        path("products/json/", products_json, name="products_json"),
        path("products/xml/", products_xml, name="products_xml"),
        path("products/json/<int:id>/", product_json_by_id, name="product_json_by_id"),
        path("products/xml/<int:id>/", product_xml_by_id, name="product_xml_by_id"),

    6. Lalu saya mengedit `main.html` yang berada di folder main agar memiliki tombol "Add Product" yang langsung mendirect ke halaman form dan menampilkan deretan produk yang sudah di add. Setelah produk sudah di Add, user bisa melihat detail produk dengan menekan tombol "Detail pada daftar produk yang tampil di halaman.

    7. Lalu saya membuat `add_product.html` yang berisi form penambahan produk dan `product_detail.html` yang berisi deskripsi detail dari produk yang telah ditambahkan.

    8. Tidak lupa bahwa saya membuat fungsi tambahan lagi di `views.py` dalam folder main agar html yang dibuat sebelumnya dapat berfungsi. Kode nya sebagai berikut :
        def add_product(request):
            form = ProductForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                form.save()
                return redirect('main:show_main')

            context = {'form': form}
            return render(request, "add_product.html", context)


        def product_detail(request, id):
            product = get_object_or_404(Product, pk=id)

            context = {
                'product': product
            }

            return render(request, "product_detail.html", context)
    
    9. Selanjutnya saya membuat routing URL lagi untuk funsgi "add_product" dan "product_detail".
        path("products/<int:id>/", product_detail, name="product_detail"),
        path("products/add/", add_product, name="add_product"),

    10. Menambahkan daftar domain web ke `settings.py` yang ada di folder ROOT project supaya user dapat melakukan "Add Product" (Pengisian Form) melalui domain tersebut karena berasal dari sumber yang terpercaya.
            CSRF_TRUSTED_ORIGINS = [
                "https://zibeon-jonriano-garudastore.pbp.cs.ui.ac.id"
            ]

## 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    Untuk saat ini belum ada.

## 7.  Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

    1. JSON
    `http://127.0.0.1:8000/products/json/` 
![json](./products_json_SS_POSTMAN.png)

    2. XMl
    `http://127.0.0.1:8000/products/xml/`
![xml](./products_xml_SS_POSTMAN.png)

    3. JSON by id
    `http://127.0.0.1:8000/products/json/1`
![json_by_id](./products_json_by_id_SS_POSTMAN.png)

    4. XML by id
    `http://127.0.0.1:8000/products/xml/1`
![xml_by_id](./products_xml_by_id_SS_POSTMAN.png)
        

---
# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django

## 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

AuthenticationForm adalah form bawaan Django yang disediakan di django.contrib.auth.forms untuk menangani proses login. Form ini meminta username dan password, lalu memvalidasi apakah pasangan kredensial tersebut sesuai dengan user yang terdaftar di database.

Kelebihan :
-Sudah terintegrasi penuh dengan sistem autentikasi Django.
-Secara otomatis melakukan validasi username dan password.
-Mudah digunakan, cukup import dan panggil dalam view.
-Bisa di-customize jika ingin menambahkan field lain (misalnya email).

Kekurangan :
-Terbatas pada field bawaan (username & password). Kalau butuh login dengan cara lain (misal nomor HP, OTP, atau social login), perlu menulis form custom.
-Pesan error standar (default) kadang perlu dimodifikasi agar lebih ramah pengguna.

## 2.  Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

**Autentikasi** merupakan proses **verifikasi identitas** pengguna (contohnya: apakah username & password benar). Seperti menjawab pertanyaan: “Kamu siapa?”. 

Implementasi Autentikasi di Django dengan menggunakan sistem login/logout dengan authenticate(), login(), logout(), dan AuthenticationForm.
    
Sedangkan **Otorisasi** merupakan proses **pemberian izin** setelah identitas diverifikasi (contohnya: apakah user boleh mengakses halaman admin). Seperti menjawab pertanyaan: “Kamu boleh melakukan apa?”

Implementasi Otorisasi di Django dengan menggunakan sistem permissions dan groups.
-Bisa pakai decorator seperti @login_required, @permission_required, atau user.is_staff / user.is_superuser.
-Middleware AuthenticationMiddleware otomatis melampirkan objek request.user ke setiap request.

## 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

### Cookie
Cookies adalah data kecil yang disimpan di browser user dan dikirim bersama setiap request ke server.

**Kelebihan**
-Sederhana dan langsung → Mudah digunakan untuk menyimpan data sederhana (misalnya preferensi bahasa, dark/light mode).
-Persisten → Bisa bertahan di browser meskipun user menutup aplikasi/web, tergantung expiry.
-Dapat diakses client-side → JavaScript bisa membaca/mengatur cookies (jika tidak diberi flag HttpOnly).
-Tidak perlu server-side storage → Semua data ada di browser, sehingga tidak membebani server.

**Kekurangan**
-Terbatas ukuran → Umumnya hanya 4KB per cookie.
-Dikirim di setiap request → Membebani jaringan karena ikut dikirim di header HTTP.
-Keamanan rendah → Rentan terhadap pencurian data (misalnya melalui XSS) jika tidak diamankan dengan HttpOnly, Secure, SameSite.
-Mudah dimanipulasi user → Karena tersimpan di client, user bisa mengubah isinya.

### Session
Session adalah data state yang disimpan di server, biasanya hanya disimpan identifier (session ID) di browser (misalnya lewat cookies atau URL).

**Kelebihan**
-Lebih aman → Data penting disimpan di server, bukan di browser.
-Mendukung data lebih besar/kompleks → Tidak terbatas 4KB seperti cookie.
-Tidak dikirim di setiap request (hanya session ID) → Lebih efisien daripada menyimpan semua data di cookies.
-Kontrol penuh di server → Admin bisa menghapus atau memodifikasi session kapan saja.

**Kekurangan**
-Membebani server → Karena semua data user disimpan di server-side memory/database.
-Tidak persisten tanpa konfigurasi tambahan → Session biasanya hilang saat browser ditutup atau setelah idle timeout.
-Butuh mekanisme tracking → Biasanya melalui session ID di cookies; jika bocor (session hijacking), akun bisa diambil alih.
-Skalabilitas sulit → Pada aplikasi besar, harus ada mekanisme penyimpanan terdistribusi (misalnya Redis, Memcached) agar session bisa diakses di banyak server.

## 4.  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

**Tidak sepenuhnya aman**
Cookies punya beberapa risiko keamanan:
-Session hijacking (pencurian session ID).
-XSS (Cross-Site Scripting) bisa mencuri cookie.
-CSRF (Cross-Site Request Forgery) bisa memanfaatkan cookie aktif.

Namun risiko tersebut bisa ditangani dengan ini:
- `SESSION_COOKIE_HTTPONLY = True`  
  → Mencegah cookie session diakses melalui JavaScript (lebih aman terhadap XSS).

- `SESSION_COOKIE_SECURE = True`  
  → Membuat cookie hanya dikirim melalui koneksi HTTPS, sehingga tidak bocor lewat HTTP.

- `CSRF_COOKIE_HTTPONLY = True` + `CSRF_COOKIE_SECURE = True`  
  → Melindungi CSRF token agar tidak bisa diambil via JavaScript dan hanya dikirim lewat HTTPS.

- **Middleware**:  
  `CsrfViewMiddleware`  
  → Secara otomatis memvalidasi token CSRF di setiap request `POST`, sehingga mencegah serangan CSRF.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### 1. Membuat fungsi dan form registrasi, buka views.py lalu tambahkan
`from django.contrib.auth.forms import UserCreationForm`
`from django.contrib import messages`
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

### 2. Buat register.html di main/templates
```
<!-- main\templates\register.html -->
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div>
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```

### 3. Lalu melakukan routing fungsi register ke urls.py 
`from main.views import register`
```
urlpatterns = [
    ...
    path('register/', register, name='register'),
]
```

### 4. Membuat fungsi login, buka views.py lalu tambahkan
`from django.contrib.auth.forms import UserCreationForm, AuthenticationForm`
`from django.contrib.auth import authenticate, login`

### 5. Tambahkan funsgi login_user ke dalam views.py yang berfungsi mengautentifikasi pengguna yang ingin login.
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

### 6. buat login.html di main/templates seperti :
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

### 7. Lakukan routing fungsi login_user ke urls.py dengan tambahkan :

`from main.views import login_user`
```
urlpatterns = [
   ...
   path('login/', login_user, name='login'),
]
```

### 8. Membuat fungsi logout_user di views.py dengan mengimport
`from django.contrib.auth import authenticate, login, logout` dan buat fungsinya seperti:
```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

### 9. Tambahkan button logout di main.html
```
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```

### 10.Lakukan routing fungsi logout_user ke urls.py dengan 
`from main.views import logout_user`
```
urlpatterns = [
   ...
   path('logout/', logout_user, name='logout'),
]
```

### 11. Menrestriksi halaman main dan detail product dengan menambahkan import 
`from django.contrib.auth.decorators import login_required`

### 12. Tambahkan decorator `@login_required(login_url='/login')` diatas setiap fungsi yang memerlukan auntetikasi login, jadi halaman tsb hanya bisa diakses oleh pengguna saat sudah login 

### 14. Menggunakan data dari Cookies, pertama-tama bukak views.py lalu tambahkan
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

### 15. lalu ubah kode di fungsi login_user untuk menyimpan last_login yang berisi timestamp terakhir kali pengguna melakukan login. Kita dapat memperoleh ini dengan mengganti kode yang ada pada blok if form.is_valid() menjadi seperti berikut.
```
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```

### 16. Pada fungsi show_main, tambahkan potongan kode 'last_login': request.COOKIES['last_login'] ke dalam variabel context. 
```
context = {
        'app_name': "Garuda Store",
        'student_name': "Zibeon Jonriano Wisnumoerti",
        'class_name': "PBP D",
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
```

### 17. Ubah fungsi logout_user untuk mengapus cookie last_login setelah melakukan logout
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
lalu setelah itu menambahkan potongan kode di main.html pada main/templates 
```
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

### 18. Menghubungkakn models Product dengan User, pertama-tama dengan mengimport kode ini di models.py 
```
from django.contrib.auth.models import User
```

### 19. Tambahkan potongan kode berikut pada models Product
```
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # tambahkan ini
```

### 20 Buka views.pydan ubah fungsi add_product menjadi seperti ini
```
@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)  # jika ada field file seperti thumbnail

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)      # jangan langsung save
        product.user = request.user           # set owner sesuai user yang login
        product.save()                         # baru save ke DB
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "add_product.html", context)
```

### 21. Memodifikasi show_main sehingga menjadi seperti ini :
```
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        products = Product.objects.all()
    else : 
        products = Product.objects.filter(user=request.user)

    context = {
        'app_name': "Garuda Store",
        'student_name': "Zibeon Jonriano Wisnumoerti",
        'class_name': "PBP D",
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)

```

### 22. Tambahkan block code dibawah ini untuk menerapkan filter product di main.html
```
<a href="?filter=all">
    <button type="button">All Products</button>
</a>
<a href="?filter=my">
    <button type="button">My Products</button>
</a> 
```

### 23. Selanjutnya saya menampilkan nama seller di setiap product details di product yag dibuat olehnya dengan menambah kode berikut
```

<!-- Tambahkan kode ini -->
{% if product.user %}
    <p>Seller: {{ product.user.username }}</p>
{% else %}
    <p>Seller: Anonymous</p>
{% endif %}
{% endblock content %}
```

### 24. Selanjutnya saya jug amenampilkan informasi nama pengguna yang sedang login di main.html dengan menambah kode ini
```
{% if request.user.is_authenticated %}
    <h2>Hallo, {{ request.user.username }}!</h2>
{% else %}
    <h2>Hallo, Guest!</h2>
{% endif %}
```
kode ini ditambahkan persis diatas informasi sesi login terakhir.

### 25. Setelah selesai saya dapat me-run server dengan python manage.py runserver

### 26. Membuat 2 akun baru dan masing masing membuat 3 product baru.
