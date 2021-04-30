from django.shortcuts import render
from django.http import JsonResponse
import json
from praw import Reddit
import datetime
from .models import Posts, PostClick

# Create your views here.
def home(request):
    if request.method == 'POST':
        print('\nPOST incoming!')

        # Get the data from client
        data = json.load(request).get('post_data')

        print('Incoming raw json:', data)
        print('Success\n')

        return JsonResponse({'some_data': 'Successful POST and response'})

    return render(request, 'home.html')


def fetch_signups(request):
    if request.method == "GET":
        reddit = Reddit(
            client_id="cmGaZGun0_QQOA",
            client_secret="_OBLXi15RFoFEvqXWJ7Zihvqv6bDjQ",
            password="V0ltair3$GEB",
            user_agent="practice project by vitruvian__man",
            username="vitruvian__man",
        )

        # Create a list of keywords to look for
        key_words = [
            'OnlyFans',
            'Only Fans',
            'Only fans',
            'Onlyfans',
            'only Fans',
            'onlyfans',
        ]

        # Get a list of top submissions for a particular subreddit if sub.title in keywords
        subs = [sub for sub in reddit.subreddit('signupsforpay').new(limit=1000)]

        # Loop over subs looking for a keyword
        subs_with_keyword = []
        subs_with_keyword_time = []
        for s in subs:
            for k in key_words:
                if k in s.title:
                    subs_with_keyword.append(s.title)
                    subs_with_keyword_time.append(datetime.datetime.fromtimestamp(s.created))
                    break
            continue

        print('Ajax requested registered!')

        return JsonResponse({
            "subData": subs_with_keyword,
            "status": "200"
        })


# Directory of leads home
def listings_home(request):
    # Query the list of items in the DB
    listings = Posts.objects.all()

    context = {}
    context['current_listings'] = listings

    return render(request, 'listings.html', context=context)


def listing_detail(request, pk):
    # Get the listing in question
    listing = Posts.objects.get(pk=pk)

    if request.method == 'POST':
        # Create a post click event and save to the database
        post_click_event = PostClick(title=listing.title, post=listing)
        post_click_event.save()

        print('\nClick registered!\n')

        return JsonResponse({"msg": "Click successfully recorded"})

    context = {}
    context['listing'] = listing

    return render(request, 'listing_detail.html', context)


def barry_home(request):
    return render(request, 'barry_home.html')