from django import forms
from .models import Mart
from django.forms.widgets import SelectDateWidget,DateTimeBaseInput,SplitDateTimeWidget
from django.utils.timezone import datetime



class MartForm(forms.ModelForm):

    class Meta:
        model=Mart

        fields = ['title','price','image','offer','desc','important','datecompleted']

