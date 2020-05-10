
from django.urls import path
#importing from . means from current directory
from . import views
#above line says that from current directory we are importing views.py into this program

#urlpatterns is a list which associates a particular url with a particular view from the project

urlpatterns = [
    path("", views.index, name = "index"), #itmeans the empty path which is the basic nothing after / then display a particular view
    path("<int:flight_id>",views.flight, name = "flight"),
    path("<int:flight_id>/book",views.book,name = "book")
]
