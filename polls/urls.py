from django.conf.urls import url


from . import views
#this is to call the view. Now we need to point the mysite urls to the polls urls
urlpatterns = [
    #The url() function is passed (regex, view, kwargs, name)
    #regex is required, it stands for regular expression, and matches patterns in strings
    #view is also required. Once the regex matches, the view is called
    #kwargs is optional. It stands for keyword arguments. They are passed in a dictionary to the target view
    #name is also optional. You can name a URL to refer to it later in django. It helps make global changes.
    url(r'^$', views.index, name='index'),
]