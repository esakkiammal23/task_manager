from django.urls import path
from . import views


urlpatterns=[
    path('tasks/',views.get_tasks),
    path('tasks/add',views.add),
    path('tasks/update/<int:pk>',views.update),
    path('tasks/delete/<int:pk>',views.delete),

]