from django.contrib import admin

from .models import Article, Category, Tag

# Register your models here.
#--------------------------------------------------------------------------------------
#-------> ArticleAdmine Model
#-------------------------------------------------------------------------------------
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('image_tag',"title", "slug", "state","category", "created",)
    list_filter = ("state", "category",)
    prepopulated_fields = {"slug":("title",)}
    


#--------------------------------------------------------------------------------------
#-------> REGISTER Model
#-------------------------------------------------------------------------------------
admin.site.register(Article,ArticleAdmin)

admin.site.register([Category,Tag])