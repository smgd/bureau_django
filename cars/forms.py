from django import forms

from cars.models import Car


class DateInput(forms.DateInput):
    input_type = 'date'


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['vin', 'creation_date', 'disposal_date', 'passport']
        widgets = {
            'disposal_date': DateInput(),
            'creation_date': DateInput()
        }


class PeriodForm(forms.Form):
    start_of_period = forms.DateField(widget=DateInput())
    end_of_period = forms.DateField(widget=DateInput())