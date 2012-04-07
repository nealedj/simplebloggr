from django.conf.urls.defaults import *
from django.views.generic.base import TemplateView
from core import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), {}, name='core-home'),
    url(r'^article/(?P<key>[\d\w-]+)$', views.ArticleView.as_view(), {}, name='core-view'),
    url(r'^add$', views.AddArticleView.as_view(), {}, name='core-add'),
    url(r'^update/(?P<key>[\d\w-]+)$', views.UpdateArticleView.as_view(), {}, name='core-update'),
    url(r'^delete/(?P<key>[\d\w-]+)$', views.DeleteArticleView.as_view(), {}, name='core-delete'),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), {}, name='core-about'),
)
