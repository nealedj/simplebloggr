from django import forms

__author__ = 'davidne'

class AddEntryForm(forms.Form):
    title = forms.CharField(max_length=500, label='Title: ', widget=forms.TextInput(attrs={'class' : 'input_text'}))
    body = forms.CharField(label='Body: ', widget=forms.Textarea(attrs={'class' : 'input_text ckeditor'}))

class UpdateArticleForm(AddEntryForm):
    key = forms.CharField(label='Key', widget=forms.HiddenInput())