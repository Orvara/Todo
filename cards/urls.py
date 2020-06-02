from django.urls import path
from .views import (
    HomeView,
    product_create_view
)

app_name = 'cards'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('todo', product_create_view, name='todo')

]
