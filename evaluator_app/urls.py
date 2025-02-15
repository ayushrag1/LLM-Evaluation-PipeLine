from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("evaluate", views.EvaluationRequestViewSet)

urlpatterns = [
    path("", views.HealthCheck.as_view()),
    path("", include(router.urls)),
]
