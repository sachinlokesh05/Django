from app.models import Student
from django import forms
from app.models import Student


class Student_info(forms.ModelForm):
    class Meta:
        model =  Student
        fields = "__all__"