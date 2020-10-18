from django.forms import ModelForm
from .views import Mem

class MemeForm(ModelForm):
    class Meta:
        model = Mem
        fields = ['title', 'tags', 'pic']
