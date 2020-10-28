from django.views.generic import TemplateView
from django.urls import path

from rest_framework.schemas import get_schema_view

from .views import PostList, PostDetail


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),

    #  path to dynamic OpenAPI schema (used in redoc path)
    path('openapi/', get_schema_view(
        title="My Blog",
        description="Small blog project",
        version="1.0.0"
    ), name='openapi-schema'),

    # redoc documentation for the API
    path('redoc/', TemplateView.as_view(
        template_name='posts/redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),
]
