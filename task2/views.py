from  django.views.generic import TemplateView
from django.shortcuts import render

class class_view(TemplateView):
    template_name = 'second_task/class_template.html'

def function_view(request):
    return render(request, 'second_task/func_template.html')