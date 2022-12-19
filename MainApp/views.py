import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponseNotFound

with open('MainApp/country.json', 'r') as f:
    countries_data = json.load(f)

def index(request):
    return render(request, 'MainApp/Gl.html')


def country(request):

    ListC=[]
    for a in range(len(countries_data)):
        ListC.append(countries_data[a]['country'])

    Alfavit = []
    for i in range(len(countries_data)):
        if countries_data[i]['country'][0] not in Alfavit:
            Alfavit.append(countries_data[i]['country'][0])
    object_list = ListC
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 10)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    Alfavit.sort()
    context={
        'ListC':ListC,
        'Alfavit':Alfavit,
        'page_obj': page_obj,
    }
    return render(request, 'MainApp/country.html', context=context)


def EveryCountry(request, EveryCountry):
    def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k
    for i in range(len(countries_data)):
        Peremennay = get_key(countries_data[i], EveryCountry)
        if Peremennay:
            context = {
                'country': countries_data[i]['country'],
                'languages': countries_data[i]['languages'],
            }
            return render(request, 'MainApp/EveryOne.html', context=context)
    return HttpResponseNotFound('Нет Ничего')


def EveryLang(request, EveryLang):
    LANG = []
    for i in range(len(countries_data)):
        if EveryLang in countries_data[i]['languages']:
            LANG.append(countries_data[i]['country'])

    for i in range(len(countries_data)):
            context = {
                'LANG': LANG,
                'languages': countries_data[i]['languages'],
                'country': countries_data[i]['country'],
                'l': EveryLang,
            }
            if EveryLang in countries_data[i]['languages']:
                return render(request, 'MainApp/EveryOneLang.html', context=context)
            else:
                continue
    return HttpResponseNotFound('Нет Ничего')


def lang(request):
    ListL=[]
    for a in range(len(countries_data)):
        for i in countries_data[a]['languages']:
            if i not in ListL:
                ListL.append(i)

    ListL.sort()
    context={
        'ListL':ListL,

    }
    return render(request, 'MainApp/lang.html', context=context)


def EveryBukva(request, Bukva):
    ListC=[]

    Alfavit = []
    for i in range(len(countries_data)):
        if countries_data[i]['country'][0] not in Alfavit:
            Alfavit.append(countries_data[i]['country'][0])

        if countries_data[i]['country'][0] == str(Bukva):
            ListC.append(countries_data[i]['country'])
    object_list = ListC
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 10)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    Alfavit.sort()
    context={
        'ListC':ListC,
        'Alfavit':Alfavit,
        'page_obj': page_obj,

    }
    return render(request, 'MainApp/country.html', context=context)

