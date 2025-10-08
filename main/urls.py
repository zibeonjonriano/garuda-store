# main/urls.py
from django.urls import path
from main.views import (
    show_main, products_json, products_xml, product_json_by_id, 
    product_xml_by_id, product_detail, add_product, register, 
    login_user, logout_user, edit_product, delete_product, 
    add_product_entry_ajax, login_ajax, register_ajax  # Import baru
)
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),  # "/" → fungsi show_main di views.py
    path("products/json/", products_json, name="products_json"),
    path("products/xml/", products_xml, name="products_xml"),
    path('products/json/<int:id>/', product_json_by_id, name='product_json_by_id'),
    path("products/xml/<int:id>/", product_xml_by_id, name="product_xml_by_id"),
    path("products/<int:id>/", product_detail, name="product_detail"),
    path("products/add/", add_product, name="add_product"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('products/<int:id>/edit', edit_product, name='edit_product'),
    path('products/<int:id>/delete', delete_product, name='delete_product'),
    path('create-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    
    # AJAX Auth endpoints - TAMBAHKAN INI
    path('auth/login/', login_ajax, name='login_ajax'),
    path('auth/register/', register_ajax, name='register_ajax'),

] 
