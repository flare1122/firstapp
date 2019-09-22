from django.conf.urls import url
from myapp  import views

urlpatterns = (
    url(r'index', views.index),
    url(r'grade/$', views.grade),
    url(r'student/$', views.student),
    url(r'grade/(\d+)$',views.StudentInGrade),
    url(r'login/$',views.login)
#    url(r'^$', 'home')
)
