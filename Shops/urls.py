from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('',views.Home,name='home'),
   path('shop/',views.Shops,name='shop'),
   path('products/<slug:slug>/', views.product, name='products'),
   path('admin/',admin.site.urls,name='admin'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)