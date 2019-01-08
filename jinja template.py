#**p3 jinja Templating

'''
jinja is a templating framework built with python.
we are using template to make some dynamic stuff on the server.
jinja template can render html source which is downloading to user.
'''

# brief steps to make new app (to more refer the intro.py)
'''
1.make a app (using terminal)
2.add that app on setting.py
3.link that app  on urls.py
4.app> make urls.py
                 > import views
                 > link views.py 's methods
5.app> make methos in views.py
6.app> create special name call 'templates' to store html files
       (it's better to make sub folder to not confuse with big file list )   

'''

# jinja have two different syntax to insert python code into html file
'''
logic eg:- python for loop
    {%for i in range(10)%} # sign to start 'for loop'
    
    {%endfor%}             # sign to end 'for loop'

variable eg:-
     {{i}}

combine eg:- to print 0-9 values on the html page
    {%for i in range(10)%} 
        <p> {{i}} </p>
    {%endfor%}             

'''

# web page = header+contant+footer
# let's make header-footer static to use any contant using jinja template

'''
<!--  1.make normal html file to header and footer
      2.select the point put the contant on the html file
      3.make following python jinja syntax on that point
          {%block contant%}


          {%endblock%}

eg:-       
-->
<!DOCTYPE html>

<html lang='en'>
<head>
    <title> Samadhi Django</title>
    <meta charset="utf-8"/>
</head>

<body>
  <h2> my frist django render </h2>

    <div>
       {%block contant%}

       {%endblock%}
    </div>

</body>

</html>
'''
# connect to header-footer static to contant html file
'''
{% extends "weed/header.html" %} <!-- link to header-footer -->
                                 <!-- *** this link can use in other apps too --> 
                                 <!-- this link relative to template folder -->
  {%block contant%}
  
  <!-- where you should put contant to render jinja template  -->

   <p> welcome to my website</p>


  {%endblock%}
  
'''




# include some html code to some html document
# 
'''
    {%block contant%}
     <!-- write what do you want include to -->
     <p> this is html include html file </p>


    {%endblock%}
'''
# includeing html code link to  on the html document
'''
  {% include "weed/includes/htmlsnippet.html" %}  <!-- put this code on html document where it should be -->
                                                  <!-- this link relative to template folder -->
'''




