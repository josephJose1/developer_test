from django import forms
from task4.models import Salon, Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
                
                'reserva_salon',
                'start',
                'end',
                # 'state',
                'user',
                'description',
                ]
        widgets = {
            "reserva_salon":forms.SelectMultiple(attrs={"class":"form-control"}),
            "start": forms.DateTimeInput(attrs={"type":"datetime-local", }),
            "end": forms.DateTimeInput(attrs={"type":"datetime-local"}),
            "user":forms.SelectMultiple(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"cols": 30, "rows": 5})
        }