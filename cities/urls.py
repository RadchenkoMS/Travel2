from django.urls import path
from cities.views import home, CitiesDetailView, CitiesCreateView, CitiesUpdateView, CitiesDeleteView, CitiesListView

urlpatterns = [
    #path('', home, name='home'),
    path('', CitiesListView.as_view(), name='home'),
    path('detail/<int:pk>/', CitiesDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', CitiesUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CitiesDeleteView.as_view(), name='delete'),
    path('add/', CitiesCreateView.as_view(), name='create'),
]
