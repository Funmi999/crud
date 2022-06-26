from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.postlistview.as_view(), name="all"),
    path("create/", views.postcreateview.as_view(), name="post_create"),
    path("delete/<slug:slug>", views.postdeleteview.as_view(), name="post_delete"),
    path("update/<slug:slug>", views.postupdateview.as_view(), name="post_update"),
    path("read/<slug:slug>", views.postdetailView.as_view(), name="post_detail"),

]
