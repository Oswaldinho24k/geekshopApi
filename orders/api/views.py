from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from ..models import Order, Quantity
from .serializers import OrderSerializer
from rest_framework.response import Response
from django.conf import settings

from django.http import HttpResponse
from rest_framework.decorators import detail_route
import conekta



class OrderViewSet(viewsets.ModelViewSet):

	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	@detail_route(methods=['get'], 
		serializer_class=OrderSerializer,)
	def content(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	@detail_route(methods=['post'])
	def pagar(self, request, *args, **kwargs):
		conekta.api_key = settings.CONEKTA_PRIVATE_KEY
		
		#orden de db de django
		orderdj = self.get_object()
		
		print(orderdj)
		print(orderdj.total)
		amount = orderdj.total * 100

		order = conekta.Order.create({
		    "line_items": [{
		        "name": "Compra total",
		        "unit_price": int(amount),
		        "quantity": 1
		   	}],
		    "shipping_lines": [{
		        #"amount": 1500,
		        "amount": 0,
		        "carrier": "mi compañia"
		    }],
		    "currency": "MXN",
		    "customer_info": {			    
			    #"name": "Mario Perez",
			    "name": orderdj.cname,
			    "email": 'os@fixter.org',
			    "phone": orderdj.tel
			  },
		    "shipping_contact":{
		     "phone": "5555555555",
		     "receiver": "Bruce Wayne",
		     "address": {
		       "street1": "Calle 123 int 2 Col. Chida",
		       "city": "Cuahutemoc",
		       "state": "Ciudad de Mexico",
		       "country": "MX",
		       "postal_code": "06100",
		       "residential": True
		     }
		   },
		  "charges": [{
		        "payment_method":{
		          "type": "card",
		          "token_id": request.POST.get('conektaTokenId'),
		        } 
		        
		  }]
		})
		

				

		#messages.success(request, 'siiiiiiii')
		orderdj.pagado=True
		orderdj.save()

		return HttpResponse('ya pagaste bro!!')

	