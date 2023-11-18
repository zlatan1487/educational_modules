from django.urls import path
from education_modules.apps import EducationModulesConfig
from education_modules.views import EducationCreateView, \
                                    EducationsListView, \
                                    EducationsDetailView, \
                                    EducationEditView, \
                                    EducationDeleteView, \
                                    delete_review

app_name = EducationModulesConfig.name


urlpatterns = [
    path('create/', EducationCreateView.as_view(),
         name='create_education'),
    path('', EducationsListView.as_view(),
         name='education_list'),
    path('education_detail/<int:pk>/', EducationsDetailView.as_view(),
         name='education_detail'),
    path('education_detail/<int:pk>/add_review/',
         EducationsDetailView.as_view(),
         name='add_review'),
    path('edit/<int:pk>', EducationEditView.as_view(),
         name='education_update'),
    path('delete/<int:pk>', EducationDeleteView.as_view(),
         name='education_delete'),
    path('delete_review/<int:review_id>/', delete_review,
         name='delete_review'),
]
