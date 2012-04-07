
__author__ = 'davidne'
from django import template

register = template.Library()

@register.inclusion_tag('include/article.html')
def render_article(article):
    return article
