from django.forms import ModelForm

from . import models

class CategoryForm(ModelForm):

    class Meta:
        model = models.Category
        fields = ('name', 'description',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
