
__author__ = 'davidne'

class AppEngineUser(object):
    def __get__(self, request, obj_type=None):
        if not hasattr(request, '_cached_user'):
            from google.appengine.api import users
            request._cached_user = users.get_current_user()
        return request._cached_user


class GoogleAppEngineAuthenticationMiddleware(object):
    def process_request(self, request):
        assert hasattr(request, 'session'), "The Google App Engine authentication middleware requires session middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.sessions.middleware.SessionMiddleware'."
        request.__class__.user = AppEngineUser()
        return None