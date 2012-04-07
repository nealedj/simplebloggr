from google.appengine.api import users, memcache
from core.models import ArticleModel

__author__ = 'davidne'

def user_urls(request):
    return {'user_urls' : {
        'signin' : users.create_login_url("/"),
        'signout' : users.create_logout_url("/"),
        }
    }

def recent_articles(request):
    memcache_key = 'recent_articles'
    ras = memcache.get(memcache_key)

    if ras is None:
        max_articles = 5
        cache_timeout = 5
        ras = ArticleModel.gql('ORDER BY created DESC').fetch(max_articles)
        memcache.add(memcache_key, ras, cache_timeout)

    return {
        'recent_articles' : [ra.to_safe_dict() for ra in ras]
    }