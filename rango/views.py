from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Page
from .forms import CategoryForm, PageForm


def index(request):
    context = {
        'categories': Category.objects.order_by('-likes')[:5],
        'pages': Page.objects.order_by('-views')[:5],
    }

    return render(request, 'index.html', context)


def about(request):
    context = {'boldmessage': 'This tutorial has been put together by Andrey'}
    return render(request, 'about.html', context)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['category'] = category
        context_dict['pages'] = pages
    except:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'category.html', context_dict)


def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context = {'form': form, 'category': category}
    return render(request, 'add_page.html', context)
