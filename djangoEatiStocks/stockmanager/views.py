import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from .models import Investment, Stock
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class AddStockForm(forms.Form):
    stock = forms.ModelChoiceField(
      label="Stock",
      queryset=Stock.objects.all(),
      required=True,
      widget=forms.Select(attrs={'class':'form-select'})
    )
    quantity = forms.FloatField(label="Quantity", required=True)
    price = forms.FloatField(label="Price", required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-addstockform'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))

def index(request):
  return render(
    request,
    "stockmanager/index.html",
    {"investments": Investment.objects.all()}
  )

def add(request):
  if request.method == "POST":
    form = AddStockForm(request.POST)
    if form.is_valid():
      try:
        investment = Investment.objects.create(  
          date=datetime.date.today(),
          quantity=form.cleaned_data["quantity"],
          pricePerUnit=form.cleaned_data["price"]/form.cleaned_data["quantity"],
          stock=form.cleaned_data["stock"]
        )
        investment.save()
        return HttpResponseRedirect(reverse("stockmanager:index"))
      except Stock.DoesNotExist:      
        return render(
          request,
          "stockmanager/add.html",
          {"addForm": AddStockForm()}
        )
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