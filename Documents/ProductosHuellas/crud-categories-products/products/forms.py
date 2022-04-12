from django.forms import ModelForm

from . import models

class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = (
            'name',
            'description',
            'price',
            'available',
            'category',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    