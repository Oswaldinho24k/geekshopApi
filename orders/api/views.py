from ..models import Order
from .serializers import OrderSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import conekta
from django.conf import settings
from decimal import Decimal


class OrderList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            conekta.api_key = settings.CONEKTA_PRIVATE_KEY
            orderdj = serializer.data
            print(orderdj)
            #print(orderdj.total)
            amount = Decimal(orderdj['total'])
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
				    "name": "Mario Perez",
				    #"name": orderdj.cname,
				    "email": 'os@fixter.org',
				    #"phone": orderdj.tel
				    "phone": "7711732959"
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
			  #"charges": [{
			   #     "payment_method":{
			    #      "type": "card",
			     #     "token_id": request.POST.get('conektaTokenId'),
			      #  } 
			        
			  #}]
			  })
            orderstat = Order.objects.get(id=orderdj['id'])
            orderstat.pagado = True
            orderstat.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	


	
