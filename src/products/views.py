from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from .models import Product


def product_create_view(request):
    initial_data = {'title': 'Big Title', 'description':'Sirf yagnesh ki hi baten'}
    obj = Product.objects.get(id=3)
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)

    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # obj = Product.object.get(id=1)
    context = {
        "object": obj,
        # "title": obj.title
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)
