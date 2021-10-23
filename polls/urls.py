from django.urls import path
from polls import views

urlpatterns = [
    path('std',views.add_show,name="addshow"),
    path('delete/<int:id>/',views.delete_data,name="delete"),
    path('update/<int:id>/',views.update_data,name="update"),

]
