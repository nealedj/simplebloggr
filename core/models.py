import datetime
from django.utils.safestring import mark_safe
from google.appengine.ext import db

__author__ = 'davidne'

class ArticleModel(db.Model):
    title = db.StringProperty(required=True)
    body = db.StringProperty(required=True, multiline=True)
    created = db.DateTimeProperty()
    created_by = db.UserProperty()
    updated = db.DateTimeProperty()
    updated_by = db.UserProperty()

    def update(self, title, body, user):
        self.title = title
        self.body = body
        self.updated = datetime.datetime.utcnow()
        self.updated_by = user

    @staticmethod
    def create(title, body, user):
        now = datetime.datetime.utcnow()
        return ArticleModel(title=title, body=body,created=now,updated=now, created_by=user, updated_by=user)

    def to_safe_dict(self):
        return {
            'key' : str(self.key()),
            'title' : self.title,
            'body' : mark_safe(self.body),#todo: check out potentially dangerous scripting in body
            'created' : self.created,
            'created_by' : self.created_by,
            'updated' : self.updated,
            'updated_by' : self.updated_by
        }