from django import forms
from .models import Doctor, Patient

class DoctorUpdateForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ['name', 'category', 'details', 'visitingHour', 'visitingDates', 'dailyoccupation']
class PatientUpdateForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['name', 'dob', 'phone', 'appointment']

class CategoryForm(forms.Form):
    name = forms.CharField(label='Please, select a category!',widget=forms.Select(choices=(('Obstetricians and gynecologists', 'Obstetricians and gynecologists'), ('Psychiatrists', 'Psychiatrists'), ('Neurologists', 'Neurologists'), ('Cardiologists', 'Cardiologists'), ('All', 'All'))))
