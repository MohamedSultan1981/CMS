from django import forms
from django.forms.models import inlineformset_factory
from .models import News, NewsType, PaperType, NewsFile, Newsimages
from tinymce.widgets  import TinyMCE
from django.urls import reverse
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField
from django.core.files.base import ContentFile


class NewsFormModel(forms.ModelForm):
    class Meta:
        # fields = ('name', 'title', 'birth_date')
        # labels = {
        #     'name': _('Writer'),
        # }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }
        # field_classes = {
        #     'slug': MySlugFormField,
        # }
        
        # widgets={'name': Textarea(attrs={'cols': 80, 'rows': 20})})
        # localized_fields=('birth_date',))
        model = News
        fields = ["title","newstype","papertype","newsdate","newsscript","negative","newsurl","newsvideo","newsembedvideo"]
        
       

    title=forms.CharField(label='العنوان الرئيسى',widget=forms.TextInput(attrs={'class': 'form-control mr-sm-4 text-info h2','placeholder': 'ادخل العنوان هنا'}))
    
    newstype= forms.ModelChoiceField(label='اختر نوع الخبر',required=False, queryset=NewsType.objects.all(), empty_label='اختر نوع الخبر', widget=forms.Select(attrs={'class':'dropdown'}))
    papertype=forms.ModelMultipleChoiceField(label='اختر الجريدة',required=False, queryset=PaperType.objects.all(),widget=forms.SelectMultiple(attrs={'class':'dropdown'}))
    
    newsdate=forms.DateField(widget=forms.SelectDateWidget(years=range(2019, 2030)), label='تاريخ الخبر')
    newsscript=forms.CharField(widget=TinyMCE(attrs={'cols': 70, 'rows': 20}), label='ادخل الخبر')
    negative=forms.BooleanField(required=False, label='سلبى')
    newsurl=forms.URLField(label='ادخل رابط الخبر', required=False,widget=forms.TextInput(attrs={'class': 'form-control mr-sm-4'}))
    newsvideo=forms.FileField(required=False, label='ادخل الفيديو') 
    newsembedvideo=forms.CharField(label='ادخل رابط الفيديو', required=False, widget=forms.Textarea(attrs={'class': 'form-control mr-sm-4 ','placeholder': 'ادخل رابط الفيديو هنا','rows':5, 'cols':10})) 
    
    

class NewsFileFormModel(forms.ModelForm):
    
    class Meta:
        model = NewsFile
        fields = ["filename"]
        filename=forms.FileField(required=False, label="ادخل الملف")

# NewsFilesFormSet = inlineformset_factory( News, NewsFile,fields=['filename'],
#                                             form=NewsFileFormModel, extra=3)

class NewsImageFormModel(forms.ModelForm):
    
    class Meta:
        model = Newsimages
        fields = ["image"]
        filename=forms.ImageField(required=False, label="ادخل الصورة")

# NewsFilesFormSet = inlineformset_factory( News, Newsimages,fields=['image'],
#                                             form=NewsImageFormModel, extra=3)

class PressModelForm(forms.ModelForm):
    class Meta:
        model= News
        fields=["title","newsscript" ,"newstype", "papertype", "newsdate","newsvideo","newsurl","negative"]

    title=forms.CharField(label='العنوان الرئيسى',widget=forms.TextInput(attrs={'class': 'form-control mr-sm-9 text-info h2','placeholder': 'ادخل العنوان هنا'}))
    #newstype= forms.ModelChoiceField(label='اختر نوع الخبر',required=False, queryset=NewsType.objects.filter(id__lte=4), empty_label='اختر نوع الخبر', widget=forms.Select(attrs={'class':'dropdown'}))
    #papertype=forms.ModelChoiceField(label='اختر الجريدة',required=False, queryset=PaperType.objects.filter(id__lte=1), empty_label='اختر الجريدة', widget=forms.Select(attrs={'class':'dropdown'})) 
    papertype=forms.ModelMultipleChoiceField(label='اختر الجريدة',required=False, queryset=PaperType.objects.all(),widget=forms.SelectMultiple(attrs={'class':'dropdown  mr-sm-4 col-2'}))  
    newsdate=forms.DateField(widget=forms.SelectDateWidget(years=range(2019, 2030)), label='تاريخ الخبر')
    newsvideo=forms.FileField(required=False, label='ادخل الفيديو') 
    negative=forms.BooleanField(required=False, label='سلبى')
    newsurl=forms.URLField(label='ادخل رابط الخبر', required=False,widget=forms.TextInput(attrs={'class': 'form-control mr-sm-4'}))

    


