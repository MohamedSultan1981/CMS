from .feeds import LatestNewsFeed
from django.views.generic.base import TemplateView
from django.urls import path
from .views import (NewsListView,
NewsDetailView,
NewsCreateView,
NewsUpdateView,
PressCreateView,
PressListView,
PressUpdateView,
FilteredNewsListView,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
app_name='news'
urlpatterns = [
    path('', TemplateView.as_view(template_name='news/index.html'), name="index"),
    #path('',PressListView.as_view(), name="index"),
    path('presslist',PressListView.as_view(),name="press-list"),
    path('list/<int:type>',NewsListView.as_view(), name="news-list" ),
    path('create', NewsCreateView.as_view(), name="news-create"),
    path('presscreate', PressCreateView.as_view(), name="press-create"), 
    path('pressupdate',PressUpdateView.as_view(), name="press-update"),
     path('search', FilteredNewsListView.as_view(), name='search'),
     
    path('<int:year>/<int:month>/<int:day>/<str:slug>/',NewsDetailView.as_view(), name="news-detail"),
    #path('<int:pk>',NewsDetailView.as_view(), name="news-detail"),
    #path('<str:slug>', NewsUpdateView.as_view(), name="news-update"),
   path('feed', LatestNewsFeed(), name='News_feed'),
   
    
    #path('<int:id>/delete',product_delete_view, name="news-delete"),
  
]