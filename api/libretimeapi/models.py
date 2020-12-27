# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import hashlib
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class SmartBlock(models.Model):
    name = models.CharField(max_length=255)
    mtime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    length = models.DurationField(blank=True, null=True)
    type = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_block'


class SmartBlockContent(models.Model):
    block = models.ForeignKey(SmartBlock, models.DO_NOTHING, blank=True, null=True)
    file = models.ForeignKey('File', models.DO_NOTHING, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    trackoffset = models.FloatField()
    cliplength = models.DurationField(blank=True, null=True)
    cuein = models.DurationField(blank=True, null=True)
    cueout = models.DurationField(blank=True, null=True)
    fadein = models.TimeField(blank=True, null=True)
    fadeout = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_blockcontents'


class SmartBlockCriteria(models.Model):
    criteria = models.CharField(max_length=32)
    modifier = models.CharField(max_length=16)
    value = models.CharField(max_length=512)
    extra = models.CharField(max_length=512, blank=True, null=True)
    criteriagroup = models.IntegerField(blank=True, null=True)
    block = models.ForeignKey(SmartBlock, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cc_blockcriteria'


class Country(models.Model):
    isocode = models.CharField(primary_key=True, max_length=3)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cc_country'


class File(models.Model):
    name = models.CharField(max_length=255)
    mime = models.CharField(max_length=255)
    ftype = models.CharField(max_length=128)
    directory = models.ForeignKey('MusicDir', models.DO_NOTHING, db_column='directory', blank=True, null=True)
    filepath = models.TextField(blank=True, null=True)
    import_status = models.IntegerField()
    currently_accessing = models.IntegerField(db_column='currentlyaccessing')
    edited_by = models.ForeignKey('User', models.DO_NOTHING, db_column='editedby', blank=True, null=True, related_name='edited_files')
    mtime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    lptime = models.DateTimeField(blank=True, null=True)
    md5 = models.CharField(max_length=32, blank=True, null=True)
    track_title = models.CharField(max_length=512, blank=True, null=True)
    artist_name = models.CharField(max_length=512, blank=True, null=True)
    bit_rate = models.IntegerField(blank=True, null=True)
    sample_rate = models.IntegerField(blank=True, null=True)
    format = models.CharField(max_length=128, blank=True, null=True)
    length = models.DurationField(blank=True, null=True)
    album_title = models.CharField(max_length=512, blank=True, null=True)
    genre = models.CharField(max_length=64, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=16, blank=True, null=True)
    track_number = models.IntegerField(blank=True, null=True)
    channels = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=1024, blank=True, null=True)
    bpm = models.IntegerField(blank=True, null=True)
    rating = models.CharField(max_length=8, blank=True, null=True)
    encoded_by = models.CharField(max_length=255, blank=True, null=True)
    disc_number = models.CharField(max_length=8, blank=True, null=True)
    mood = models.CharField(max_length=64, blank=True, null=True)
    label = models.CharField(max_length=512, blank=True, null=True)
    composer = models.CharField(max_length=512, blank=True, null=True)
    encoder = models.CharField(max_length=64, blank=True, null=True)
    checksum = models.CharField(max_length=256, blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    orchestra = models.CharField(max_length=512, blank=True, null=True)
    conductor = models.CharField(max_length=512, blank=True, null=True)
    lyricist = models.CharField(max_length=512, blank=True, null=True)
    original_lyricist = models.CharField(max_length=512, blank=True, null=True)
    radio_station_name = models.CharField(max_length=512, blank=True, null=True)
    info_url = models.CharField(max_length=512, blank=True, null=True)
    artist_url = models.CharField(max_length=512, blank=True, null=True)
    audio_source_url = models.CharField(max_length=512, blank=True, null=True)
    radio_station_url = models.CharField(max_length=512, blank=True, null=True)
    buy_this_url = models.CharField(max_length=512, blank=True, null=True)
    isrc_number = models.CharField(max_length=512, blank=True, null=True)
    catalog_number = models.CharField(max_length=512, blank=True, null=True)
    original_artist = models.CharField(max_length=512, blank=True, null=True)
    copyright = models.CharField(max_length=512, blank=True, null=True)
    report_datetime = models.CharField(max_length=32, blank=True, null=True)
    report_location = models.CharField(max_length=512, blank=True, null=True)
    report_organization = models.CharField(max_length=512, blank=True, null=True)
    subject = models.CharField(max_length=512, blank=True, null=True)
    contributor = models.CharField(max_length=512, blank=True, null=True)
    language = models.CharField(max_length=512, blank=True, null=True)
    file_exists = models.BooleanField(blank=True, null=True)
    soundcloud_id = models.IntegerField(blank=True, null=True)
    soundcloud_error_code = models.IntegerField(blank=True, null=True)
    soundcloud_error_msg = models.CharField(max_length=512, blank=True, null=True)
    soundcloud_link_to_file = models.CharField(max_length=4096, blank=True, null=True)
    soundcloud_upload_time = models.DateTimeField(blank=True, null=True)
    replay_gain = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    owner = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    cuein = models.DurationField(blank=True, null=True)
    cueout = models.DurationField(blank=True, null=True)
    silan_check = models.BooleanField(blank=True, null=True)
    hidden = models.BooleanField(blank=True, null=True)
    is_scheduled = models.BooleanField(blank=True, null=True)
    is_playlist = models.BooleanField(blank=True, null=True)
    filesize = models.IntegerField()
    description = models.CharField(max_length=512, blank=True, null=True)
    artwork = models.CharField(max_length=512, blank=True, null=True)
    track_type = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_files'


class ListenerCount(models.Model):
    timestamp = models.ForeignKey('Timestamp', models.DO_NOTHING)
    mount_name = models.ForeignKey('MountName', models.DO_NOTHING)
    listener_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cc_listener_count'


class LiveLog(models.Model):
    state = models.CharField(max_length=32)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_live_log'


class LoginAttempt(models.Model):
    ip = models.CharField(primary_key=True, max_length=32)
    attempts = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_login_attempts'


class MountName(models.Model):
    mount_name = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'cc_mount_name'


class MusicDir(models.Model):
    directory = models.TextField(unique=True, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    exists = models.BooleanField(blank=True, null=True)
    watched = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_music_dirs'


class Permission(models.Model):
    permid = models.IntegerField(primary_key=True)
    subj = models.ForeignKey('User', models.DO_NOTHING, db_column='subj', blank=True, null=True)
    action = models.CharField(max_length=20, blank=True, null=True)
    obj = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_perms'
        unique_together = (('subj', 'action', 'obj'),)


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    mtime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    length = models.DurationField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_playlist'


class PlaylistContent(models.Model):
    playlist = models.ForeignKey(Playlist, models.DO_NOTHING, blank=True, null=True)
    file = models.ForeignKey(File, models.DO_NOTHING, blank=True, null=True)
    block = models.ForeignKey(SmartBlock, models.DO_NOTHING, blank=True, null=True)
    stream_id = models.IntegerField(blank=True, null=True)
    type = models.SmallIntegerField()
    position = models.IntegerField(blank=True, null=True)
    trackoffset = models.FloatField()
    cliplength = models.DurationField(blank=True, null=True)
    cuein = models.DurationField(blank=True, null=True)
    cueout = models.DurationField(blank=True, null=True)
    fadein = models.TimeField(blank=True, null=True)
    fadeout = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_playlistcontents'


class PlayoutHistory(models.Model):
    file = models.ForeignKey(File, models.DO_NOTHING, blank=True, null=True)
    starts = models.DateTimeField()
    ends = models.DateTimeField(blank=True, null=True)
    instance = models.ForeignKey('ShowInstance', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_playout_history'


class PlayoutHistoryMetadata(models.Model):
    history = models.ForeignKey(PlayoutHistory, models.DO_NOTHING, related_name="metadata")
    key = models.CharField(max_length=128)
    value = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'cc_playout_history_metadata'


class PlayoutHistoryTemplate(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'cc_playout_history_template'


class PlayoutHistoryTemplateField(models.Model):
    template = models.ForeignKey(PlayoutHistoryTemplate, models.DO_NOTHING)
    name = models.CharField(max_length=128)
    label = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    is_file_md = models.BooleanField()
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cc_playout_history_template_field'


class Preference(models.Model):
    subjid = models.ForeignKey('User', models.DO_NOTHING, db_column='subjid', blank=True, null=True)
    keystr = models.CharField(unique=True, max_length=255, blank=True, null=True)
    valstr = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_pref'
        unique_together = (('subjid', 'keystr'),)


class Schedule(models.Model):
    starts = models.DateTimeField()
    ends = models.DateTimeField()
    file = models.ForeignKey(File, models.DO_NOTHING, blank=True, null=True)
    stream = models.ForeignKey('Webstream', models.DO_NOTHING, blank=True, null=True)
    clip_length = models.DurationField(blank=True, null=True)
    fade_in = models.TimeField(blank=True, null=True)
    fade_out = models.TimeField(blank=True, null=True)
    cue_in = models.DurationField()
    cue_out = models.DurationField()
    media_item_played = models.BooleanField(blank=True, null=True)
    instance = models.ForeignKey('ShowInstance', models.DO_NOTHING)
    playout_status = models.SmallIntegerField()
    broadcasted = models.SmallIntegerField()
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cc_schedule'


class ServiceRegister(models.Model):
    name = models.CharField(primary_key=True, max_length=32)
    ip = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cc_service_register'


class Session(models.Model):
    sessid = models.CharField(primary_key=True, max_length=32)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    login = models.CharField(max_length=255, blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_sess'


class Show(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=8192, blank=True, null=True)
    color = models.CharField(max_length=6, blank=True, null=True)
    background_color = models.CharField(max_length=6, blank=True, null=True)
    live_stream_using_airtime_auth = models.BooleanField(blank=True, null=True)
    live_stream_using_custom_auth = models.BooleanField(blank=True, null=True)
    live_stream_user = models.CharField(max_length=255, blank=True, null=True)
    live_stream_pass = models.CharField(max_length=255, blank=True, null=True)
    linked = models.BooleanField()
    is_linkable = models.BooleanField()
    image_path = models.CharField(max_length=255, blank=True, null=True)
    has_autoplaylist = models.BooleanField()
    autoplaylist = models.ForeignKey(Playlist, models.DO_NOTHING, blank=True, null=True)
    autoplaylist_repeat = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cc_show'


class ShowDays(models.Model):
    first_show = models.DateField()
    last_show = models.DateField(blank=True, null=True)
    start_time = models.TimeField()
    timezone = models.CharField(max_length=1024)
    duration = models.CharField(max_length=1024)
    day = models.SmallIntegerField(blank=True, null=True)
    repeat_type = models.SmallIntegerField()
    next_pop_date = models.DateField(blank=True, null=True)
    show = models.ForeignKey(Show, models.DO_NOTHING)
    record = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_show_days'


class ShowHost(models.Model):
    show = models.ForeignKey(Show, models.DO_NOTHING)
    subjs = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cc_show_hosts'


class ShowInstance(models.Model):
    description = models.CharField(max_length=8192, blank=True, null=True)
    starts = models.DateTimeField()
    ends = models.DateTimeField()
    show = models.ForeignKey(Show, models.DO_NOTHING)
    record = models.SmallIntegerField(blank=True, null=True)
    rebroadcast = models.SmallIntegerField(blank=True, null=True)
    instance = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    file = models.ForeignKey(File, models.DO_NOTHING, blank=True, null=True)
    time_filled = models.DurationField(blank=True, null=True)
    created = models.DateTimeField()
    last_scheduled = models.DateTimeField(blank=True, null=True)
    modified_instance = models.BooleanField()
    autoplaylist_built = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cc_show_instances'


class ShowRebroadcast(models.Model):
    day_offset = models.CharField(max_length=1024)
    start_time = models.TimeField()
    show = models.ForeignKey(Show, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cc_show_rebroadcast'


class Smemb(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    gid = models.IntegerField()
    level = models.IntegerField()
    mid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_smemb'


class StreamSetting(models.Model):
    keyname = models.CharField(primary_key=True, max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'cc_stream_setting'

GUEST = 'G'
DJ = 'H'
PROGRAM_MANAGER = 'P'
ADMIN = 'A'

USER_TYPE_CHOICES = (
    (GUEST, 'Guest'),
    (DJ, 'DJ'),
    (PROGRAM_MANAGER, 'Program Manager'),
    (ADMIN, 'Admin'),
)

class UserManager(BaseUserManager):
    def create_user(self, username, type, email, first_name, last_name, password):
        user = self.model(username=username,
                          type=type,
                          email=email,
                          first_name=first_name,
                          last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password):
        user = self.create_user(username, ADMIN, email, first_name, last_name, password)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)

class User(AbstractBaseUser):
    username = models.CharField(db_column='login', unique=True, max_length=255)
    password = models.CharField(db_column='pass', max_length=255)  # Field renamed because it was a Python reserved word.
    type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    last_login = models.DateTimeField(db_column='lastlogin', blank=True, null=True)
    lastfail = models.DateTimeField(blank=True, null=True)
    skype_contact = models.CharField(max_length=1024, blank=True, null=True)
    jabber_contact = models.CharField(max_length=1024, blank=True, null=True)
    email = models.CharField(max_length=1024, blank=True, null=True)
    cell_phone = models.CharField(max_length=1024, blank=True, null=True)
    login_attempts = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['type', 'email', 'first_name', 'last_name']
    objects = UserManager()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return f'{self.first_name}'

    def set_password(self, password):
        if not password:
            self.set_unusable_password()
        else:
            self.password = hashlib.md5(password.encode()).hexdigest()

    def is_superuser(self):
        return self.type == ADMIN

    def is_staff(self):
        return self.type == ADMIN

    def check_password(self, password):
        if self.has_usable_password():
            test_password = hashlib.md5(password.encode()).hexdigest()
            return test_password == self.password
        return False

    def has_perms(self, perm_list, obj=None):
        if not self.is_active:
            return False
        if self.is_superuser():
            return True
        if len(perm_list) == 0:
            return True
        # TODO: Handle permissions for Program Managers, DJs and Guests for add and edit
        print(perm_list)
        return False

    class Meta:
        managed = False
        db_table = 'cc_subjs'


class UserToken(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    action = models.CharField(max_length=255)
    token = models.CharField(unique=True, max_length=40)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cc_subjs_token'


class Timestamp(models.Model):
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cc_timestamp'


class Webstream(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=512)
    length = models.DurationField()
    creator_id = models.IntegerField()
    mtime = models.DateTimeField()
    utime = models.DateTimeField()
    lptime = models.DateTimeField(blank=True, null=True)
    mime = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_webstream'


class WebstreamMetadata(models.Model):
    instance = models.ForeignKey(Schedule, models.DO_NOTHING)
    start_time = models.DateTimeField()
    liquidsoap_data = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'cc_webstream_metadata'


class CeleryTask(models.Model):
    task_id = models.CharField(max_length=256)
    track_reference = models.ForeignKey('ThirdPartyTrackReference', models.DO_NOTHING, db_column='track_reference')
    name = models.CharField(max_length=256, blank=True, null=True)
    dispatch_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'celery_tasks'


class CloudFile(models.Model):
    storage_backend = models.CharField(max_length=512)
    resource_id = models.TextField()
    filename = models.ForeignKey(File, models.DO_NOTHING, blank=True, null=True,
                                 db_column='cc_file_id')

    class Meta:
        managed = False
        db_table = 'cloud_file'


class ImportedPodcast(models.Model):
    auto_ingest = models.BooleanField()
    auto_ingest_timestamp = models.DateTimeField(blank=True, null=True)
    album_override = models.BooleanField()
    podcast = models.ForeignKey('Podcast', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'imported_podcast'


class Podcast(models.Model):
    url = models.CharField(max_length=4096)
    title = models.CharField(max_length=4096)
    creator = models.CharField(max_length=4096, blank=True, null=True)
    description = models.CharField(max_length=4096, blank=True, null=True)
    language = models.CharField(max_length=4096, blank=True, null=True)
    copyright = models.CharField(max_length=4096, blank=True, null=True)
    link = models.CharField(max_length=4096, blank=True, null=True)
    itunes_author = models.CharField(max_length=4096, blank=True, null=True)
    itunes_keywords = models.CharField(max_length=4096, blank=True, null=True)
    itunes_summary = models.CharField(max_length=4096, blank=True, null=True)
    itunes_subtitle = models.CharField(max_length=4096, blank=True, null=True)
    itunes_category = models.CharField(max_length=4096, blank=True, null=True)
    itunes_explicit = models.CharField(max_length=4096, blank=True, null=True)
    owner = models.ForeignKey(User, models.DO_NOTHING, db_column='owner', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'podcast'


class PodcastEpisode(models.Model):
    file = models.ForeignKey(File, models.DO_NOTHING, blank=True, null=True)
    podcast = models.ForeignKey(Podcast, models.DO_NOTHING)
    publication_date = models.DateTimeField()
    download_url = models.CharField(max_length=4096)
    episode_guid = models.CharField(max_length=4096)
    episode_title = models.CharField(max_length=4096)
    episode_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'podcast_episodes'


class StationPodcast(models.Model):
    podcast = models.ForeignKey(Podcast, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'station_podcast'


class ThirdPartyTrackReference(models.Model):
    service = models.CharField(max_length=256)
    foreign_id = models.CharField(unique=True, max_length=256, blank=True, null=True)
    file = models.ForeignKey(File, models.DO_NOTHING, blank=True, null=True)
    upload_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'third_party_track_references'

class TrackType(models.Model):
    code = models.CharField(max_length=16, unique=True)
    type_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    visibility = models.BooleanField(blank=True, default=True)

    class Meta:
        managed = False
        db_table = 'cc_track_types'
