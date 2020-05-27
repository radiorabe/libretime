from django.conf.urls import url, include
from rest_framework import routers

from .serializers import *

router = routers.DefaultRouter()
router.register('smart-blocks', SmartBlockViewSet)
router.register('smart-block-contents', SmartBlockContentViewSet)
router.register('smart-block-criterias', SmartBlockCriteriaViewSet)
router.register('countries', CountryViewSet)
router.register('files', FileViewSet)
router.register('listener-counts', ListenerCountViewSet)
router.register('live-logs', LiveLogViewSet)
router.register('login-attempts', LoginAttemptViewSet)
router.register('mount-names', MountNameViewSet)
router.register('music-dirs', MusicDirViewSet)
router.register('permissions', PermissionViewSet)
router.register('playlists', PlaylistViewSet)
router.register('playlist-contents', PlaylistContentViewSet)
router.register('playout-history', PlayoutHistoryViewSet)
router.register('playout-history-metadata', PlayoutHistoryMetadataViewSet)
router.register('playout-history-templates', PlayoutHistoryTemplateViewSet)
router.register('playout-history-template-fields', PlayoutHistoryTemplateFieldViewSet)
router.register('preferences', PreferenceViewSet)
router.register('schedules', ScheduleViewSet)
router.register('service-registers', ServiceRegisterViewSet)
router.register('sessions', SessionViewSet)
router.register('shows', ShowViewSet)
router.register('show-days', ShowDaysViewSet)
router.register('show-hosts', ShowHostViewSet)
router.register('show-instances', ShowInstanceViewSet)
router.register('show-rebroadcasts', ShowRebroadcastViewSet)
router.register('smembs', SmembViewSet)
router.register('stream-settings', StreamSettingViewSet)
router.register('users', UserViewSet)
router.register('user-tokens', UserTokenViewSet)
router.register('timestamps', TimestampViewSet)
router.register('webstreams', WebstreamViewSet)
router.register('webstream-metadata', WebstreamMetadataViewSet)
router.register('celery-tasks', CeleryTaskViewSet)
router.register('cloud-files', CloudFileViewSet)
router.register('imported-podcasts', ImportedPodcastViewSet)
router.register('podcasts', PodcastViewSet)
router.register('podcast-episodes', PodcastEpisodeViewSet)
router.register('station-podcasts', StationPodcastViewSet)
router.register('third-party-track-references', ThirdPartyTrackReferenceViewSet)
router.register('track-types', TrackTypeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
