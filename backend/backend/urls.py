"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
import backend.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # api
    url(r'^api/v1/categories/$', backend.views.category_collection),
    url(r'^api/v1/categories/(?P<pk>[0-9]+)$', backend.views.category_element),
    url(r'^api/v1/producttypes/$', backend.views.producttype_collection),
    url(r'^api/v1/producttypes/(?P<pk>[0-9]+)$', backend.views.producttype_element),
    url(r'^api/v1/producttypes/search/(?P<name>\w{1,30})$', backend.views.producttype_name),
    url(r'^api/v1/products/name/(?P<name>\w{1,30})$', backend.views.product_name),
    url(r'^api/v1/products/barcode/$', backend.views.product_barcode),
    url(r'^api/v1/products/(?P<pk>[0-9]+)$', backend.views.product_element),
    url(r'^api/v1/users/geo/', backend.views.user_radius),
    url(r'^api/v1/orders/$', backend.views.order_by_id),
    url(r'^api/create', backend.views.create_data),
    url(r'^api/v1/orders/deliver/(?P<order>[0-9]+)$', backend.views.deliver_order),
]
