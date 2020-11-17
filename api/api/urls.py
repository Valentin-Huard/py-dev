from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'ligne', views.LigneViewSet)
router.register(r'tram', views.TramViewSet)
router.register(r'trajet', views.TrajetViewSet)

# Use automatic URL routing
# Can also include login URLs for the browsable API
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
