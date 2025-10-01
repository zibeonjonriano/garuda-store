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

---

# Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS

## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Jika terdapat beberapa CSS selector yang berlaku untuk satu elemen HTML, browser akan memilih yang paling spesifik berdasarkan aturan berikut (urutan prioritas):
1. Inline Style -> ditulis langsung pada elemen dengan atribut style="". contohj: 
`<p style="color:red;">Teks</p>`
2. ID Selector (#id) -> contoh:
`#judul { color: blue; }`
3. Class, Pseudo-class, dan Attribute Selector (.class, :hover, [type="text"]) -> contoh:
`.teks { color: purple; }`
4. Element / Tag Selector (p, div, h1) -> contoh:
`p { color: black; }`
5. Universal Selector (*), inheritance, dan default browser -> paling rendah.

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Karena responsive design merupakan teknik agar tampilan web dapat menyesuaikan ukuran layar (PC, tablet, smartphone) tanpa mengurangi kenyamanan pengguna. Hal ini penting karena mayoritas pengguna internet sekarang mengakses lewat smartphone, meningkatkan user experience (UX) seperti mudah dibaca, navigasi enak, lalu SEO lebih baik karena Google mengutamakan mobile-friendly site, mengurangi kebutuhan membuat aplikasi/web versi terpisah.
Contoh :
-Sudah responsive : Youtube, Tokopedia, Instagram Web
-Belum responsive : Siak-Ng

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

1. Margin = ruang di luar border, jarak antar elemen.
`div { margin: 20px; }`
→ memberi ruang kosong antara elemen.

2. Border = garis tepi di sekeliling elemen.
`div { border: 2px solid black; }`
→ batas antara elemen dengan sekitarnya.

3. Padding = ruang antara isi konten dan border.
`div { padding: 10px; }`
→ memberi jarak antara teks/gambar di dalam elemen dan tepi border.

## 4.  Jelaskan konsep flex box dan grid layout beserta kegunaannya!
1. Flexbox (Flexible Box Layout)

Digunakan untuk mengatur elemen dalam 1 dimensi (baris atau kolom).
Berguna untuk: Menyusun navbar horizontal/vertikal, Mengatur alignment (center, space-between, space-around), Membuat layout responsif lebih fleksibel.
Contoh:
```
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

2. Grid Layout

Digunakan untuk layout 2 dimensi (baris dan kolom).
Cocok untuk: Layout halaman penuh (header, sidebar, content, footer), Desain kompleks seperti galeri foto.

Contoh:
```
.container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  grid-template-rows: auto auto;
  gap: 10px;
}
```

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!


### 1. Implementasi fungsi untuk menghapus dan mengedit product

**Edit Product**
1. Buka `views.py` lalu buat funsgi baru bernama `edit_product`
```
@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)
```

2. Buat `edit_product.html` di `main\templates`
```
{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Edit Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

3. Buka `urls.py` untuk melakukan routing tambahkan  `from main.views import edit_product` , `path('product/<int:id>/edit', edit_product, name='edit_product'),` di urlpatterns.

4. Perbarui loop pada `main.html` supaya muncul tombol edit
```
{% for product in products %}
<div>
<h2><a href="{% url 'main:product_detail' product.id %}">{{ product.name }}</a></h2>

<p><b>{{ product.get_category_display }}</b>{% if product.is_featured %} | 
  <b>Featured</b>{% endif %}{% if product.is_product_hot %} | 
  <b>Hot</b>{% endif %} | <i>{{ product.created_at|date:"d M Y H:i" }}</i> 
  | Views: {{ product.product_views }}</p>

{% if product.thumbnail %}
<img src="{{ product.thumbnail }}" alt="thumbnail" width="150" height="100">
<br />
{% endif %}

<p>{{ product.description|truncatewords:25 }}...</p>

<p>
    <a href="{% url 'main:product_detail' product.id %}"><button>Check Product</button></a>
    {% if user.is_authenticated and product.user == user %}
    <a href="{% url 'main:edit_product' product.pk %}">
        <button>
            Edit
        </button>
    </a>
    {% endif %}
</p>

</div>
<hr>
{% endfor %}
```

**Delete Product**
1. buat fungsi baru dengan nama `delete_product` di `views.py` yang nerima pameter request dan id
```
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
2. Buka `urls.py` untuk melakukan routing tambahkan  `from main.views import delete_product` , `path('product/<int:id>/delete', delete_product, name='delete_product'),` di urlpatterns.


3. Perbarui loop pada `main.html` supaya muncul tombol delete
```
{% for product in products %}
<div>
 <h2><a href="{% url 'main:product_detail' product.id %}">{{ product.name }}</a></h2>

 <p><b>{{ product.get_category_display }}</b>{% if product.is_featured %} | 
   <b>Featured</b>{% endif %}{% if product.is_product_hot %} | 
   <b>Hot</b>{% endif %} | <i>{{ product.created_at|date:"d M Y H:i" }}</i> 
   | Views: {{ product.product_views }}</p>

 {% if product.thumbnail %}
 <img src="{{ product.thumbnail }}" alt="thumbnail" width="150" height="100">
 <br />
 {% endif %}

 <p>{{ product.description|truncatewords:25 }}...</p>
 
 <p>
     <a href="{% url 'main:product_detail' product.id %}"><button>Read More</button></a>
     {% if user.is_authenticated and product.user == user %}
     <a href="{% url 'main:edit_product' product.pk %}">
         <button>
             Edit
         </button>
     </a>
     <a href="{% url 'main:delete_product' product.pk %}">
      <button>
          Delete
      </button>
  </a>
     {% endif %}
 </p>
 
</div>
<hr>
{% endfor %}
```

### 2. Buat Navigation Bar pada aplikasi

1. Buat `navbar.html` di `templates/` di root directory. Isinya :
```
<nav>
  <h1>Garuda Store</h1>

  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="{% url 'main:add_product' %}">Add Product</a></li>
  </ul>

  {% if user.is_authenticated %}
    <div>
      <span>Welcome, {{ name|default:user.username }}</span>
      <span>{{ student_name|default:"Student" }} - {{ class_name|default:"Class" }}</span>
      <a href="{% url 'main:logout' %}">Logout</a>
    </div>
  {% else %}
    <div>
      <a href="{% url 'main:login' %}">Login</a>
      <a href="{% url 'main:register' %}">Register</a>
    </div>
  {% endif %}
</nav>
```

2. Menautkan navbar ke `main.html`
```
{% extends 'base.html' %}
{% block content %}
{% include 'navbar.html' %}
...
{% endblock content%}
```
### 3. Konfigurasi Static Files pada Aplikasi

1.Pada settings.py, tambahkan middleware WhiteNoise.
```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
    ...
]
```

2. Pada `settings.py`, pastikan variabel `STATIC_ROOT`, `STATICFILES_DIRS`, dan `STATIC_URL` dikonfigurasikan seperti ini (jika belum ada, bisa ditambahkan saja):
```
STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static' # merujuk ke /static root project pada mode development
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
```

### 4. Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:

1. Buat file `global.css` di `/static/css`

2. Menghubungkan `global.css` dan script Tailwind ke base.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
  </head>
  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

4. Menambahkan custom styling ke global.css
```
body {
    background-color: #d0cec1;
}

* {
    background-color: transparent;
}

.form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bbff00;
    border-radius: 0.375rem;
}
.form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
    border-color: #b3f300;
    box-shadow: 0 0 0 3px #b3f300;
}

.form-style input[type="checkbox"] {
    width: 1.25rem;
    height: 1.25rem;
    padding: 0;
    border: 2px solid #deff82;
    border-radius: 0.375rem;
    background-color: #1f2937;
    cursor: pointer;
    position: relative;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
}

.form-style input[type="checkbox"]:checked {
    background-color: #b3f300;
    border-color: #b3f300;
}

.form-style input[type="checkbox"]:checked::after {
    content: '✓';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: #1f2937;
    font-weight: bold;
    font-size: 0.875rem;
}

.form-style input[type="checkbox"]:focus {
    outline: none;
    border-color:#b3f300;
    box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.1);
}
```

### 5. Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
1. Dengan kode dibawah ini, saya juga sudah menyesuaikan peletakan link category di navbar menggunakan dropdown option dikarenakan katgori produk dalam toko sayta lumayan banyak. Lalu juga saya telah menyesuaikan tampilan navbar di mobile app.
```
<nav class="fixed top-0 left-0 w-full bg-[#010101] border-white shadow-xg z-50 border-b border-gray-100">
    <div class="max-w-7xl mx-auto px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <h1 class="text-xl font-semibold text-white">
            <span class="text-[#b3f300]">Garuda</span> Store
          </h1>
        </div>
        
        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center space-x-8 absolute left-1/2 transform -translate-x-1/2">
          <a href="/" class="text-white hover:text-[#b3f300] font-medium transition-colors">
            Home
          </a>
          <a href="{% url 'main:add_product' %}" class="text-white hover:text-[#b3f300] font-medium transition-colors">
            Add Product
          </a>
        </div>

        <div class="hidden md:flex items-center space-x-4">

    </div>
        
        <!-- Desktop User Section -->
        <div class="hidden md:flex items-center space-x-6">
          {% if user.is_authenticated %}
            <div class="text-right">
              <div class="text-sm font-medium text-white">{{ name|default:user.username }}</div>
              <div class="text-xs text-gray-300">{{ student_name|default:"Student" }} - {{ class_name|default:"Class" }}</div>
            </div>
            <a href="{% url 'main:logout' %}" class="text-red-600 hover:text-red-700 font-medium transition-colors">
              Logout
            </a>
          {% else %}
            <a href="{% url 'main:login' %}" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">
              Login
            </a>
            <a href="{% url 'main:register' %}" class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded font-medium transition-colors">
              Register
            </a>
          {% endif %}
        </div>
        
        <!-- Mobile Menu Button -->
        <div class="md:hidden flex items-center">
          <button class="mobile-menu-button p-2 text-white hover:text-[#b3f300] transition-colors">
            <span class="sr-only">Open menu</span>
            <div class="w-6 h-6 flex flex-col justify-center items-center">
              <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm"></span>
              <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm my-0.5"></span>
              <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm"></span>
            </div>
          </button>
        </div>
      </div>
    </div>
    <!-- Mobile Menu -->
    <div class="mobile-menu hidden md:hidden bg-[#232323] border-t border-gray-200">
      <div class="px-6 py-4 space-y-4">
        <!-- Mobile Navigation Links -->
        <div class="space-y-1">
            <a href="/" class="block text-white hover:text-[#b3f300] font-medium py-3 transition-colors">
                Home
            </a>
            <a href="{% url 'main:add_product' %}" class="block text-white hover:text-[#b3f300] font-medium py-3 transition-colors">
                Add Product
            </a>


            <!-- Category Filter as Links -->
            {% for key, value in categories %}
                <a href="{% url 'main:show_main' %}?category={{ key }}{% if current_owner != 'all' %}&owner={{ current_owner }}{% endif %}" 
                class="block text-gray-100 hover:text-[#b3f300] font-medium py-3 transition-colors {% if current_category == key %}font-bold{% endif %}">
                {{ value }}
                </a>
            {% endfor %}
        </div>
        
        <!-- Mobile User Section -->
        <div class="border-t border-gray-200 pt-4">
          {% if user.is_authenticated %}
            <div class="mb-4">
              <div class="font-medium text-white">{{ name|default:user.username }}</div>
              <div class="text-sm text-white">{{ student_name|default:"Student" }} - {{ class_name|default:"Class" }}</div>
            </div>
            <a href="{% url 'main:logout' %}" class="block text-red-600 hover:text-red-700 font-medium py-3 transition-colors">
              Logout
            </a>
          {% else %}
            <div class="space-y-3">
              <a href="{% url 'main:login' %}" class="block text-gray-600 hover:text-gray-900 font-medium py-3 transition-colors">
                Login
              </a>
              <a href="{% url 'main:register' %}" class="block bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-4 rounded text-center transition-colors">
                Register
              </a>
            </div>
          {% endif %}
        </div>
      </div>
    </div>
    <script>
      const btn = document.querySelector("button.mobile-menu-button");
      const menu = document.querySelector(".mobile-menu");
    
      btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
      });
    </script>
  </nav>
```

### 6. Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin.

**1. Styling Halaman Login**
Ubah berkas `login.html` pada subdirektori main/templates menjadi seperti berikut:
```
{% extends 'base.html' %}

{% block meta %}
<title>Login - Garuda Store</title>
{% endblock meta %}

{% block content %}
<div class="bg-[#232323] w-full min-h-screen flex items-center justify-center p-8">
  <div class="max-w-md w-full">
    <div class="bg-[#010101] rounded-lg border border-gray-200 p-6 sm:p-8 form-style">
      <div class="text-center mb-8">
        <h1 class="text-2xl font-bold text-white mb-2">Sign In</h1>
        <p class="text-white">Welcome back to Garuda Store</p>
      </div>

      <!-- Form Errors Display -->
      {% if form.non_field_errors %}
        <div class="mb-6">
          {% for error in form.non_field_errors %}
            <div class="px-4 py-3 rounded-md text-sm border bg-red-50 border-red-200 text-red-700">
              {{ error }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

      {% if form.errors %}
        <div class="mb-6">
          {% for field, errors in form.errors.items %}
            {% if field != '__all__' %}
              {% for error in errors %}
                <div class="px-4 py-3 rounded-md text-sm border bg-red-50 border-red-200 text-red-700 mb-2">
                  <strong>{{ field|title }}:</strong> {{ error }}
                </div>
              {% endfor %}
            {% endif %}
          {% endfor %}
        </div>
      {% endif %}

      <form method="POST" action="" class="space-y-6">
        {% csrf_token %}
        
        <div>
          <label for="username" class="block text-sm font-medium text-white mb-2">Username</label>
          <input 
            id="username" 
            name="username" 
            type="text" 
            required 
            class="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-green-500 transition-colors bg-gray-800 text-white placeholder-white" 
            placeholder="Enter your username">
        </div>

        <div>
          <label for="password" class="block text-sm font-medium text-white mb-2">Password</label>
          <input 
            id="password" 
            name="password" 
            type="password" 
            required 
            class="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-green-500 transition-colors bg-gray-800 text-white placeholder-white" 
            placeholder="Enter your password">
        </div>

        <button 
          type="submit" 
          class="w-full bg-[#b3f300] text-black font-medium py-3 px-4 rounded-md hover:bg-[#bfd59f] transition-colors">
          Sign In
        </button>
      </form>

      <!-- Messages Display -->
      {% if messages %}
        <div class="mt-6">
          {% for message in messages %}
            <div 
              class="
                px-4 py-3 rounded-md text-sm border
                {% if message.tags == 'success' %}
                  bg-green-50 border-green-200 text-green-700
                {% elif message.tags == 'error' %}
                  bg-red-50 border-red-200 text-red-700
                {% else %}
                  bg-gray-50 border-gray-200 text-gray-700
                {% endif %}
              ">
              {{ message }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

      <div class="mt-6 text-center pt-6 border-t border-gray-200">
        <p class="text-white text-sm">
          Don't have an account? 
          <a href="{% url 'main:register' %}" class="text-[#b3f300] hover:text-[#bfd59f] font-medium">
            Register Now
          </a>
        </p>
      </div>
    </div>
  </div>
</div>
{% endblock content %}
```

**2. Styling Halaman Register**
Ubah berkas `register.html` pada subdirektori main/templates menjadi seperti berikut:
```
{% extends 'base.html' %}

{% block meta %}
<title>Register - Garuda Store</title>
{% endblock meta %}

{% block content %}
<div class="form-style">
  <div class="min-h-screen bg-[#232323] flex items-center justify-center p-8">
    <div class="max-w-md w-full relative z-10">
      <div class="bg-[#010101] border border-gray-200 rounded-lg p-8 shadow-sm">
      <div class="text-center mb-8">
        <h2 class="text-2xl font-semibold text-white mb-2">Join Us</h2>
        <p class="text-white">Create your Garuda Store account</p>
      </div>

      <!-- Form Errors Display -->
      {% if form.non_field_errors %}
        <div class="mb-6">
          {% for error in form.non_field_errors %}
            <div class="px-4 py-3 rounded text-sm border bg-red-50 border-red-200 text-red-700">
              {{ error }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

      {% if form.errors %}
        <div class="mb-6">
          {% for field, errors in form.errors.items %}
            {% if field != '__all__' %}
              {% for error in errors %}
                <div class="px-4 py-3 rounded text-sm border bg-red-50 border-red-200 text-red-700 mb-2">
                  <strong>{{ field|title }}:</strong> {{ error }}
                </div>
              {% endfor %}
            {% endif %}
          {% endfor %}
        </div>
      {% endif %}

      <form method="POST" action="" class="space-y-5">
        {% csrf_token %}
        
        <div>
          <label for="username" class="block text-sm font-medium text-white mb-2">Username</label>
          <input 
            id="username" 
            name="username" 
            type="text" 
            required 
            class="w-full px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-green-500 transition duration-200 bg-gray-800 text-white placeholder-white" 
            placeholder="Choose a username">
        </div>

        <div>
          <label for="password1" class="block text-sm font-medium text-white mb-2">Password</label>
          <input 
            id="password1" 
            name="password1" 
            type="password" 
            required 
            class="w-full px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-green-500 transition duration-200 bg-gray-800 text-white placeholder-white" 
            placeholder="Create a password">
        </div>

        <div>
          <label for="password2" class="block text-sm font-medium text-white mb-2">Confirm Password</label>
          <input 
            id="password2" 
            name="password2" 
            type="password" 
            required 
            class="w-full px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-green-500 transition duration-200 bg-gray-800 text-white placeholder-white" 
            placeholder="Confirm your password">
        </div>

        <button 
          type="submit" 
          class="w-full bg-[#b3f300] text-black font-medium py-3 px-4 rounded hover:bg-[#bfd59f] focus:outline-none focus:ring-2 focus:ring-[#bfd59f]
           focus:ring-offset-2 transition duration-200">
          Create Account
        </button>
      </form>

      <!-- Messages Display -->
      {% if messages %}
        <div class="mt-6">
          {% for message in messages %}
            <div 
              class="
                px-4 py-3 rounded text-sm border
                {% if message.tags == 'success' %}
                  bg-green-50 border-green-200 text-green-700
                {% elif message.tags == 'error' %}
                  bg-red-50 border-red-200 text-red-700
                {% else %}
                  bg-gray-50 border-gray-200 text-gray-700
                {% endif %}
              ">
              {{ message }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

      <div class="mt-6 text-center">
        <p class="text-gray-500 text-sm">
          Already have an account? 
          <a href="{% url 'main:login' %}" class="text-[#b3f300] hover:text-[#bfd59f] font-medium">
            Sign In
          </a>
        </p>
      </div>
      </div>
    </div>
  </div>
</div>
{% endblock content %}
```

**3. Styling Halaman Home**
Buat file `card_product.hrtml` di `main/templates`, ubah juga sedikit kode yang ada di tutorial agar bisa menampilkan harga dari product. Saya juga menggunakan `{% load humanize %}` digunakan untuk memuat template filter dari paket humanize, yang berisi filter siap pakai untuk menampilkan data dalam format lebih “manusiawi” (human-readable). Oleh karena itu saya juga harus memasukan `'django.contrib.humanize'` di `INSTALLED_APPS` di `settings.py`. Load humanize ini saya gunakan untuk memberikan tampilan harga produk yang mudah dibaca manusia yaitu `Rp {{ product.price|intcomma }}`. Lalu kodenya seperti ini:
```
{% load static %}
{% load humanize %}
<article class="bg-[#010101] rounded-lg border border-[#010101] hover:shadow-lg transition-shadow duration-300 overflow-hidden">
  <!-- Thumbnail -->
  <div class="aspect-[16/9] relative overflow-hidden">
    {% if product.thumbnail %}
      <img src="{{ product.thumbnail }}" alt="{{ product.name }}" class="w-full h-full object-cover">
    {% else %}
      <div class="w-full h-full bg-gray-200"></div>
    {% endif %}

    <!-- Category Badge -->
    <div class="absolute top-3 left-3">
      <span class="inline-flex items-center px-2.5 py-0.5 rounded-md text-xs font-medium bg-[#bfd59f] text-green">
        {{ product.get_category_display }}
      </span>
    </div>

    <!-- Status Badges -->
    <div class="absolute top-3 right-3 flex space-x-2">
      {% if product.is_featured %}
        <span class="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-yellow-100 text-yellow-800">
          Featured
        </span>
      {% endif %}
      {% if product.is_product_hot %}
        <span class="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-red-100 text-red-800">
          Hot
        </span>
      {% endif %}
    </div>
  </div>

  <!-- Content -->
  <div class="p-5">
    <div class="flex items-center text-sm text-white mb-3">
      <time datetime="{{ product.created_at|date:'c' }}"
        {{ product.created_at|date:"M j, Y" }}
      </time>
      <span class="mx-2">•</span>
      <span>{{ product.product_views }} views</span>
    </div>

    <h3 class="text-lg font-bold text-white mb-3 line-clamp-2 leading-tight">
      <a href="{% url 'main:product_detail' product.id %}" class="hover:text-[#b3f300] transition-colors">
        {{ product.name }}
      </a>
    </h3>

    <!-- Price -->
    <h3 class="text-xl text-[#b3f300] font-semibold text-sm mb-3">
    Rp {{ product.price|intcomma }}
    </h3>

    <p class="text-white text-sm leading-relaxed line-clamp-3 mb-4">
      {{ product.description|truncatewords:20 }}
    </p>

    <!-- Action Buttons -->
    {% if user.is_authenticated and product.user == user %}
      <div class="flex items-center justify-between pt-4 border-t border-gray-100">
        <!-- Check Product as Button -->
        <a href="{% url 'main:product_detail' product.id %}" 
        class="px-4 py-2 bg-[#b3f300] text-black rounded-md text-sm font-medium hover:bg-[#bfd59f] transition-colors">
        Check Product →
        </a>

        <div class="flex space-x-2 ">
          <a href="{% url 'main:edit_product' product.id %}" class="text-white hover:text-[#bfd59f] text-sm transition-colors">
            Edit
          </a>
          <a href="{% url 'main:delete_product' product.id %}" class="text-red-600 hover:text-red-700 text-sm transition-colors">
            Delete
          </a>
        </div>
      </div>
    {% else %}
      <div class="pt-4 border-t border-gray-100">
        <a href="#" 
        class="inline-block px-4 py-2 bg-[#b3f300] text-black rounded-md text-sm font-medium hover:bg-[#bfd59f] transition-colors">
        Check Product →
        </a>
      </div>
    {% endif %}
  </div>
</article>
```

**4. Saya juga mengcustom background color dari input field dan text inputnya dengan memodifikasi `forms.py`, untuk kepentingan styling `add_product.html` dan `edit_product.html`.
```
# main/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","price", "description", "thumbnail", "category", "is_featured", "size", "stock"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "bg-gray-800 text-white placeholder-white px-3 py-2 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-[#b3f300] focus:border-transparent",
                "placeholder": "Enter product name"
            }),
            "price": forms.NumberInput(attrs={
                "class": "bg-gray-800 text-white placeholder-white px-3 py-2 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-[#b3f300] focus:border-transparent",
                "placeholder": "Enter price"
            }),
            "description": forms.Textarea(attrs={
                "class": "bg-gray-800 text-white placeholder-white px-3 py-2 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-[#b3f300] focus:border-transparent",
                "placeholder": "Enter product description",
                "rows": 4
            }),
            "thumbnail": forms.URLInput(attrs={
                "class": "bg-gray-800 text-white placeholder-white px-3 py-2 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-[#b3f300] focus:border-transparent",
                "placeholder": "Enter thumbnail URL"
            }),
            "category": forms.Select(attrs={
                "class": "bg-gray-800 text-white px-3 py-2 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-[#b3f300] focus:border-transparent",
            }),
            "is_featured": forms.CheckboxInput(attrs={
                "class": "text-[#b3f300] focus:ring-[#b3f300] rounded"
            }),
            "size": forms.Select(attrs={
                "class": "bg-gray-800 text-white px-3 py-2 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-[#b3f300] focus:border-transparent",
            }),
            "stock": forms.NumberInput(attrs={
                "class": "bg-gray-800 text-white placeholder-white px-3 py-2 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-[#b3f300] focus:border-transparent",
                "placeholder": "Enter stock"
            }),
        }
```



**5. Jika belum ada product yang dibuat maka saya akan memunculkan `no-product.png` yang disimpan di `static/image` di root project**

**6. Menggunakan `card_product.html` dan `no-product.png` ke template `main.html`**
hal ini dilakukan supaya daftar produk yang muncul dapat dimanage secara modular di template terpisah dari `main.html`. lalu jika blm ada produk yang dibuat akan memunculkan gambar yang sudah ditentukan.
```
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>Garuda Store</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
<div class="bg-[#232323] w-full pt-16 min-h-screen">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">

    <!-- Header Section -->
    <div class="mb-8">
      <h1 class="text-4xl font-bold tracking-tight text-white">
        Your Football Merch Hub
      </h1>
      <p class="mt-2 text-lg text-white">
        Official collections, all in one place
      </p>
    </div>

    <!-- Filter Section -->
    <div class="flex flex-col text-white sm:flex-row sm:items-center sm:justify-between mb-8 bg-[#242424] rounded-lg p-0 ">
        <!-- Owner Filter -->
        <form method="GET" action="{% url 'main:show_main' %}" class="flex items-center space-x-2">
            <select 
              name="owner" 
              onchange="this.form.submit()" 
              class="border rounded px-2 py-1 text-sm bg-[#010101] text-white focus:bg-white focus:text-black"
            >
              <option value="all" {% if current_owner == "all" %}selected{% endif %}>All Products</option>
              <option value="my" {% if current_owner == "my" %}selected{% endif %}>My Products</option>
            </select>

            <!-- Category Filter -->
            <select 
              name="category" 
              onchange="this.form.submit()" 
              class="border rounded px-2 py-1 text-sm bg-[#010101] text-white focus:bg-white focus:text-black"
            >
              <option value="all" {% if current_category == "all" %}selected{% endif %}>All Categories</option>
              {% for key, value in categories %}
                <option value="{{ key }}" {% if current_category == key %}selected{% endif %}>{{ value }}</option>
              {% endfor %}
            </select>
        </form>
    </div>

    <!-- Product Grid -->
    {% if not products %}
      <div class="bg-[#010101] rounded-lg border border-gray-200 p-12 text-center">
        <div class="w-32 h-32 mx-auto mb-4">
          <img src="{% static 'image/no-product.png' %}" alt="No prodyct available" class="w-full h-full object-contain">
        </div>
        <h3 class="text-lg font-medium text-white mb-2">No product found</h3>
        <p class="text-white mb-6">Be the first to sell football merch to everyone.</p>
        <a href="{% url 'main:add_product' %}" class="inline-flex items-center px-4 py-2 bg-[#b3f300] text-black rounded-md hover:bg-[#b3f300] transition-colors">
          Add Product
        </a>
      </div>
    {% else %}
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {% for product in products %}
          {% include 'card_product.html' with product=product %}
        {% endfor %}
      </div>
    {% endif %}
  </div>
</div>
{% endblock content %}
```

**7. Styling halaman Detail Product**
Kurang lebih cara nya sama seperti styling halaman Detail News pada tutorial tapi disini saya melakukan penyesuaian agar atribut pada models bisa terlihat di bagian detail ini, seperti harga, size dan lain lain.
```
{% extends 'base.html' %}
{% load static %}
{% load humanize %}


{% block meta %}
<title>{{ product.name }} - Garuda Store</title>
{% endblock meta %}

{% block content %}
<div class="bg-[#232323] w-full min-h-screen">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        
        <!-- Back Navigation -->
        <div class="mb-6">
            <a href="{% url 'main:show_main' %}" class="text-[#b3f300] hover:text-[#bfd59f] font-medium text-2xl transition-colors">
                ← Back
            </a>
        </div>
        
        <!-- Product Card -->
        <article class="bg-[#010101] rounded-lg border border-gray-200 overflow-hidden shadow-md">
            
            <!-- Header -->
            <div class="p-6 sm:p-8">
                <!-- Category & Tags -->
                <div class="flex flex-wrap items-center gap-2 mb-4">
                    <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-[#bfd59f] text-green">
                        {{ product.category }}
                    </span>
                    {% if product.is_featured %}
                        <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-yellow-100 text-yellow-800">
                            Featured
                        </span>
                    {% endif %}
                    {% if product.is_product_hot %}
                        <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-red-100 text-red-800">
                            Hot
                        </span>
                    {% endif %}
                </div>

                <!-- Product Name -->
                <h1 class="text-3xl sm:text-4xl font-bold text-white leading-tight mb-2">
                    {{ product.name }}
                </h1>

                <!-- Meta Info -->
                <div class="flex flex-wrap items-center text-sm text-[#b3f300] gap-4 mb-4">
                    <time datetime="{{ product.created_at|date:'c' }}">
                        {{ product.created_at|date:"M j, Y g:i A" }}
                    </time>
                    <span>{{ product.product_views }} views</span>
                    {% if product.size %}
                        <span>Size: {{ product.size }}</span>
                    {% endif %}
                    <span>Stock: {{ product.stock }}</span>
                </div>
            </div>

            <div class="px-6 sm:px-8">
                <!-- Product Thumbnail -->
                {% if product.thumbnail %}
                    <img src="{{ product.thumbnail }}" 
                        alt="{{ product.name }}" 
                        class="w-full h-36  sm:h-80 lg:h-96 object-cover rounded-lg mb-4">
                {% endif %}
                <!-- Product Price -->
                <p class="text-3xl text-[#b3f300] font-semibold mb-0">
                    Rp{{ product.price|intcomma }}
                </p>
            </div>

            <!--  Product Description -->
            <div class="p-6 sm:p-8 pt-0">
                <div class="prose prose-lg max-w-none">
                    <div class="text-white leading-relaxed whitespace-pre-line text-base sm:text-lg">
                        <hr>
                        {{ product.description }}
                    </div>
                </div>
            </div>



            <!-- Seller Info -->
            <div class="border-t border-gray-200 p-6 sm:p-8 bg-gray-900">
                <div class="flex flex-wrap items-center justify-between gap-4">
                    <div>
                        <div class="font-medium text-[#b3f300]">
                            {% if product.user %}
                                Seller: {{ product.user.username }}
                            {% else %}
                                Seller: Anonymous
                            {% endif %}
                        </div>
                        <p class="text-sm text-gray-50">Seller</p>

                    </div>
                        <a href="{% url 'main:product_detail' product.id %}" 
                        class="inline-block  px-4 py-2 bg-[#b3f300] text-black rounded-md text-sm font-medium hover:bg-[#bfd59f] transition-colors">
                        Checkout
                        </a>
                </div>
            </div>

            <!-- Action Buttons (Optional) -->
            {% if user.is_authenticated and product.user == user %}
            <div class="border-t border-gray-200 p-6 sm:p-8 bg-[#010101] flex gap-3">
                <a href="{% url 'main:edit_product' product.pk %}" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded font-medium transition-colors">
                    Edit
                </a>
                <a href="{% url 'main:delete_product' product.pk %}" class="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded font-medium transition-colors">
                    Delete
                </a>
            </div>
            {% endif %}

        </article>
    </div>
</div>
{% endblock content %}
```

**8. Styling halaman Add Product**
Ubah berkas `add_product.html` pada subdirektori main/templates menjadi seperti berikut:
```
{% extends 'base.html' %}
{% block meta %}
<title>Add Product - Garuda Store</title>
{% endblock meta %}

{% block content %}
<div class="bg-[#232323] w-full min-h-screen">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    
    <!-- Back Navigation -->
    <div class="mb-6">
      <a href="{% url 'main:show_main' %}" class="text-[#b3f300] hover:text-[#bfd59f] font-medium text-2xl transition-colors">
        ← Back
      </a>
    </div>
    
    <!-- Form -->
    <div class="bg-[#010101] rounded-lg border border-gray-200 p-6 sm:p-8 form-style">
      <div class="mb-8">
        <h1 class="text-2xl font-bold text-white mb-2">Add New Product</h1>
        <p class="text-white">Sell your football merchandise to everyone</p>
      </div>
      
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div>
            <label for="{{ field.id_for_label }}" class="block text-sm font-medium text-white mb-2">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        
        <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-gray-200">
          <a href="{% url 'main:show_main' %}" class="order-2 sm:order-1 px-6 py-3 border border-gray-300 text-white rounded-md font-medium hover:bg-gray-500 transition-colors text-center">
            Cancel
          </a>
          <button type="submit" class="order-1 sm:order-2 flex-1 bg-[#b3f300] text-black px-6 py-3 rounded-md font-medium hover:bg-[#bfd59f] transition-colors">
            Upload Product
          </button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endblock %}
```

**9. Styling halaman Edit Product**
Ubah berkas `edit_product.html` pada subdirektori main/templates menjadi seperti berikut:
```
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>Edit Product - Garuda Store</title>
{% endblock meta %}

{% block content %}
<div class="bg-[#232323] w-full min-h-screen">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    
    <!-- Back Navigation -->
    <div class="mb-6">
      <a href="{% url 'main:show_main' %}" class="text-[#b3f300] hover:text-[#bfd59f] font-medium text-2xl transition-colors">
        ← Back
      </a>
    </div>
    
    <!-- Form -->
    <div class="bg-[#010101] rounded-lg border border-gray-200 p-6 sm:p-8 form-style">
      <div class="mb-8">
        <h1 class="text-2xl font-bold text-white mb-2">Garuda Store</h1>
        <p class="text-white">Update your football merchandise to everyone</p>
      </div>
      
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div>
            <label for="{{ field.id_for_label }}" class="block text-sm font-medium text-white mb-2">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-white0">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        
        <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-gray-200">
          <a href="{% url 'main:show_main' %}" class="order-2 sm:order-1 px-6 py-3 border border-gray-300 text-white rounded-md font-medium hover:bg-gray-500 transition-colors text-center">
            Cancel
          </a>
          <button type="submit" class="order-1 sm:order-2 flex-1 bg-[#b3f300] text-black px-6 py-3 rounded-md font-medium hover:bg-[#bfd59f] transition-colors">
            Update Product
          </button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endblock %}
```