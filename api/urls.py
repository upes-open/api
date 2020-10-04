from rest_framework_nested import routers
from django.urls import include, path
from api.views import MemberDetailView

router = routers.SimpleRouter()

router.register(r'members', MemberDetailView)

urlpatterns = [
    path('', include(router.urls)),
]
