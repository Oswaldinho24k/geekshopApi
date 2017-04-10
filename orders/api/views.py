from django.shortcuts import render
from rest_framework import viewsets
from ..models import Order, Quantity
from .serializers import OrderSerializer
from rest_framework.response import Response

from django.http import HttpResponse
from rest_framework.decorators import detail_route



class OrderViewSet(viewsets.ModelViewSet):

	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	@detail_route(methods=['post'])
	def pagar(self, request, *args, **kwargs):
		conekta.api_key = settings.CONEKTA_PRIVATE_KEY

		order_id=request.session.get('order_id')
		#orden de db de django
		order=get_object_or_404(Order,id=order_id)
		amount = order.total * 100
		
		
		#metodo para pago y orden en conekta
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
			    "name": order.cname,
			    "email": 'hola@mail.com',
			    "phone": "7712345678"
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
				

		messages.success(request, 'siiiiiiii')
		return HttpResponse('ya pagaste bro!!')

	