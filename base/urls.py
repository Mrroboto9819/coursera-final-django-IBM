from django.urls import path
from . import views

app_name="base"

urlpatterns = [
    path(route='', view=views.IndexView.as_view(), name="index"),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('submit-exam/', views.submit_exam, name='submit_exam'),
    path('registration/', views.registration_request, name='registration'),
    path('course/<str:course_id>/', view=views.CourseDetailsView.as_view(), name='course_detail'),
    path('exam/<str:exam_id>/', view=views.ExamDetailsView.as_view(), name='exam_detail'),
    path('exam/grades/<str:exam_id>', view=views.GradesView.as_view(), name='grades'),
]