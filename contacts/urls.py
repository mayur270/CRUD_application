from django.urls import path

from .views import home, create_view, update_view, delete_view

urlpatterns = [
    path('delete/(?P<uuid:pk>\d+)/', delete_view, name='delete_view'),
	path('update/(?P<uuid:pk>\d+)/', update_view, name='update_view'),
    path('create/', create_view, name='create_view'),
    path('', home, name='home'),
]
