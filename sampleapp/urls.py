from django.urls import path

from sampleapp import views
urlpatterns = [
    path("",views.first,name="first"),
    path("one",views.show,name="show"),
    path("display",views.display,name="display"),
    path("parent",views.parent,name="parent"),
    path("child",views.child,name="child"),
    path("cssstyle",views.cssstyle,name="cssstyle"),
    path("view",views.view,name="view"),
    path("djangoforms",views.djangoforms,name="djangoforms"),
    path("r",views.regform,name="regform"),
    path("mail",views.newmail,name="newmail"),
    path("regview",views.regview,name="regview"),
    path('regdelete/<int:id>',views.regdelete,name="regdelete"),
    path('regedit/<int:id>',views.regedit,name="regedit"),
    path('regupdate/<int:id>',views.regupdate,name="regupdate"),
    path("e",views.employees,name="employees"),
    path("view_emp",views.view_emp,name="view_emp"),
    path('emp_delete/<int:id>',views.emp_delete,name="emp_delete"),
    path('emp_edit/<int:id>',views.emp_edit,name="emp_edit"),
    path('emp_update/<int:id>',views.emp_update,name="emp_update"),
    path("regfile",views.regfile,name="regfile"),
    path("emppoint",views.emppoint,name="emppoint"),
    path("setcookie",views.setcookie,name="setcookie"),
    path("getcookie",views.getcookie,name="getcookie"),
    path("setsession",views.setsession,name="setsession"),
    path("getsession",views.getsession,name="getsession"),

    path('trainercreate/create/',views.TrainerCreate.as_view(),name='TrainerCreate'),
    path('trainercreate/',views.TrainerList.as_view(),name='TrainerList'),
    path('trainercreate/<int:pk>/',views.TrainerDetail.as_view(),name='TrainerDetail'),
    path('trainercreate/<int:pk>/update/',views.TrainerUpdate.as_view(),name='TrainerUpdate'),
    path('trainercreate/<int:pk>/delete/',views.TrainerDelete.as_view(),name='TrainerDelete'),


    path("test1",views.test1,name="test1"),
    path("vtest1",views.vtest1,name="vtest1"),










]
