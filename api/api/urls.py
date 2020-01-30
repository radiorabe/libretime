from django.conf.urls import url, include
from rest_framework import routers

from .serializers import SmartBlockViewSet, SmartBlockContentsViewSet, SmartBlockCriteriaViewSet, CountryViewSet, FileViewSet, ListenerCountViewSet, LiveLogViewSet, LoginAttemptsViewSet, MountNameViewSet, MusicDirViewSet, UserViewSet, StreamSettingViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'smartblock', SmartBlockViewSet)
router.register(r'smartblock-contents', SmartBlockContentsViewSet)
router.register(r'smartblock-criteria', SmartBlockCriteriaViewSet)
router.register(r'country', CountryViewSet)
router.register(r'files', FileViewSet)
router.register(r'listener-counts', ListenerCountViewSet)
router.register(r'live-log', LiveLogViewSet)
router.register(r'login-attempts', LoginAttemptsViewSet)
router.register(r'mount-names', MountNameViewSet)
router.register(r'music-directories', MusicDirViewSet)
router.register(r'login-attempts', LoginAttemptsViewSet)
router.register(r'stream-settings', StreamSettingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
