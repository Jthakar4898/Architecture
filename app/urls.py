from django.urls import path
from . import views

urlpatterns = [
    # -----------------------------------(Client side page url)-------------------------------------------------
    # ......index page(Home)..
	path('', views.index, name="index"),
    path('index', views.index, name="index"),


    # ......about page...
    path('about', views.about, name="about"),


    # ....contact page ...
    path('contact', views.contact, name="contact"),

    # ...Feature page....
    path('feature', views.feature, name="feature"),

    # ...services page.....
    path('services', views.services, name="services"),

    # ... portfolio page....
    path('showportfolio', views.showportfolio, name="showportfolio"),

    # ...project detail page....
    path('showportfolio/<id>', views.detail_portfolio),

    # -------------------------------------(Admin side Url)-----------------------------------------------
    # ...Admin login....
    # path('archlogin', views.archlogin, name="archlogin"),

    # ...Admin logout...
    path('logoutUser', views.logoutUser, name="logoutUser"),

    # ..............Admin dashboard........
    path('padmin', views.padmin, name="padmin"),

    # .......Conformation page (saved data)......
    path('saved', views.saved, name="saved"),

    # ......Contact list.........
    path('acontactlist', views.acontactlist, name="acontcatlist"),

    # ..........Uploaded portfolio list............
    path('aportfoliolist', views.aportfoliolist, name="aportfoliolist"),

    # ............Uploaded project list............
    path('aprojectlist', views.aprojectlist, name="aprojectlist"),

    # ...........Upload portfolio form...........
    path('auploadportfolio', views.auploadportfolio, name="auploadportfolio"),

    # ..........upload project form..............
    path('auploadproject', views.auploadproject, name="auploadproject"),

    # ......... Update project form..........
    path('editproject/<id>', views.editproject,name="editproject"),

    # ..........Delete project............
    path('deleteproject/<id>', views.deleteproject,name="deleteproject"),

    # ..............Delete portfolio .............
    path('deleteportfolio/<id>', views.deleteportfolio,name="deleteportfolio"),
    # path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    # path('add/', views.addPhoto, name='add'),
    # path('gallery', views.gallery, name='gallery'),
    # path('register', views.register, name='register'),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

]