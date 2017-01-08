from django.conf.urls import url

from audisim.views.index import index
from audisim.views.project import project
from audisim.views.client import client
from audisim.views.user import user

urlpatterns = [
    url(r'^index/$', index.index, name='index'),
    url(r'^projects/1$', project.project_detail, name='project_detail'),
    url(r'^projects/new/$', project.new_project, name='new_project'),
    url(r'^projects/$', project.project_index, name='project_index'),
    url(r'^clients/$', client.client_index, name='client_index'),
    url(r'^users/$', user.user_index, name='user_index'),
url(r'', index.index, name='index')
]
