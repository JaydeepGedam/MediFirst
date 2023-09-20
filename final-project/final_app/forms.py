from django import forms
from . models import Product, Admin_Register, Doctor_Register, User_Profile

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class Admin_Registation_Form(forms.ModelForm):
    class Meta:
        model = Admin_Register
        fields = "__all__"

class Doctor_Registation_Form(forms.ModelForm):
    class Meta:
        model = Doctor_Register
        fields = "__all__"

class User_Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = "__all__"