"""geekshopAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from products import urls as productUrls
from products.api import urls as productApiUrls
from orders.api import urls as orderApiUrls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
       regex=r'^media/(?P<path>.*)$',
       view=serve,
       kwargs={'document_root':settings.MEDIA_ROOT}),
    url(r'^products/', include(productUrls, namespace="products")),
    url(r'^products/api/', include(productApiUrls, namespace="productapi")), 
    url(r'^orders/api/', include(orderApiUrls, namespace="orderapi")), 
    ]
