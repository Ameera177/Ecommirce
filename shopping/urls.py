"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from phone import views
from Electrical_API import views as v1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('showElectricalTools/',views.showElectricalTools,name='showElectricalTools'),
    path('details/<int:id>/',views.details,name='details'),
    path('auth_login/',views.auth_login,name='auth_login'),
    path('auth_register/',views.auth_register,name='auth_register'),
    path('auth_login/',views.auth_login,name='auth_login'),
    path('auth_logout/',views.auth_logout,name='auth_logout'),
    path('checkout/',views.checkout,name='checkout'),
    path('add_to_cart/<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('API/itemlist/all/',v1.getallitems_list,name='itemall'),
    path('API/list_item_details/details',v1.list_item_details,name='details'),
    path('API/list_item_detailsbyid/details/<int:id>/',v1.list_item_detailsbyid,name='detailsbyid')
]
