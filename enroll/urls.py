from django.urls import path
from .views import home, studentList,deleteStudent, updateStudent

urlpatterns = [
    path('', home ,name='home'),
    path('students/',studentList, name='student-list'),
    path('delete/<int:id>/',deleteStudent, name='delete-student'),
    path('update/<int:id>/',updateStudent, name='update-student')
]
