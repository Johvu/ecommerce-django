from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.generic import DetailView

from .models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'webshop/product_detail.html'

def index(request):
    products = Product.objects.all()

    paginator = Paginator(products, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_total = paginator.num_pages
    return render(request, 'webshop/index.html',
                  {'page_obj': page_obj, 'page_number': page_number, 'page_total': page_total})


def search_results(request):
    if request.method == 'POST':
        search_text = request.POST['searched']
        products = Product.objects.filter(name__icontains=search_text)
        paginator = Paginator(products, 8)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        page_total = paginator.num_pages

        return render(request, 'webshop/search_results.html',
                      {'page_obj': page_obj, 'search_text': search_text, 'page_number': page_number,
                       'page_total': page_total})
