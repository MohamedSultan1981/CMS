from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django_filters.views import FilterView
from .filters import FACILITY_DATAFilter
urlpatterns = [
    #path('', FilterView.as_view(filterset_class=FACILITY_DATAFilter), name='search'),
    path('', views.FilteredFACILITY_DATAListView.as_view(), name='search'),
]
