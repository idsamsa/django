from django.db import models
from django.db.models import CharField, DateTimeField, IntegerField, TextField,SlugField,ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField

LIST_STATE = (
    (0,'desable'),
    (1,'enable')
)

# Create your models here.
#--------------------------------------------------------------------------------------
#-------> Article Model
#-------------------------------------------------------------------------------------
class Article(models.Model):
    state = IntegerField(default=0, choices=LIST_STATE)
    title= CharField(max_length=120, blank=True, null=True, unique=True)
    slug = SlugField(max_length=120,db_index=True,unique=True,null=True, blank=True)
    description= TextField(null=True)
    picture = ImageField(null=True, upload_to="articles/", default="featured-lg.jpg")
    category = ForeignKey('Category',null=True, on_delete=models.SET_NULL)
    tags = ManyToManyField('Tag')
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    
    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="30px" height="30px" />'%(self.picture.url))
    image_tag.short_description = 'Image'
        
    def __str__(self) -> str:
        return self.title


#--------------------------------------------------------------------------------------
#-------> Category Model
#-------------------------------------------------------------------------------------
class Category(models.Model):
    name = CharField(max_length=20,null=False)
    state = IntegerField(default=0, choices=LIST_STATE)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True) 
    
    def __str__(self) -> str:
        return self.name

#--------------------------------------------------------------------------------------
#-------> Tag Model
#-------------------------------------------------------------------------------------    
class Tag(models.Model):
    name = CharField(max_length=20)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True) 
    
    def __str__(self) -> str:
        return self.name