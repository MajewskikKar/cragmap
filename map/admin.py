from django.contrib import admin
from .models import Crag, Site, Movie, Topo, Comment
from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields
from import_export.widgets import ManyToManyWidget



class SiteResources(resources.ModelResource):
    crags = fields.Field(attribute= 'crags', widget=ManyToManyWidget(Crag,field='nazwa'))
    class Meta:
        model = Site
        skip_unchanged = True
        import_id_fields = ('link',)
        exclude = ('id',)
        fields = ('strona','rodzaj_strony','tytul','polecane','data','link','crags')

def make_published(modeladmin, request, queryset):
    queryset.update(is_approved=True)

make_published.short_description = "Publikuj wybrane"

@admin.register(Crag)
class CragAdmin(ImportExportModelAdmin):
    pass

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

@admin.register(Topo)
class TopoAdmin(admin.ModelAdmin):
    pass

@admin.register(Site)
class SiteAdmin(ImportExportModelAdmin):
    resource_class = SiteResources
    list_display = ['strona', 'link', 'is_approved']
    list_editable = ['is_approved']
    actions = [make_published]



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
