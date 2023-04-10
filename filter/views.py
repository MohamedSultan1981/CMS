from django.shortcuts import render
from django.views import View
from django.conf import settings
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2.views import SingleTableView
from django_tables2.export.views import ExportMixin
from django_filters.views import FilterView
from .models import FACILITY_DATA
from .filters import FACILITY_DATAFilter
class HomeView(LoginRequiredMixin,View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }
        return render(request, 'home/index.html', context)
class FilteredFACILITY_DATAListView(FilterView,ExportMixin,SingleTableView):
        model =FACILITY_DATA
        filterset_class = FACILITY_DATAFilter
        #context_object_name = 'users'  # Default: object_list
        paginate_by = 200
        """ def get_queryset(self):
            queryset = super().get_queryset()
            return FACILITY_DATAFilter(self.request.GET, queryset=queryset).qs  """
           
      