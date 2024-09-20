# from django.shortcuts import render
# # Create your views here.
#
# def func_template(request):
#     return render(request, 'second_task/func_template.html')
#
# def class_template(request):
#     return render(request, 'second_task/class_template.html')

from django.shortcuts import render

def class_view(request):
    return render(request, 'second_task/class_template.html')

def function_view(request):
    return render(request, 'second_task/func_template.html')