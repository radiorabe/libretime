from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets
from .models import SmartBlock, SmartBlockContents, SmartBlockCriteria, Country, File, ListenerCount, LiveLog, LoginAttempts, MountName, MusicDir, StreamSetting

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

class StreamSettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StreamSetting
        fields = '__all__'

class StreamSettingViewSet(viewsets.ModelViewSet):
    queryset = StreamSetting.objects.all()
    serializer_class = StreamSettingSerializer

class SmartBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SmartBlock
        fields = '__all__'

class SmartBlockViewSet(viewsets.ModelViewSet):
    queryset = SmartBlock.objects.all()
    serializer_class = SmartBlockSerializer

class SmartBlockContentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SmartBlockContents
        fields = '__all__'

class SmartBlockContentsViewSet(viewsets.ModelViewSet):
    queryset = SmartBlockContents.objects.all()
    serializer_class = SmartBlockContentsSerializer

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

class LoginAttemptsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoginAttempts
        fields = '__all__'

class LoginAttemptsViewSet(viewsets.ModelViewSet):
    queryset = LoginAttempts.objects.all()
    serializer_class = LoginAttemptsSerializer

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
