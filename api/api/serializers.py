from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'url',
            'username',
            'type',
            'first_name',
            'last_name',
            'lastfail',
            'skype_contact',
            'jabber_contact',
            'email',
            'cell_phone',
            'login_attempts',
        ]

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class SmartBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SmartBlock
        fields = '__all__'

class SmartBlockViewSet(viewsets.ModelViewSet):
    queryset = SmartBlock.objects.all()
    serializer_class = SmartBlockSerializer

class SmartBlockContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SmartBlockContent
        fields = '__all__'

class SmartBlockContentViewSet(viewsets.ModelViewSet):
    queryset = SmartBlockContent.objects.all()
    serializer_class = SmartBlockContentSerializer

class SmartBlockCriteriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SmartBlockCriteria
        fields = '__all__'

class SmartBlockCriteriaViewSet(viewsets.ModelViewSet):
    queryset = SmartBlockCriteria.objects.all()
    serializer_class = SmartBlockCriteriaSerializer

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class ListenerCountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListenerCount
        fields = '__all__'

class ListenerCountViewSet(viewsets.ModelViewSet):
    queryset = ListenerCount.objects.all()
    serializer_class = ListenerCountSerializer

class LiveLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LiveLog
        fields = '__all__'

class LiveLogViewSet(viewsets.ModelViewSet):
    queryset = LiveLog.objects.all()
    serializer_class = LiveLogSerializer

class LoginAttemptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoginAttempt
        fields = '__all__'

class LoginAttemptViewSet(viewsets.ModelViewSet):
    queryset = LoginAttempt.objects.all()
    serializer_class = LoginAttemptSerializer

class MountNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MountName
        fields = '__all__'

class MountNameViewSet(viewsets.ModelViewSet):
    queryset = MountName.objects.all()
    serializer_class = MountNameSerializer

class MusicDirSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MusicDir
        fields = '__all__'

class MusicDirViewSet(viewsets.ModelViewSet):
    queryset = MusicDir.objects.all()
    serializer_class = MusicDirSerializer

class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlaylistContent
        fields = '__all__'

class PlaylistContentViewSet(viewsets.ModelViewSet):
    queryset = PlaylistContent.objects.all()
    serializer_class = PlaylistContentSerializer

class PlayoutHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayoutHistory
        fields = '__all__'

class PlayoutHistoryViewSet(viewsets.ModelViewSet):
    queryset = PlayoutHistory.objects.all()
    serializer_class = PlayoutHistorySerializer

class PlayoutHistoryMetadataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayoutHistoryMetadata
        fields = '__all__'

class PlayoutHistoryMetadataViewSet(viewsets.ModelViewSet):
    queryset = PlayoutHistoryMetadata.objects.all()
    serializer_class = PlayoutHistoryMetadataSerializer

class PlayoutHistoryTemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayoutHistoryTemplate
        fields = '__all__'

class PlayoutHistoryTemplateViewSet(viewsets.ModelViewSet):
    queryset = PlayoutHistoryTemplate.objects.all()
    serializer_class = PlayoutHistoryTemplateSerializer

class PlayoutHistoryTemplateFieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayoutHistoryTemplateField
        fields = '__all__'

class PlayoutHistoryTemplateFieldViewSet(viewsets.ModelViewSet):
    queryset = PlayoutHistoryTemplateField.objects.all()
    serializer_class = PlayoutHistoryTemplateFieldSerializer

class PreferenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Preference
        fields = '__all__'

class PreferenceViewSet(viewsets.ModelViewSet):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class ServiceRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceRegister
        fields = '__all__'

class ServiceRegisterViewSet(viewsets.ModelViewSet):
    queryset = ServiceRegister.objects.all()
    serializer_class = ServiceRegisterSerializer

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'

class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class ShowDaysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowDays
        fields = '__all__'

class ShowDaysViewSet(viewsets.ModelViewSet):
    queryset = ShowDays.objects.all()
    serializer_class = ShowDaysSerializer

class ShowHostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowHost
        fields = '__all__'

class ShowHostViewSet(viewsets.ModelViewSet):
    queryset = ShowHost.objects.all()
    serializer_class = ShowHostSerializer

class ShowInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowInstance
        fields = '__all__'

class ShowInstanceViewSet(viewsets.ModelViewSet):
    queryset = ShowInstance.objects.all()
    serializer_class = ShowInstanceSerializer

class ShowRebroadcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowRebroadcast
        fields = '__all__'

class ShowRebroadcastViewSet(viewsets.ModelViewSet):
    queryset = ShowRebroadcast.objects.all()
    serializer_class = ShowRebroadcastSerializer

class SmembSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Smemb
        fields = '__all__'

class SmembViewSet(viewsets.ModelViewSet):
    queryset = Smemb.objects.all()
    serializer_class = SmembSerializer

class StreamSettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StreamSetting
        fields = '__all__'

class StreamSettingViewSet(viewsets.ModelViewSet):
    queryset = StreamSetting.objects.all()
    serializer_class = StreamSettingSerializer

class UserTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserToken
        fields = '__all__'

class UserTokenViewSet(viewsets.ModelViewSet):
    queryset = UserToken.objects.all()
    serializer_class = UserTokenSerializer

class TimestampSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timestamp
        fields = '__all__'

class TimestampViewSet(viewsets.ModelViewSet):
    queryset = Timestamp.objects.all()
    serializer_class = TimestampSerializer

class WebstreamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Webstream
        fields = '__all__'

class WebstreamViewSet(viewsets.ModelViewSet):
    queryset = Webstream.objects.all()
    serializer_class = WebstreamSerializer

class WebstreamMetadataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WebstreamMetadata
        fields = '__all__'

class WebstreamMetadataViewSet(viewsets.ModelViewSet):
    queryset = WebstreamMetadata.objects.all()
    serializer_class = WebstreamMetadataSerializer

class CeleryTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CeleryTask
        fields = '__all__'

class CeleryTaskViewSet(viewsets.ModelViewSet):
    queryset = CeleryTask.objects.all()
    serializer_class = CeleryTaskSerializer

class CloudFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CloudFile
        fields = '__all__'

class CloudFileViewSet(viewsets.ModelViewSet):
    queryset = CloudFile.objects.all()
    serializer_class = CloudFileSerializer

class ImportedPodcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImportedPodcast
        fields = '__all__'

class ImportedPodcastViewSet(viewsets.ModelViewSet):
    queryset = ImportedPodcast.objects.all()
    serializer_class = ImportedPodcastSerializer

class PodcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

class PodcastEpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PodcastEpisode
        fields = '__all__'

class PodcastEpisodeViewSet(viewsets.ModelViewSet):
    queryset = PodcastEpisode.objects.all()
    serializer_class = PodcastEpisodeSerializer

class StationPodcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StationPodcast
        fields = '__all__'

class StationPodcastViewSet(viewsets.ModelViewSet):
    queryset = StationPodcast.objects.all()
    serializer_class = StationPodcastSerializer

class ThirdPartyTrackReferenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThirdPartyTrackReference
        fields = '__all__'

class ThirdPartyTrackReferenceViewSet(viewsets.ModelViewSet):
    queryset = ThirdPartyTrackReference.objects.all()
    serializer_class = ThirdPartyTrackReferenceSerializer

class TrackTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrackType
        fields = '__all__'

class TrackTypeViewSet(viewsets.ModelViewSet):
    queryset = TrackType.objects.all()
    serializer_class = TrackTypeSerializer
