
from django.contrib import admin
from django.urls import path, include
from routes.views import home, search_route, add_route, save_route, RouteListView, RouteDetailView,RoutesDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include(('cities.urls', 'cities'))),
    path('trains/', include(('trains.urls', 'trains'))),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('', home, name='home'),
    path('search_route/', search_route, name='search_route'),
    path('add_route/', add_route, name='add_route'),
    path('save_route/', save_route, name='save_route'),
    path('list/', RouteListView.as_view(), name='list'),
    path('detail/<int:pk>/', RouteDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', RoutesDeleteView.as_view(), name='delete'),
]
