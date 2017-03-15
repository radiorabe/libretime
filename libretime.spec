#
# spec file for LibreTime
#
# Copyright (c) 2017 LibreTime Community
#                    http://libretime.org
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public 
# License as published  by the Free Software Foundation, version
# 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License  along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
# Please submit enhancements, bugfixes or comments via GitHub:
# https://github.com/LibreTime/libretime
#

%define _version     3.0.0-alpha
%define _rpm_version 3.0.0.alpha

Name:           libretime
Version:        %{_rpm_version}
Release:        0
Summary:        LibreTime Radio Automation Suite

License:        AGPLv3
URL:            http://libretime.org
Source0:        %{name}-%{_version}.tar.gz

BuildRequires: python-setuptools
BuildRequires: pytz
BuildRequires: python-boto
BuildRequires: python-nose
BuildRequires: python-mutagen
BuildRequires: python-amqp
BuildRequires: python-amqplib
BuildRequires: python-six
BuildRequires: python-configobj
BuildRequires: python-inotify
BuildRequires: python-pydispatcher
BuildRequires: python-poster
BuildRequires: python-kombu
BuildRequires: python-docopt
BuildRequires: python-mutagen
BuildRequires: python-vine
BuildRequires: python-requests
BuildRequires: systemd

%description
LibreTime makes it easy to run your own online or terrestrial
radio station. It is a community managed fork of the AirTime
project.
It is managed by a friendly inclusive community of stations 
from around the globe that use, document and improve LibreTime. 

%prep
%setup -q -n %{name}-%{_version}

%build

%install
rm -rf $RPM_BUILD_ROOT

# Install system directories
install -d %{buildroot}/%{_sysconfdir}/airtime
install -d %{buildroot}/%{_unitdir}

# isntall all the systemd units from centos-rpm repo
install installer/systemd/*.service %{buildroot}/%{_unitdir}

# install airtime-web parts in the right location for the httpd package
mkdir -p $RPM_BUILD_ROOT/var/www/
cp -rp airtime_mvc/{application,build,locale,public} $RPM_BUILD_ROOT/var/www/
cp -rp vendor $RPM_BUILD_ROOT/var/www/
ls $RPM_BUILD_ROOT/var/www
mv $RPM_BUILD_ROOT/var/www/public $RPM_BUILD_ROOT/var/www/html
# configure zend config dep into scl php
install -d %{buildroot}/etc/php.d
cat << EOF > %{buildroot}/etc/php.d/50-upload_tmp_dir.ini
[main]
upload_tmp_dir=/tmp
EOF
cat << EOF > %{buildroot}/etc/php.d/50-upload_max_filesize.ini
upload_max_filesize=20M
post_max_size=20M
EOF

# setup apache
install -d %{buildroot}/etc/httpd/conf.d
cat << EOF > %{buildroot}/etc/httpd/conf.d/airtime-fallback.conf
<Directory "/var/www/html/">
    FallbackResource /index.php
</Directory>
EOF


# install airtime-utils so they can be called by a user

mkdir -p $RPM_BUILD_ROOT/usr/{sbin,bin}
pushd utils
cp airtime-backup.py \
   airtime-log \
   airtime-log.php \
   airtime-import/airtime-import \
   $RPM_BUILD_ROOT/usr/sbin/

cp airtime-test-soundcard \
   airtime-test-soundcard.py \
   airtime-test-stream \
   airtime-test-stream.py \
   $RPM_BUILD_ROOT/usr/bin/
popd

export PYTHONPATH=$RPM_BUILD_ROOT/${_prefix}usr/lib64/python2.7/site-packages
mkdir -p $PYTHONPATH

# install analyzer python app
pushd python_apps/airtime_analyzer
python setup.py build --no-init-script
python setup.py install --no-init-script --prefix=$RPM_BUILD_ROOT/${_prefix}usr --install-lib=$PYTHONPATH --single-version-externally-managed --record=installed.pth
mkdir -p $RPM_BUILD_ROOT/${_prefix}etc/airtime/
popd
install -d %{buildroot}/%{_tmppath}/airtime/airtime_analyzer

# install api_clients module
pushd python_apps/api_clients/
python setup.py build
python setup.py install --prefix=$RPM_BUILD_ROOT/${_prefix}usr --install-lib=$PYTHONPATH --single-version-externally-managed --record=installed.pth
popd

# install pypo module
pushd python_apps/pypo/
python setup.py build --no-init-script
python setup.py install --no-init-script --prefix=$RPM_BUILD_ROOT/${_prefix}usr --install-lib=$PYTHONPATH --single-version-externally-managed --record=installed.pth
popd

# install icecast xsl
pushd python_apps/icecast2
mkdir -p $RPM_BUILD_ROOT/${_prefix}usr/share/icecast/web
cp airtime-icecast-status.xsl $RPM_BUILD_ROOT/${_prefix}usr/share/icecast/web/airtime-icecast-status.xsl
popd

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.md CREDITS LICENSE LICENSE_3RD_PARTY
%dir %{_sysconfdir}/airtime
%dir %{_tmppath}/airtime


%changelog

%package web
Summary: radio rabe airtime web interface installation

Requires: php
Requires: php-pdo
Requires: php-gd
Requires: php-pgsql
Requires: php-bcmath
Requires: php-mbstring
Requires: php-fpm
Requires: php-ZendFramework-full
Requires: httpd
Requires: liquidsoap

%description web
Installs the airtime web interface into /var/www.

%files web
%config(noreplace) /var/www/application/configs/application.ini
%config(noreplace) /etc/php.d/*.ini
%config(noreplace) /etc/httpd/conf.d/airtime-fallback.conf
/var/www/

%package utils
Summary: radio rabe airtime utils installation

%description utils
Installs the various utils neeeded by airtime to d stuff on the cli.

%files utils
/usr/sbin/airtime-backup.py
/usr/sbin/airtime-log
/usr/sbin/airtime-log.php
/usr/sbin/airtime-import
/usr/bin/airtime-test-*



%package analyzer
Summary: LibreTime Media Analyzer component

AutoReqProv: no

Requires: %{name} = %{version}-%{release}
Requires: python
Requires: pytz
Requires: python-mutagen
Requires: python-amqp
Requires: python-amqplib
Requires: python-six
Requires: python-configobj
Requires: python-inotify
Requires: python-pydispatcher
Requires: python-poster
Requires: python-kombu
Requires: python-docopt
Requires: python-vine
Requires: %{name}-api_clients
Requires: lsof
%{?systemd_requires}

%description analyzer
airtime analyzer imports uploaded files and watches directories

%pre analyzer
getent group airtime-analyzer >/dev/null || groupadd -r airtime-analyzer
getent passwd airtime-analyzer >/dev/null || \
    useradd -r -g airtime-analyzer -d /var/tmp/airtime/analyzer -m \
    -c "Airtime media analyzer" airtime-analyzer
exit 0

%post analyzer
%systemd_post airtime_analyzer.service

%preun analyzer
%systemd_preun airtime_analyzer.service

%postun analyzer
%systemd_postun airtime_analyzer.service

%files analyzer
%dir %attr(-, airtime-analyzer, airtime-analyzer) %{_tmppath}/airtime/airtime_analyzer
%attr(550, -, -) %{_unitdir}/airtime_analyzer.service
%{_bindir}/airtime_analyzer
%{_libdir}/python2.7/site-packages/airtime_analyzer*


%package api_clients
Summary: radio rabe airtime python api clients

AutoReqProv: no

Requires: python

%description api_clients
airtime python api client library

%files api_clients
/usr/lib64/python2.7/site-packages/api_clients*



%package pypo
Summary: radio rabe airtime pypo installation

AutoReqProv: no

Requires: python
Requires: python-requests
Requires: liquidsoap
Requires: python-setuptools
Requires: pytz
Requires: python-inotify
Requires: python2-pydispatcher
Requires: python-poster
Requires: python-mutagen
Requires: python-kombu
Requires: python-amqplib
Requires: python-vine
Requires: airtime-api_clients
%{?systemd_requires}

%description pypo
Python Play-Out for airtime calls liquidsoap as defined in airtime.


%pre pypo
getent group airtime-pypo >/dev/null || groupadd -r airtime-pypo
getent passwd airtime-pypo >/dev/null || \
    useradd -r -g airtime-pypo -d /dev/null \
    -c "Airtime pypo playout server" airtime-pypo
exit 0

%post pypo
%systemd_post airtime-playout.service
%systemd_post airtime-liquidsoap.service

%preun pypo
%systemd_preun airtime-playout.service
%systemd_preun airtime-liquidsoap.service

%postun pypo
%systemd_postun airtime-playout.service
%systemd_postun airtime-liquidsoap.service


%files pypo
%attr(550, -, -) %{_unitdir}/airtime-playout.service
%attr(550, -, -) %{_unitdir}/airtime-liquidsoap.service
%{_libdir}/python2.7/site-packages/airtime_playout*
%{_libdir}/python2.7/site-packages/pypo/
%{_libdir}/python2.7/site-packages/liquidsoap/
%{_bindir}/airtime-liquidsoap
%{_bindir}/airtime-playout
%{_bindir}/pyponotify



%package icecast
Summary: radio rabe airtime icecast xsl installation
AutoReqProv: no
Requires: icecast

%description icecast
Install LibreTime icecast XML snippet into icecast webdir.

%files icecast
%{_datarootdir}/icecast/web/airtime-icecast-status.xsl


%package celery
Summary: LibreTime Celery Tasks

AutoReqProv: no

Requires: python-celery

%description celery
LibreTime Celery Tasks.

%post celery
%systemd_post airtime-celery.service

%preun celery
%systemd_preun airtime-celery.service

%postun celery
%systemd_postun airtime-celery.service

%files celery
%attr(550, -, -) %{_unitdir}/airtime-celery.service
