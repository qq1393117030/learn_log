"""定义learning_logs的url模式"""
from django.urls import path,re_path
from .import views
app_name='[learning_logs]'
urlpatterns = [
	# homepage
	path(r'',views.index,name='index'),
	# display all topics
	path(r'topics/',views.topics,name='topics'),
	# dispaly entry of a topic 
	# path(r'topics/^(?P<topic_id>\d+/$)',views.topic,name='topic'),
	path(r'topics/<topic_id>',views.topic,name='topic'),
]
