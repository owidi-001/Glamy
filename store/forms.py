from django import forms

from store.models import Product, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=["name"]

class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=["name"]


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=["category","name","manufacturer","description","image","price","quantity"]

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=["quantity","price"]