from django.conf.urls import url


from . import views

app_name = 'polls'
#this is to call the view. We included polls.urls in mysite.urls
#Also, notice that urlpatterns is a list, so include commas
urlpatterns = [
    #The url() function is passed (regex, view, kwargs, name)
    #regex is required, it stands for regular expression, and matches patterns in strings
    #view is also required. Once the regex matches, the view is called
    #kwargs is optional. It stands for keyword arguments. They are passed in a dictionary to the target view
    #name is also optional. You can name a URL to refer to it later in django. It helps make global changes.
    #
    #The karet in the regex points to
    # ex /polls/
    url(r'^$', views.index, name='index'),
    # (?P<question_id>[0-9]+) gets question_id as string
    # ex /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name = 'detail'),
    #ex /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name = 'results'),
    #ex /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = 'vote'),

]