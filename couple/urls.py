
from django.contrib import admin
from django.urls import path
from couple import views


urlpatterns = [
    path('couple/<int:name>', views.CoupleView, name='CoupleView'),
    path('', views.IndexView, name='IndexView'),
    path('addcouple', views.CreateCoupleView.as_view(), name='AddCouple'),
    path('addteacher', views.CreateTeacherView.as_view(), name='AddTeacher'),
    path('addcoupleadmin', views.CreateCoupleViewAdmin.as_view(), name='AddCoupleAdmin'),
    path('addstudent', views.CreateStudentView.as_view(), name='AddStudent'),
    path('addgroup', views.CreateGroupView.as_view(), name='AddGroup'),
    path('delete_student/<int:pk>', views.delete_student, name='delete_student'),
    path('delete-teacher/<int:pk>', views.delete_teacher, name='delete_teacher'),
    path('deletegroup/<int:pk>', views.delete_group, name='delete_group'),
    path('delete-page/<int:pk>', views.delete_couple, name='delete_couple'),
    path('updateCouple/<int:pk>', views.CoupleUpdateView.as_view(), name='updateCouple'),
    path('updateCoupleAdmin/<int:pk>', views.CoupleUpdateViewAdmin.as_view(), name='updateCoupleAdmin'),
    path('updateTeacher/<int:pk>', views.TeacherUpdateView.as_view(), name='updateTeacher'),
    path('updateStudent/<int:pk>', views.UpdateStudentView.as_view(), name='updateStudent'),
    path('updateGroup/<int:pk>', views.UpdateGroupView.as_view(), name='updateGroup'),
    path('login', views.MyprojectLoginView.as_view(), name='login_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('logout', views.MyProjectLogout.as_view(), name='logout_page'),
]
