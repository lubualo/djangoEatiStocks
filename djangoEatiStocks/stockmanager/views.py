import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from .models import Investment, Stock
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from . import services
from . import forms


def index(request):
    return render(
        request,
        "stockmanager/index.html",
        {"investments": services.getInvestmentsWithCurrentPrice()},
    )


def add(request):
    if request.method == "POST":
        form = forms.AddStockForm(request.POST)
        if form.is_valid():
            investment = Investment.objects.create(
                date=datetime.date.today(),
                quantity=form.cleaned_data["quantity"],
                pricePerUnit=form.cleaned_data["price"] / form.cleaned_data["quantity"],
                stock=form.cleaned_data["stock"],
            )
            investment.save()
            return HttpResponseRedirect(reverse("stockmanager:index"))
        else:
            return render(request, "stockmanager/add.html", {"addForm": form})
    else:
        return render(
            request, "stockmanager/add.html", {"addForm": forms.AddStockForm()}
        )
