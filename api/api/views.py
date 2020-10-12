from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class SmartBlockViewSet(viewsets.ModelViewSet):
    queryset = SmartBlock.objects.all()
    serializer_class = SmartBlockSerializer

class SmartBlockContentViewSet(viewsets.ModelViewSet):
    queryset = SmartBlockContent.objects.all()
    serializer_class = SmartBlockContentSerializer

class SmartBlockCriteriaViewSet(viewsets.ModelViewSet):
    queryset = SmartBlockCriteria.objects.all()
    serializer_class = SmartBlockCriteriaSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class ListenerCountViewSet(viewsets.ModelViewSet):
    queryset = ListenerCount.objects.all()
    serializer_class = ListenerCountSerializer

class LiveLogViewSet(viewsets.ModelViewSet):
    queryset = LiveLog.objects.all()
    serializer_class = LiveLogSerializer

class LoginAttemptViewSet(viewsets.ModelViewSet):
    queryset = LoginAttempt.objects.all()
    serializer_class = LoginAttemptSerializer

class MountNameViewSet(viewsets.ModelViewSet):
    queryset = MountName.objects.all()
    serializer_class = MountNameSerializer

class MusicDirViewSet(viewsets.ModelViewSet):
    queryset = MusicDir.objects.all()
    serializer_class = MusicDirSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistContentViewSet(viewsets.ModelViewSet):
    queryset = PlaylistContent.objects.all()
    serializer_class = PlaylistContentSerializer

class PlayoutHistoryViewSet(viewsets.ModelViewSet):
    queryset = PlayoutHistory.objects.all()
    serializer_class = PlayoutHistorySerializer

class PlayoutHistoryMetadataViewSet(viewsets.ModelViewSet):
    queryset = PlayoutHistoryMetadata.objects.all()
    serializer_class = PlayoutHistoryMetadataSerializer

class PlayoutHistoryTemplateViewSet(viewsets.ModelViewSet):
    queryset = PlayoutHistoryTemplate.objects.all()
    serializer_class = PlayoutHistoryTemplateSerializer

class PlayoutHistoryTemplateFieldViewSet(viewsets.ModelViewSet):
    queryset = PlayoutHistoryTemplateField.objects.all()
    serializer_class = PlayoutHistoryTemplateFieldSerializer

class PreferenceViewSet(viewsets.ModelViewSet):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class ServiceRegisterViewSet(viewsets.ModelViewSet):
    queryset = ServiceRegister.objects.all()
    serializer_class = ServiceRegisterSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class ShowDaysViewSet(viewsets.ModelViewSet):
    queryset = ShowDays.objects.all()
    serializer_class = ShowDaysSerializer

class ShowHostViewSet(viewsets.ModelViewSet):
    queryset = ShowHost.objects.all()
    serializer_class = ShowHostSerializer

class ShowInstanceViewSet(viewsets.ModelViewSet):
    queryset = ShowInstance.objects.all()
    serializer_class = ShowInstanceSerializer

class ShowRebroadcastViewSet(viewsets.ModelViewSet):
    queryset = ShowRebroadcast.objects.all()
    serializer_class = ShowRebroadcastSerializer

class SmembViewSet(viewsets.ModelViewSet):
    queryset = Smemb.objects.all()
    serializer_class = SmembSerializer

class StreamSettingViewSet(viewsets.ModelViewSet):
    queryset = StreamSetting.objects.all()
    serializer_class = StreamSettingSerializer

class UserTokenViewSet(viewsets.ModelViewSet):
    queryset = UserToken.objects.all()
    serializer_class = UserTokenSerializer

class TimestampViewSet(viewsets.ModelViewSet):
    queryset = Timestamp.objects.all()
    serializer_class = TimestampSerializer

class WebstreamViewSet(viewsets.ModelViewSet):
    queryset = Webstream.objects.all()
    serializer_class = WebstreamSerializer

class WebstreamMetadataViewSet(viewsets.ModelViewSet):
    queryset = WebstreamMetadata.objects.all()
    serializer_class = WebstreamMetadataSerializer

class CeleryTaskViewSet(viewsets.ModelViewSet):
    queryset = CeleryTask.objects.all()
    serializer_class = CeleryTaskSerializer

class CloudFileViewSet(viewsets.ModelViewSet):
    queryset = CloudFile.objects.all()
    serializer_class = CloudFileSerializer

class ImportedPodcastViewSet(viewsets.ModelViewSet):
    queryset = ImportedPodcast.objects.all()
    serializer_class = ImportedPodcastSerializer

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

class PodcastEpisodeViewSet(viewsets.ModelViewSet):
    queryset = PodcastEpisode.objects.all()
    serializer_class = PodcastEpisodeSerializer

class StationPodcastViewSet(viewsets.ModelViewSet):
    queryset = StationPodcast.objects.all()
    serializer_class = StationPodcastSerializer

class ThirdPartyTrackReferenceViewSet(viewsets.ModelViewSet):
    queryset = ThirdPartyTrackReference.objects.all()
    serializer_class = ThirdPartyTrackReferenceSerializer

class TrackTypeViewSet(viewsets.ModelViewSet):
    queryset = TrackType.objects.all()
    serializer_class = TrackTypeSerializer

@api_view(['GET'])
def version(request, *args, **kwargs):
    return Response({'version': settings.API_VERSION})
