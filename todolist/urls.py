from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.loginPage, name='default'),
    url(r'^login/',views.loginPage, name='loginPage'),
    url(r'^logout/',views.logoutUser, name='logout'),
    url(r'^registration/',views.registerPage, name='registerPage'),
    url(r'^home/', views.index, name='index'),
    url(r'^add/', views.addTodo, name='add'),
    url(r'^complete/(?P<todo_id>\d)/$',views.completeTodo, name='complete'),
    url(r'^deleteCompleted/', views.deleteCompleted, name='deleteCompleted'),
    url(r'^deleteAll/', views.deleteAll, name='deleteAll')
]
