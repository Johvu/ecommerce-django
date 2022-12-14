"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include

from cart import views

urlpatterns = [
    path('', views.cart),
    path('test', views.cart),
    path('add/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>', views.remove_from_cart, name='remove_from_cart'),
    path('remove_single_item/<int:product_id>', views.remove_single_item_from_cart, name='remove_single_item_from_cart'),

]
