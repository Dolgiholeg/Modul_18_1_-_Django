# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('1/', views.func_template, name='func_template'),
#     path('2/', views.class_template, name='class_template'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('class/', views.class_view, name='class_view'),
    path('function/', views.function_view, name='function_view'),
]