from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.response import Response
from quickstart import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'ligne', views.LigneViewSet)
router.register(r'tram', views.TramViewSet)
router.register(r'trajet', views.TrajetViewSet)

# Use automatic URL routing
# Can also include login URLs for the browsable API
urlpatterns = [
    path('', include(router.urls)),
    path('connexion/', obtain_auth_token, name='api_token_auth'),
]
