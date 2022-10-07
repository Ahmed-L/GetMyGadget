from django.shortcuts import render, redirect
from .models import *
import operator
import random
from operator import itemgetter


def trend(request):
    name = []
    price = []
    link = []
    img = []
    objectList = []

    objectList.append(Web1())
    objectList.append(Web2())

    for o in objectList:
        n, p, l, i = o.fetch()
        name = name + n
        price = price + p
        link = link + l
        img = img + i

    price = list(map(int, price))
    zipped = zip(name, price, link, img)
    mylist = list(zipped)
    # suffles product list
    random.shuffle(mylist)

    # sorts product list on price
    # mylist = sorted(mylist, key=itemgetter(1))

    context = {
        'mylist': mylist,
    }

    return render(request, 'trend/trend.html', context)
