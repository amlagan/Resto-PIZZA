from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

def index(request):
    """

    pizzas_names_and_prices = [pizza.nom+": "+ str(pizza.prix) +" $ " for pizza in pizzas]
    pizzas_names_and_prices_str = ", ".join(pizzas_names_and_prices)
    return HttpResponse("Les pizzas  :" + pizzas_names_and_prices_str )

    :param request:
    :return:
    """
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, "menu/index.html", {"pizzas":pizzas })
