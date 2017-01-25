from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.losProductos.as_view(), name="products"), 
	#url(r'^detalle(?P<id>[-w]+)/$',views.elDetalle.as_view(), name="detalle" )
]