
from .views import *
from django.urls import path

urlpatterns = [
    # CRUD for template
    path('template/list/', TemplateListView.as_view(), name='template_list'),
    path('template/create/', TemplateCreateView.as_view(), name='tamplate_create'),
    path('template/<int:pk>/update/', TemplateUpdateView.as_view(), name='template_update'),
    path('template/<int:pk>/delete/', TemplateDeleteView.as_view(), name='template_delete'),

    path('template/<int:pk>/', TemplateDetailView.as_view(), name='template'),
    path('create-document/<int:pk>', CreateDocumentView.as_view(), name='create_document'),
    path('', HomeView.as_view(), name='home'),
]
