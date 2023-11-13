# from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


def api_home(request, *args, **kwargs):
    print("GET: ", request.GET)
    print("HEADERS: ", request.headers)
    print("POST: ", request.POST)
    return JsonResponse({"xabar": "Tavba qil, birodar!"})


# def product_list(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=["id", "title"])
#         # data["title"] = model_data.title
#         # data["content"] = model_data.content
#         # data["price"] = model_data.price


#     return JsonResponse(data)
@api_view(["GET"])
def product_list(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
        return Response(data)
    return Response("Not found")
