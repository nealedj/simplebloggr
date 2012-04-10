
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic import TemplateView
from set_trace import set_trace
from django.views.generic.edit import FormView, DeleteView
from google.appengine.api import users
from google.appengine.ext.db import Key
from core.forms import AddEntryForm, UpdateArticleForm
from core.models import ArticleModel


class IndexView(TemplateView):
    template_name = "index.html"


class AddArticleView(FormView):
    template_name = "add-entry.html"
    form_class = AddEntryForm

    def form_valid(self, form):
        title = form.cleaned_data['title']
        body = form.cleaned_data['body']

        article = ArticleModel.create(title, body, self.request.user)
        self.key = article.put()

        return super(AddArticleView, self).form_valid(form)

    def get_success_url(self):
        return reverse('core-view', kwargs={'key':str(self.key)})

class UpdateArticleView(FormView):
    template_name = 'update.html'
    form_class = UpdateArticleForm

    def get_initial(self):
        key = self.kwargs.get('key')
        if not key: raise Http404

        self.key = Key(key)

        article = ArticleModel.get(self.key)
        if not article: raise Http404
        return article.to_safe_dict()

    def form_valid(self, form):
        title = form.cleaned_data['title']
        body = form.cleaned_data['body']
        key = form.cleaned_data['key']

        article = ArticleModel.get(Key(key))

        article.update(title, body, self.request.user)

        article.put()
        return super(UpdateArticleView, self).form_valid(form)

    def get_success_url(self):
        return reverse('core-view', kwargs={'key':str(self.key)})



class ArticleView(TemplateView):
    template_name = 'view-article.html'

    def get_context_data(self, **kwargs):
        key = kwargs.get('key')
        if not key: raise Http404

        article_key = Key(key)
        article = ArticleModel.get(article_key)
        if not article: raise Http404

        kwargs['article'] = article.to_safe_dict()
        return super(ArticleView, self).get_context_data(**kwargs)

class DeleteArticleView(DeleteView):
    http_method_names = ['post']
    def get_success_url(self):
        return reverse('core-home')

    def get_object(self, queryset=None):
        key = self.kwargs.get('key')
        if not key: raise Http404

        article = ArticleModel.get(Key(key))
        if not article: raise Http404

        return article

    def get(self, request, **kwargs):
        raise Http405
