from import_export import resources
from .models import add_student,add_course,add_teachers

class studentResource(resources.ModelResource):
    class meta:
        model= add_student

class courseResource(resources.ModelResource):
    class meta:
        model= add_course

class teacherResource(resources.ModelResource):
    class meta:
        model= add_teachers