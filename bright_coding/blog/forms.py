# from django.db.models.fields import 
from django.forms import ModelForm
from django.forms.widgets import Select, SelectMultiple, TextInput, Textarea
from .models import Article
           
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = ['state']
        # fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class':'form-control'}),
            'category': Select(attrs={'class':'form-control'}),
            'tags': SelectMultiple(attrs={'class':'form-control'})
        }
