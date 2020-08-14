from django.urls import path

from . import views

urlpatterns=[
path('',views.home,name='item'),
    path('index/',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('list/',views.MartList,name='list'),
path('detail/<pk>',views.MartDetail,name='detail'),
path('update/<pk>',views.MartUpdate,name='update'),
path('delete/<pk>',views.MartDelete,name='delete'),
path('complete/',views.MartComp,name='complete'),
path('comp/<pk>', views.MartCopmpleted, name='MartCompleted'),
path('pdf/<pk>',views.generate_pdf,name='pdf'),

]