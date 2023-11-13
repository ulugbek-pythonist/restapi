from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_home),
    path("products/", views.product_list),
    path("products/add/", views.ProductCreateAPIView.as_view()),
    path("products/<int:pk>/", views.ProductDetailView.as_view()),
    path("products/<str:title>/update/", views.ProductUpdateAPIView.as_view()),
    path("products/<int:pk>/delete/", views.ProductDestroyAPIView.as_view()),
    path("products-list/", views.ProductListCreateAPIView.as_view()),
]
