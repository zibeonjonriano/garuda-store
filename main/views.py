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
from django.http import HttpResponseRedirect
from django.urls import reverse

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



# --- Data Delivery Views ---
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