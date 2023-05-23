from django import forms
from .models import add_student,add_course,add_teachers

import re

class studentforms(forms.Form):
    class meta:
        model = add_student
        fields= '__all__'


class courseforms(forms.Form):
    class meta:
        model = add_course
        fields= '__all__'

class teacherforms(forms.Form):
    class meta:
        model = add_teachers
        fields= '__all__'