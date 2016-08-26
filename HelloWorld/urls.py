from django.conf.urls import url

from HelloWorld import views

urlpatterns=[


    # in that sayHelloWorld is the function  our ViewName/fucnton  name
    # you can try without specicying any name

    url(r'^',views.sayHelloWorld,name='sayHelloWorld')
]