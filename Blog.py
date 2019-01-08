# part 6 
# start a new app
$ python3.6 manage.py startapp blog

# add to 'INSTALLED_APPS' in setting.py
'blog',

# specify url path in urls.py
path('blog', include('blog.urls'))

# go to app>models.py
'''
# This models file like your entire database in your Django system
# because we are doing all database query part in here.but it's not with
# normal query language but with python classes


from django.db import models

class Post(models.Model):    # make a 'Post' table
    # define db table column name and its properties
    # column name = properties
    title=models.CharField(max_length=40)
    body=models.TextField()
    date=models.DateTimeField()

    def __str__(self):       # return title column value convert to string
        return self.title    # it's best when you want get title list


'''
# part 7 
# template/blog/blog.html for view
'''
{% extends "weed/header.html"%}

{% block content %}
    {% for p in object_list %}
        <h5> {{ p.date|date:"Y-m-d" }} <a href=
          "/blog/{{p.id}}">{{p.title}}</a> </h5>
    {% endfor %}

{% endblock %}

'''


# let's link template/blog/blog.html file with model.py database
'''
from django.conf.urls import url ,include
from django.views.generic import ListView , DetailView
from blog.models import Post


urlpatterns=[
    url(r'^$',ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                               template_name="blog/blog.html")),

]
'''


# part 8
# migrations
'''
# migrations create the real data base in sqlate data base
$ python3.6 manage.py makemigrations
# if you want to migrations for specific aplication
$ python3.6 manage.py makemigrations blog


# see app>blog>migrations/0001_initial.py
# to see what is "0001_initial.py" file's real sql query
$ python3.6 manage.py sqlmigrate blog 0001

# to check errors and finish all migrations process
$ python3.6 manage.py migrate

'''

# part 9
# admin
'''
first check the setting, is there have 'admin'app in the INSTALLED_APPS. if not the add.

# before you log the admin page you need to create superuser throught terminal 
$ python3.6 manage.py createsuperuser

# for do editing using admin pannel

from django.contrib import admin
from blog.models import Post     # import our model


admin.site.register(Post)        # register on admin page



'''

# part 9
# Individual blog pages



