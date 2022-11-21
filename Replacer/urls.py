
from .views import *
from django.urls import path

urlpatterns = [
    # CRUD for template
    path('', HomeView.as_view(), name='home'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),

    path('template/list/', TemplateListView.as_view(), name='template_list'),
    path('template/create/', TemplateCreateView.as_view(), name='tamplate_create'),
    path('template/<int:pk>/update/', TemplateUpdateView.as_view(), name='template_update'),
    path('template/<int:pk>/delete/', TemplateDeleteView.as_view(), name='template_delete'),

    path('fields/list/<int:pk>/', FieldsForTemplateView.as_view(), name='fields_list'),
    path('fields/create/', FieldsForTemplateCreateView.as_view(), name='fields_create'),
    path('fields/<int:pk>/update/', FieldsForTemplateUpdateView.as_view(), name='fields_update'),
    path('fields/<int:pk>/delete/', FieldsForTemplateDeleteView.as_view(), name='fields_delete'),

    path('template/<int:pk>/', TemplateDetailView.as_view(), name='template'),
    path('create-document/<int:pk>', CreateDocumentView.as_view(), name='create_document'),
]
