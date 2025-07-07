import json
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cloth, Quote


def home(request):
    cloths = Cloth.objects.all()
    return render(request, "store/home.html", {"cloths": cloths})


def cloth_detail(request, pk):
    cloth = get_object_or_404(Cloth, pk=pk)
    return render(request, "store/cloth_detail.html", {"cloth": cloth})


def add_to_cart(request, cloth_id):
    cloth = get_object_or_404(Cloth, pk=cloth_id)
    qty = float(request.POST.get("quantity", 0))
    cart = request.session.get("cart", {})
    cart[str(cloth_id)] = cart.get(str(cloth_id), 0) + qty
    request.session["cart"] = cart
    return redirect("cart_detail")


def cart_detail(request):
    cart = request.session.get("cart", {})
    items = []
    total = 0
    for cid, qty in cart.items():
        cloth = Cloth.objects.get(pk=int(cid))
        items.append({"cloth": cloth, "qty": qty})
        total += cloth.price * qty
    return render(request, "store/cart.html", {"items": items, "total": total})


def send_quote(request):
    cart = request.session.get("cart", {})
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        items_list = []
        for cid, qty in cart.items():
            cloth = Cloth.objects.get(pk=int(cid))
            items_list.append({"cloth": cloth.name, "quantity": qty})
        Quote.objects.create(
            customer_name=name,
            customer_email=email,
            items=json.dumps(items_list),
        )
        request.session["cart"] = {}
        return render(request, "store/quote_sent.html")
    return render(request, "store/quote_form.html")
