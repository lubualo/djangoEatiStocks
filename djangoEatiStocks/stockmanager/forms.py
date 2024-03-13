from django import forms
from .models import Stock
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout


class AddStockForm(forms.Form):
    stock = forms.ModelChoiceField(
        label="Stock",
        queryset=Stock.objects.all(),
        required=True,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    quantity = forms.FloatField(label="Quantity", required=True)
    price = forms.FloatField(label="Price", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-addstockform"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            "stock",
            "quantity",
            "price",
            Submit("submit", "Submit"),
        )
