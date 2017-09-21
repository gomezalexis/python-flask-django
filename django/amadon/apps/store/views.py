# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    request.session['items'] = {
        "1": {'item_name': 'Dojo Tshirt', 'price': 19},
        '2': {'item_name': 'Dojo Sweater', 'price': 29},
        '3': {'item_name': 'Dojo Sweater', 'price': 4.95},
        '4': {'item_name': 'Algorithm Book', 'price': 49.99},
        '5': {'item_name': 'Dojo Chips', 'price': 1.25}
    }
    items_print = [
        {'product_id': 1, 'item_name': 'Dojo Tshirt', 'price': 19},
        {'product_id': 2, 'item_name': 'Dojo Sweater', 'price': 29},
        {'product_id': 3, 'item_name': 'Dojo Sweater', 'price': 4.95},
        {'product_id': 4, 'item_name': 'Algorithm Book', 'price': 49.99},
        {'product_id': 5, 'item_name': 'Dojo Chips', 'price': 1.25},
    ]
    
    return render(request, 'store/index.html',{'items_print':items_print})

def buy(request):
    if request.method == "POST":
        request.session['quantity'] = int(request.POST['quantity'])
        print request.session['items'][request.POST['item']]['price']
        request.session['total_money'] = request.session['quantity'] * request.session['items'][request.POST['item']]['price']
        request.session['item_name'] = request.session['items'][request.POST['item']]['item_name']
    return redirect(checkout)

def checkout(request):
    return render(request, 'store/checkout.html')

