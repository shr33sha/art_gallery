# artapp/urls.py
from django.urls import path, re_path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API for Art Gallery App",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('artists/category/<str:category_name>/', views.get_artists_by_category),
    path('artists/blockbuster/', views.get_blockbuster_artists),
    path('artists/shop_by_price/<int:min_price>/<int:max_price>/', views.shop_by_price),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
