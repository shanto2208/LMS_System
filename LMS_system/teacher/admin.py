from django.contrib import admin
from .models import lms_wieght
from import_export import resources
# Register your models here.

class lms_wieghtresources(resources.ModelResource):
    class meta:
        model = lms_wieght
        fields=('id','classid','asses_name','co_name','asses_point')
        export_order=('id','classid','asses_name','co_name','asses_point')
