from django.shortcuts import render, get_object_or_404
from items.models import Item
from django.contrib import messages

# Create your views here.


def start_auction(request, pk):
    """
    start the auction
    """
    item = get_object_or_404(Item, pk=pk)
    if (request.POST.get('end-time-fix-form')):
        item.auction_end_time = request.POST.get('end-time-fix-form')
        item.auction_duration_time = request.POST.get('auction-time-form')
        item.highest_bid_offer = item.price
        item.auction_status = 1
        print(item.auction_end_time)
        print(item.auction_duration_time)
    elif request.POST.get('higher-bid-user'):
        if not request.POST.get('end-of-timer'):
            bid = int(request.POST.get('higher-bid'))
            item.highest_bid_offer = item.highest_bid_offer + bid
            item.highest_bid_user = request.POST.get('higher-bid-user')
            print(item.auction_end_time)
            print(item.auction_duration_time)
        else:
            messages.error(request, "Auction is finished. You cannot palce a bid any more!")
            print(int(request.POST.get('end-of-timer')))
            item.endtime = 1
    elif (request.POST.get('comments_seller')):
        item.comment_seller = request.POST.get('comments_seller')
    elif (request.POST.get('comments_buyer')):
        item.comment_winner = request.POST.get('comments_buyer')
    item.save()
    return render(request, "itemdetail.html", {'item': item})