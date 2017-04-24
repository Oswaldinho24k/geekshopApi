from django.conf.urls import url, include
from rest_framework import routers
from . import views


#router = routers.DefaultRouter()

#router.register(r'orders', views.OrderViewSet)



urlpatterns = [
	url(r'^orders/$', views.OrderList.as_view())
 #   url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]