
# get Bootstrp and link to django
'''
go to follwing link
https://getbootstrap.com/
and hit download and extrac

app>>
    make new diractory name 'static' (special name)
    and move to bootstrap files (css+js+font)
and check at bottom of 'setting.py' file is there already
linked to all static files.if there not link as following code    
'''
STATIC_URL = '/static/'

# link css to html file
'''
#go to header-footer html file

<head>
    <title> Samadhi Django</title>
    <meta charset="utf-8"/>
    {% load staticfiles%}
    <!--  <link rel='stylesheet' href='/static/css/bootstrap.min.css' type='text/css' />  
    -->
      <link rel='stylesheet' href={% static 'bootstrap.min.css' %} type='text/css' />
  
</head>

'''

# *remaind if you are linking using jinjor-python
''' you should add "{% load staticfiles%}" to anywere in html file. include.html or header.html
    will not share on every page.
      {% load staticfiles%}
      <link rel='stylesheet' href={% static 'bootstrap.min.css' %} type='text/css' />

'''

# now you can add Bootstrap example on your html page..
# enjoy!!
