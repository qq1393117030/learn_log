"""定义learning_logs的url模式"""
from django.urls import path
from .import views
app_name='[learning_logs]'
urlpatterns = [
	# homepage
	path(r'',views.index,name='index'),
]
