from django.shortcuts import render
from items.models import Item
from django.utils import timezone
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator

# Create your views here.


def general_search(request):
    # items = Item.objects.annotate(search=SearchVector('title', 'description', 'price', 'tag', 'published_date'),).filter(search=request.GET['q'])
    items = Item.objects.filter(title__icontains=request.GET['q'])
    return render(request, "index.html", {"items": items})


def user_item_search(request):
    items_user = Item.objects.filter(seller__icontains=request.user.username)
    paginator = Paginator(items_user, 4)
    page = request.GET.get('page', 1)
    items_user = paginator.page(page)
    return render(request, "index.html", {"items": items_user})


def user_bid_or_bought_search(request):
    items_bid_or_bought_user = Item.objects.filter(highest_bid_user__icontains=request.user.username)
    paginator = Paginator(items_bid_or_bought_user, 4)
    page = request.GET.get('page', 1)
    items_bid_or_bought_user = paginator.page(page)
    return render(request, "index.html", {"items": items_bid_or_bought_user})


def sort_sold(request):
    # items = Item.objects.annotate(search=SearchVector('title', 'description', 'price', 'tag', 'published_date'),).filter(search=request.GET['q'])
    items = Item.objects.filter(sold=1).order_by('-published_date')
    paginator = Paginator(items, 4)
    page = request.GET.get('page', 1)
    items = paginator.page(page)
    return render(request, "index.html", {"items": items})


def sort_new(request):
    # items = Item.objects.annotate(search=SearchVector('title', 'description', 'price', 'tag', 'published_date'),).filter(search=request.GET['q'])
    items = Item.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    paginator = Paginator(items, 4)
    page = request.GET.get('page', 1)
    items = paginator.page(page)
    return render(request, "index.html", {"items": items})


def sort_price(request):
    # items = Item.objects.annotate(search=SearchVector('title', 'description', 'price', 'tag', 'published_date'),).filter(search=request.GET['q'])
    items = Item.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-price')
    paginator = Paginator(items, 4)
    page = request.GET.get('page', 1)
    items = paginator.page(page)
    return render(request, "index.html", {"items": items})
