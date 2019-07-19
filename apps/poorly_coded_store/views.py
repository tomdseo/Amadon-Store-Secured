from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def calculate_checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(Product.objects.get(id=request.POST["price"]).price)
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    total_order_items = 0
    total_order_price = 0
    for order in Order.objects.all():
        total_order_items += order.quantity_ordered
        total_order_price += order.total_price

    request.session['quantity_from_form'] = str(quantity_from_form)
    request.session['total_charge'] = str(total_charge)
    request.session['total_order_items'] = str(total_order_items)
    request.session['total_order_price'] = str(total_order_price)

    return redirect("/checkout")

def checkout(request):
    return render(request, "store/checkout.html")