from django.contrib import admin
from daterangefilter.filters import PastDateRangeFilter, FutureDateRangeFilter
from django.contrib import messages
from django.utils.translation import ngettext
# Register your models here.
from .models import News, NewsType, PaperType, NewsFile,Newsimages
from adminsortable2.admin import SortableAdminMixin

#Action Functions
class NewsimageAdmin(admin.TabularInline):
    model = Newsimages
class NewsFileAdmin(admin.TabularInline):
    model = NewsFile
    
@admin.register(News)
class newsAdmin(SortableAdminMixin,admin.ModelAdmin):
    inlines = [NewsimageAdmin,NewsFileAdmin]
    ordering = ['my_order']
    actions = ['make_published','make_draft','make_withdraw']
    search_fields = ['title__icontains']
    list_display = ['title','newstype','newsdate','status']
    list_filter = [('newsdate', PastDateRangeFilter),('created_at', PastDateRangeFilter),'papertype','newstype','status']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ("البيانات التعرفيه بالخبر", {
            'fields': [('title', "newsdate"),('slug','negative')],
            
        }),("مضمون و ملخض الخبر", {
            'fields': ["newsscript"],
            
        }),
        ('اماكن ظهور الخبر و الروابط', {
            'fields': [('papertype','newstype') ,"newsurl"]
            }),
            ('الوسائط المتعددة للخبر ', {
            'fields': ["newsvideo","newsembedvideo"]
            })
    )
    
    def make_published(self, request, queryset,):
        
        updated = queryset.update(status=News.STATUS_CHOICES.PUBLISHED)
       
        self.message_user(request, ngettext(
            '%d لقد تم نشر الخبر بنجاح.',
            '%d لقد تم نشر الاخبار بنجاح',
            updated,
        ) % updated, messages.SUCCESS)
    make_published.short_description = "نشر الخبر " 
    def make_draft(self, request, queryset,):
        updated = queryset.update(status=News.STATUS_CHOICES.DRAFT)
       
        self.message_user(request, ngettext(
            '%d لقد تم أعادة الخبر بنجاح.',
            '%d لقد تم أعادة الاخبار بنجاح',
            updated,
        ) % updated, messages.SUCCESS)
    make_draft.short_description = "أعادة الخبر للتعديل "  
    def make_withdraw(self, request, queryset,):
        updated = queryset.update(status=News.STATUS_CHOICES.WITHDRAW)
       
        self.message_user(request, ngettext(
            '%d لقد تم سحب الخبر بنجاح.',
            '%d لقد تم سحب الاخبار بنجاح',
            updated,
        ) % updated, messages.SUCCESS)
    make_withdraw.short_description = "سحب الخبر من النشر " 
    def get_actions(self, request):
        actions = super(newsAdmin, self).get_actions(request)
        if  not request.user.is_superuser:
            del actions['make_withdraw']
            del actions['make_draft']
        return actions

    #fields = [('title','negative',"slug"),  ('newstype', 'papertype'),"newsscript",'newsdate',("newsvideo","newsembedvideo")]
   
       
    

@admin.register(Newsimages)
class NewsimageAdmin(admin.ModelAdmin):
    pass
@admin.register(NewsFile)
class NewsFileAdmin(admin.ModelAdmin):
    pass   
admin.site.register(NewsType)
admin.site.register(PaperType)





