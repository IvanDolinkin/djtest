from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort', '')
    all_phones = Phone.objects.all()
    if sort_pages == 'max_price':
        phones = all_phones.order_by('-price')
        context = {'phones': phones}
        return render(request, template, context)
    elif sort_pages == 'min_price':
        phones = all_phones.order_by('price')
        context = {'phones': phones}
        return render(request, template, context)
    elif sort_pages == 'name':
        phones = all_phones.order_by('name')
        context = {'phones': phones}
        return render(request, template, context)
    else:
        context = {'phones': all_phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)    # Unresolved attribute reference 'objects' for class 'Phone'. Почему так?
    context = {'phone': phone}
    return render(request, template, context)
