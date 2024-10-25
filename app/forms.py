from django import forms
from .models import *

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'cover_image']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'cover_image', 'price']

class AdditionalProjectImageForm(forms.ModelForm):
    image = MultipleFileField(label='Select files', required=False)
    class Meta:
        model = AdditionalProjectImage
        fields = ['image']
        widgets = {
            # 'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }

class AdditionalProductImageForm(forms.ModelForm):
    pimage = MultipleFileField(label='Select files', required=False)
    class Meta:
        model = AdditionalProductImage
        fields = ['pimage']
        widgets = {
            # 'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }

# class ProjectForm(forms.ModelForm):
#     additional_images = MultipleFileField(label='Select files', required=False)
    
#     class Meta:
#         model = Project
#         fields = ['title', 'description', 'cover_image', 'additional_images']
#         widgets = {
#             'description': forms.Textarea(attrs={'placeholder': 'Enter a detailed description'}),
#         }

class ProductForm(forms.ModelForm):
    additional_images = MultipleFileField(label='Select files', required=False)
     
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'cover_image', 'additional_images']
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Enter a detailed description'}),
        }