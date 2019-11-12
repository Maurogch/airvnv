from django import forms


class FilterForm(forms.Form):
    city_id = forms.CharField(id="city_id")
    checkin_date = forms.DateField(id="checkin_date")
    checkout_date = forms.DateField(id="checkout_date")