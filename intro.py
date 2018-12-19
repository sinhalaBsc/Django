#**p1
# to install 'Django' using pip to your python version
 $ sudo python3.6 -m pip install Django

# make folder for project and go to that directory
# and start project name as 'mysite'
$ django-admin startproject mysite

# above cmd make two files in the project folder  1.mysite 2.manage.py
'''
1.mysite
   i  .init     - we are not going to touch this file
   ii .settings -  INSTALLED_APP / secret key 
   iii.urls     -  main controller point
   iv .wsgi     - 
2.manage.py - this is our command line file

'''

# enter the project file whare have 'manage.py'
$ cd mysite

# to run linux/mac
$ python3.6 manage.py runserver
# if windows
> C:/Python35/python manage.py runserver

# open browser and go localhost link given by terminal http://127.0.0.1:8000/

# to brack the server
# $ ctr+c

#**p2

# to start new app name as 'webapp'
$ python3.6 manage.py startapp webapp
# this cmd make folder as you named insied the project floder (start Django>mysite folder)
'''
eg:-
 webapp
     admin.py   -for administration stuff
     apps.py    -will never be edited
     __init.py  -treated as its own app
     migrations 
     models.py  - contain database information as just some simple metadata
     tests.py   -for testing purpose your codes
     views.py   -what the users sees Django is a Model View controller eg URL 
'''

# we have to add our created app('webapp') to $ mysite>settings -  INSTALLED_APP list
'''
eg:-
    INSTALLED_APPS = [
        'webapp',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
 
'''
# now we have to create new url to this app
# for this go to $ mysite>url

'''
# and import the include 
from django.urls import path, include

eg:-
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('webapp/', include('webapp.urls')),
    ]
    # when getting url-'webapp/' then it's direct to > "include('webapp.urls')"
'''

# ?? creted Django/mysite/mysite/__pycache__
# ?? creted Django/mysite/db.sqlite3

# to make view to user go to Django/mysite/webapp/ and open view.py
'''
# we are not going to use render
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h2>HEY</h2>")


'''

# to controll that view to show .. go to Django/mysite/webapp/ and make urls.py
# then specify url pattern
from django.conf.urls import url
# from period import views to import current package
from . import views
'''
#eg:-
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index')]
    #url(r'^$',views.index,name='just name')]

'''


# then run the server
$ python3.6 manage.py runserver
# in http://127.0.0.1:8000/ you will see 404 error
# then go to the http://127.0.0.1:8000/webapp/ it's will works !!!!


#**p2 jinja Templating
# jinja is a templating framework built with python






