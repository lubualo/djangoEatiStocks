from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

stocks = ["AAPL", "BA", "TSLA"]

class AddStockForm(forms.Form):
    ticker = forms.CharField(label="Ticker", max_length=4)
    quantity = forms.FloatField(label="Quantity")
    price = forms.FloatField(label="Price")

def index(request):
  return render(
    request,
    "stockmanager/index.html",
    {"stocks": stocks}
  )

def add(request):
  if request.method == "POST":
    form = AddStockForm(request.POST)
    if form.is_valid():
      ticker = form.cleaned_data["ticker"]
      stocks.append(ticker)
      return HttpResponseRedirect(reverse("stockmanager:index"))
    else:
      return render(
        request,
        "stockmanager/add.html",
        {"addForm": form}
      )
  else:
    form = AddStockForm()
    return render(
      request,
      "stockmanager/add.html",
      {"addForm": form}
    )