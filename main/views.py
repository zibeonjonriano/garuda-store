# main/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json

@login_required(login_url='/login')
def show_main(request):
    category_filter = request.GET.get("category", "all")  # kategori
    owner_filter = request.GET.get("owner", "all")        # all / my

    products = Product.objects.all()
    # Filter berdasarkan kategori
    if category_filter != "all":
        products = products.filter(category=category_filter)

    # Filter berdasarkan owner
    if owner_filter == "my":
        products = products.filter(user=request.user)

    context = {
        'app_name': "Garuda Store",
        'student_name': "Zibeon Jonriano Wisnumoerti",
        'class_name': "PBP D",
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'categories': Product.CATEGORY_CHOICES,  # semua kategori
        'current_category': category_filter,
        'current_owner': owner_filter
    }
    return render(request, "main.html", context)



# --- Data Delivery Views ---
def products_json(request):
    products = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in products
    ]

    return JsonResponse(data, safe=False)

def products_xml(request):
    products = Product.objects.all()
    data = serializers.serialize("xml", products)
    return HttpResponse(data, content_type="application/xml")

def product_json_by_id(request, id):
    try:
        product = Product.objects.select_related('user').get(pk=id)
        
        # Handle thumbnail safely - FIX HERE
        thumbnail_url = ''
        if product.thumbnail:
            # Check if it's already a string URL or ImageField
            if isinstance(product.thumbnail, str):
                thumbnail_url = product.thumbnail  # Already a URL string
            else:
                try:
                    thumbnail_url = request.build_absolute_uri(product.thumbnail.url)
                except (ValueError, AttributeError) as e:
                    thumbnail_url = ''
        
        # Check if 'description' field exists
        description = ''
        if hasattr(product, 'description'):
            description = product.description
        elif hasattr(product, 'content'):
            description = product.content
        else:
            print("⚠️ No description or content field found!")
        
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': description,
            'price': product.price,
            'category': product.category if hasattr(product, 'category') else 'unknown',
            'thumbnail': thumbnail_url,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        
        print(f"✅ Returning data: {data}")
        return JsonResponse(data)
        
    except Product.DoesNotExist:
        print(f"❌ Product {id} not found")
        return JsonResponse({'detail': 'Not found'}, status=404)
    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        print(f"❌ Exception occurred: {error_trace}")
        return JsonResponse({'error': str(e)}, status=500)
        
    except Product.DoesNotExist:
        print(f"❌ Product {id} not found")  # Debug
        return JsonResponse({'detail': 'Not found'}, status=404)
    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        print(f"❌ Exception occurred: {error_trace}")  # Debug
        return JsonResponse({'error': str(e)}, status=500)

def product_xml_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    data = serializers.serialize("xml", [product])
    return HttpResponse(data, content_type="application/xml")

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

@login_required(login_url='/login')
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()  #product.increment_views() digunakan untuk menambah jumlah views pada berita tersebut.

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

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

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

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

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


@csrf_exempt
@require_POST
@login_required(login_url='/login') # Tambahkan decorator login_required untuk keamanan
def add_product_entry_ajax(request):
    try:
        # Mengambil data dari request.POST (FormData dari frontend)
        name = strip_tags(request.POST.get("name"))
        price = request.POST.get("price")
        description = strip_tags(request.POST.get("description"))
        category = request.POST.get("category")
        thumbnail = request.POST.get("thumbnail")
        size = request.POST.get("size")
        stock = request.POST.get("stock")
        is_featured = request.POST.get("is_featured") == 'on'
        user = request.user
        
        # Validasi dasar
        if not name or not price:
             return JsonResponse({'success': False, 'message': 'Name and price are required.'}, status=400)

        # Membuat dan menyimpan Product
        new_product = Product.objects.create(
            name=name, 
            price=int(price), # Konversi ke integer
            description=description,
            category=category,
            thumbnail=thumbnail,
            size=size,
            stock=int(stock),  # Konversi ke integer
            is_featured=is_featured,
            user=user
        )
        
        #  KEMBALIKAN JSON RESPONSE (Wajib untuk AJAX) 
        return JsonResponse({
            'success': True,
            'message': f"Product '{new_product.name}' successfully added!", # Pesan untuk Toast
            'product_id': new_product.id
        }, status=201) 
        
    except Exception as e:
        # Penanganan error jika konversi int gagal atau error database
        return JsonResponse({'success': False, 'message': f"Failed to save product: {str(e)}"}, status=500)


@csrf_exempt
@require_POST
def login_ajax(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        # ... (Validasi input) ...
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # --- START PERBAIKAN AJAX COOKIE ---
            # 1. Buat HttpResponse sebagai dasar untuk JsonResponse
            response = JsonResponse({
                'success': True,
                'message': f'Welcome back, {user.username}!',
                'redirect_url': reverse("main:show_main") # Gunakan reverse() untuk konsistensi
            })
            
            # 2. Atur Cookie pada objek HttpResponse ini
            # Gunakan format waktu yang sama seperti di fungsi login_user konvensional
            response.set_cookie('last_login', str(datetime.datetime.now()))
            
            # 3. Kembalikan objek HttpResponse yang sudah membawa Cookie
            return response
            # --- END PERBAIKAN AJAX COOKIE ---
            
        else:
            return JsonResponse({
                'success': False,
                'message': 'Invalid username or password'
            }, status=401)
            
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)

# AJAX Register
@csrf_exempt
@require_POST
def register_ajax(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password1 = data.get('password1')
        password2 = data.get('password2')
        
        # Validasi input
        if not username or not password1 or not password2:
            return JsonResponse({
                'success': False,
                'message': 'All fields are required'
            }, status=400)
        
        if password1 != password2:
            return JsonResponse({
                'success': False,
                'message': 'Passwords do not match'
            }, status=400)
        
        # Cek username sudah ada atau belum
        from django.contrib.auth.models import User
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                'success': False,
                'message': 'Username already exists'
            }, status=400)
        
        # Validasi password menggunakan Django validators
        from django.contrib.auth.password_validation import validate_password
        from django.core.exceptions import ValidationError
        
        try:
            validate_password(password1)
        except ValidationError as e:
            return JsonResponse({
                'success': False,
                'message': ' '.join(e.messages)
            }, status=400)
        
        # Create user
        user = User.objects.create_user(
            username=username,
            password=password1
        )
        
        return JsonResponse({
            'success': True,
            'message': f'Account created successfully! Welcome, {username}!',
            'redirect_url': '/login'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)


@csrf_exempt
@require_POST
@login_required(login_url='/login')
def logout_ajax(request):
    logout(request)
    
    # Hapus cookie last_login di respons JSON
    response = JsonResponse({
        'success': True,
        'message': 'Logout successful!',
        'redirect_url': reverse('main:login')
    })
    response.delete_cookie('last_login')
    
    # Kembalikan JsonResponse yang sudah membawa instruksi hapus cookie
    return response 

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def delete_product_ajax(request, id):
    try:
        # 1. Cari produk dan pastikan user adalah pemilik
        product = get_object_or_404(Product, pk=id, user=request.user) 
        product_name = product.name
        
        # 2. Hapus produk
        product.delete()
        
        # 3. Kembalikan respons sukses JSON
        return JsonResponse({
            'success': True,
            'message': f"Product '{product_name}' deleted successfully!"
        }, status=200)
        
    except Product.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Product not found or unauthorized.'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'message': f"Error deleting product: {str(e)}"}, status=500)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def update_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id, user=request.user)
        # Gunakan request.POST (FormData)
        form = ProductForm(request.POST, instance=product) 
        
        if form.is_valid():
            form.save()
            return JsonResponse({
                'success': True,
                'message': f"Product '{product.name}' updated successfully!" # 🔥 TOAST MESSAGE 🔥
            }, status=200)
        else:
            errors = dict(form.errors.items()) # Ambil error spesifik
            return JsonResponse({'success': False, 
                                 'message': 'Validation Failed. Please check the form.',
                                 'errors': errors}, 
                                status=400)

    except Product.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Product not found or unauthorized.'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'message': f"Error updating product: {str(e)}"}, status=500)
