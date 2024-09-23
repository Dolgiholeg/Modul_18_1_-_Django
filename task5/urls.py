from django.urls import path
from . import views
# from views import sign_up_by_django


urlpatterns = [
    path('', views.sign_up_by_html, name='sign_up_by_html'),
    # path('', views.sign_up_by_django, name='sign_up_by_django'),

]