from django.shortcuts import render, redirect, HttpResponse
from .models import *
import operator
import random
from operator import itemgetter


def search(request):
    if request.method == 'POST':
        search = request.POST['search']

        if search:
            mylist = makeList(search)
            mylist = sorted(mylist, key=itemgetter(1))
            context = {
                'mylist': mylist,
            }
            return render(request, 'search/search_products.html', context)
        else:
            return HttpResponse("BLANK")
    return render(request, 'search/search_bar.html')


def deep_index(mylist, n):
    return [y[0] for y in mylist].index(n)


def makeList(search):
    name = []
    price = []
    link = []
    img = []
    objectList = []

    objectList.append(Web1())
    objectList.append(Web2())
    objectList.append(Web3())
    objectList.append(Web4())
    # objectList.append(Web5())
    objectList.append(Web6())

    for o in objectList:
        o.addSearch(search)
        n, p, l, i = o.fetch()
        name = name + n
        price = price + p
        link = link + l
        img = img + i

    price = list(map(int, price))
    zipped = zip(name, price, link, img)
    mylist = list(zipped)

    newList = []
    searchList = search.split()
    for n, p, l, i in mylist:
        flag = 0
        for s in searchList:
            if s.lower() in n.lower():
                pass
            else:
                flag = 1
                break
        if flag == 0:
            index = deep_index(mylist, n)
            newList.append(mylist[index])

    return newList
