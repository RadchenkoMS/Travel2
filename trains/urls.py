from django.urls import path
from trains.views import home, TrainsDetailView, TrainsCreateView, TrainsUpdateView, TrainsDeleteView, TrainsListView

urlpatterns = [
    #path('', home, name='home'),
    path('', TrainsListView.as_view(), name='home'),
    path('detail/<int:pk>/', TrainsDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', TrainsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TrainsDeleteView.as_view(), name='delete'),
    path('add/', TrainsCreateView.as_view(), name='create'),
]
