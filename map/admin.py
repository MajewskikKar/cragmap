from django.contrib import admin
from .models import Crag
from .models import Site
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Crag, ImportExportModelAdmin)
admin.site.register(Site)
