from re import X
from django.shortcuts import render, get_object_or_404, reverse
from .models import News, NewsFile , NewsType, Newsimages
from .forms import NewsFormModel, NewsFileFormModel, PressModelForm, NewsImageFormModel
from django.views.generic import (
CreateView,
DetailView,
ListView,
DeleteView,
UpdateView,
FormView
)
from  django.views.generic.detail import  SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from notifications.signals import notify
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage
from .filters import NewsFilter
from django_tables2.views import SingleTableView
from django_tables2.export.views import ExportMixin
from django_filters.views import FilterView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory,SuccessMessageMixin
#variables
page_size=8
# Create your views here.
class MyPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise

class NewsListView(LoginRequiredMixin,ListView):
    model=News
    paginate_by = page_size
    paginator_class = MyPaginator # We use our paginator class
    queryset = News.published
    def get_queryset(self):
      
        return super(NewsListView, self).get_queryset().filter(newstype_id=self.kwargs['type'])
        #queryset = News.objects.all()
        # if self.request.GET.get("browse"):
        #     selection = self.request.GET.get("browse")
        #     queryset = queryset.filter(newstype_id=selection)    
        # return queryset
        
class FileInline (InlineFormSetFactory):
    model = NewsFile
    fields = '__all__'
    form_class=NewsFileFormModel
    prefix = 'File'
    
    factory_kwargs = {'extra':1, 'max_num': 1000,
                      'can_order': False, 'can_delete': True,}

class ImageInline (InlineFormSetFactory):
    model = Newsimages
    fields = '__all__'
    form_class=NewsImageFormModel
    prefix = 'Image'
    
    factory_kwargs = {'extra':1, 'max_num': 1000,
                      'can_order': False, 'can_delete': True,}
    
class NewsDetailView(DetailView):
    model=News
class NewsCreateView(LoginRequiredMixin,CreateWithInlinesView,SuccessMessageMixin):
    model = News
    template_name = "News/news_create.html"
    form_class=NewsFormModel
    inlines = [FileInline,ImageInline]

    #context_object_name='news'
    

    
# # '''     form_classes={'create': NewsFormModel,
# #                     'pressCreate': PressModelForm,
# #                     }
# #    '''
#     def get_context_data(self, **kwargs):
#         data = super(NewsCreateView, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['files'] = NewsFilesFormSet(self.request.POST, self.request.FILES,instance=self.object,)
#         else:
#             data['files'] = NewsFilesFormSet(instance=self.object)
#         return data
#     def form_valid(self, form):
#         context = self.get_context_data()
#         files = context['files']

#         with transaction.atomic():
#             form.instance.created_by = self.request.user
#             form.instance.updated_by = self.request.user
#             self.object = form.save()

#             if files.is_valid():
#                 files.instance = self.object
#                 files.save()

#         return super(NewsCreateView, self).form_valid(form)
        
class PressCreateView(LoginRequiredMixin,CreateView):
    model = News
    template_name = "News/news_create.html"
    form_class= PressModelForm
    def get_context_data(self, **kwargs):
        data = super(PressCreateView, self).get_context_data(**kwargs)
        # if self.request.POST:
            # data['files'] = NewsFilesFormSet(self.request.POST, self.request.FILES,instance=self.object,)
        # else:
            # data['files'] = NewsFilesFormSet(instance=self.object)
        # return data
    def form_valid(self, form):
        context = self.get_context_data()
        files = context['files']

    queryset = News.objects.all() 
    

class PressListView(LoginRequiredMixin,ListView):
    model=News
    template_name="News/press_list.html"
    queryset=News.published.exclude(newstype__in= [5,6]).order_by('-newsdate')
    
    paginate_by = page_size
    paginator_class = MyPaginator # We use our paginator class

class PressUpdateView(LoginRequiredMixin,UpdateView):
    model = News
    template_name = "News/news_create.html"
    form_class= PressModelForm
class NewsUpdateView(LoginRequiredMixin,UpdateView):
    template_name="News/news_create.html"
    model = News
    form_class=NewsFormModel
class FilteredNewsListView(FilterView,ExportMixin,SingleTableView):
        model =News
        filterset_class = NewsFilter
        #context_object_name = 'users'  # Default: object_list
        paginate_by = 8


   

        
        




    
   

