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

class SmartBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SmartBlock
        fields = '__all__'

class SmartBlockContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SmartBlockContent
        fields = '__all__'

class SmartBlockCriteriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SmartBlockCriteria
        fields = '__all__'

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class ListenerCountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListenerCount
        fields = '__all__'

class LiveLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LiveLog
        fields = '__all__'

class LoginAttemptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoginAttempt
        fields = '__all__'

class MountNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MountName
        fields = '__all__'

class MusicDirSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MusicDir
        fields = '__all__'

class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class PlaylistContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlaylistContent
        fields = '__all__'

class PlayoutHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayoutHistory
        fields = '__all__'

class PlayoutHistoryMetadataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayoutHistoryMetadata
        fields = '__all__'

class PlayoutHistoryTemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayoutHistoryTemplate
        fields = '__all__'

class PlayoutHistoryTemplateFieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayoutHistoryTemplateField
        fields = '__all__'

class PreferenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Preference
        fields = '__all__'

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class ServiceRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceRegister
        fields = '__all__'

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'

class ShowDaysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowDays
        fields = '__all__'

class ShowHostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowHost
        fields = '__all__'

class ShowInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowInstance
        fields = '__all__'

class ShowRebroadcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowRebroadcast
        fields = '__all__'

class SmembSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Smemb
        fields = '__all__'

class StreamSettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StreamSetting
        fields = '__all__'

class UserTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserToken
        fields = '__all__'

class TimestampSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timestamp
        fields = '__all__'

class WebstreamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Webstream
        fields = '__all__'

class WebstreamMetadataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WebstreamMetadata
        fields = '__all__'

class CeleryTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CeleryTask
        fields = '__all__'

class CloudFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CloudFile
        fields = '__all__'

class ImportedPodcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImportedPodcast
        fields = '__all__'

class PodcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'

class PodcastEpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PodcastEpisode
        fields = '__all__'

class StationPodcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StationPodcast
        fields = '__all__'

class ThirdPartyTrackReferenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThirdPartyTrackReference
        fields = '__all__'

class TrackTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrackType
        fields = '__all__'
