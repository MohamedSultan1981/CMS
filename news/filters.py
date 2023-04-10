from django.forms import widgets
from django.forms.widgets import Widget
import django_filters
from django_filters.widgets import RangeWidget

from .models import News,PaperType
from django import forms

class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains',label="عنوان الخبر",help_text="البحث بعنوان الخبر", widget=forms.TextInput(attrs={'class':'form-control'}))
    newsdate=django_filters.DateFromToRangeFilter(label="تاريخ نشر الخبر من الي",widget=RangeWidget(attrs={
                                                                            'class': ' datetimepicker-input col-lg-4 col-sm-12',
            'type':'date'    
                                                                            }))
    newsscript=django_filters.CharFilter(lookup_expr='icontains',label="الخبر",widget=forms.Textarea(attrs={'rows':2, 'cols':4}))
   
    papertype=django_filters.ModelMultipleChoiceFilter(queryset=PaperType.objects.all(),help_text="يمكنك اختيار أكثر من جريدة")
    negative=django_filters.BooleanFilter(widget=forms.CheckboxInput(attrs={'class':'form-check-input form-control col-lg-3 col-sm-12','type':'checkbox','style':'height:1.2em !important;'}),label='  سلبي/ايجابي    ')

    
    class Meta:
        model = News
        fields = ["title",'newsdate',"newstype","papertype","newsscript","negative",]
    
    def __init__(self, *args, **kwargs):
        super(NewsFilter, self).__init__(*args, **kwargs)
        # at sturtup user doen't push Submit button, and QueryDict (in data) is empty
        if self.data == {}:
            self.queryset = self.queryset.none()


      