
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import News
import datetime
from django.contrib.auth.decorators import login_required

class LatestNewsFeed(Feed):
    title = 'اخبار الصناعة'
    link = reverse_lazy('news:press-list')
    description = 'الاخبار الخاصة بالصناعة '
    def items(self):
        return News.published.all()[:5]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return truncatewords_html(item.newsscript, 30)
    def item_pubdate(self, item):
        return datetime.datetime(item.newsdate.year,item.newsdate.month,item.newsdate.day)
