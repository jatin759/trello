from django.urls import path
from projects.views import ProjectView, ParticularProjectView, UserProjectView

urlpatterns = [
    path('', ProjectView.as_view(), name='project_board'),
    path('<int:pbid>/', ParticularProjectView.as_view(),
         name='particular_project_board'),
    path('user/<int:pbid>/', UserProjectView.as_view(),
         name='user_project_relation'),
]