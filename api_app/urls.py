from django.urls import path
from.views import GetAllProductView, get_all_product, GetProductCategoryView, ProductDetail, GetAllProductView, AllProductCreateView,ProductDetail2, DeleteProduct, AllProductView




urlpatterns=[
    path('products/', GetAllProductView.as_view()),
    path('products/<str:category>/', GetProductCategoryView.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('allproducts/', GetAllProductView.as_view()),
    path('all_products/', AllProductCreateView.as_view()),
    path('single_product/<int:pk>/', ProductDetail2.as_view()),
    path('deleteproduct/<int:pk>/', DeleteProduct.as_view()),
    path('productview/', AllProductView.as_view()),
    # path('product/', second_api_view),
    path('all_product/', get_all_product),

]