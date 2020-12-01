from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.
def all_product(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,create= Order.objects.get_or_create(customer=customer,complete=False)
        cartitems=order.get_cart_total_items
    else:
        order={'get_cart_total_items':0,
        'get_cart_total_price':0
        }
    all_p=Product.objects.all()
    context={"product":all_p,'order':order,"cartitems":cartitems}
    return render(request,'essecommerceapp/all_product.html',context)
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,create= Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartitems=order.get_cart_total_items
    else:
        items=[]
        order={'get_cart_total_items':0,
        'get_cart_total_price':0
        }
    context={'order':order,"items":items,"cartitems":cartitems}
    return render(request,'essecommerceapp/cart.html',context)
def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,create= Order.objects.get_or_create(customer=customer,complete=False)
        item=order.orderitem_set.all()
    else:
        item=[]
        order={'get_cart_total_items':0,
        'get_cart_total_price':0
        }
    context={'order':order,"item":item}
    return render(request,'essecommerceapp/checkout.html',context)
import json
def updateItem(request):
    print('update')
    data=json.loads(request.body)
    productID=data['productID']
    action=data['action']
    customer=request.user.customer
    product=Product.objects.get(id=productID)
    print(product)
    order,created= Order.objects.get_or_create(customer=customer,complete=False)
    print(order)
    orderItem,created=Orderitem.objects.get_or_create(order=order,product=product)
    print(orderItem)
    if action=='add':
        orderItem.quantity={orderItem.quantity+1}
    elif action=='remove':
        orderItem.quantity={orderItem.quantity-1}
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse("added item",safe=False)
