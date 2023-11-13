# from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "title"


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def api_home(request, *args, **kwargs):
    return JsonResponse({"xabar": "DRF is interesting."})


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


@api_view(["POST"])
def add_product(request, *args, **kwargs):
    print(request.data)
    data = request.data

    title = data["title"]
    content = data["content"]
    price = data["price"]

    Product.objects.create(title=title, content=content, price=price)

    return Response({"xabar": "Mahsulot qo'shildi"})
