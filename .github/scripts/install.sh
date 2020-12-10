#/bin/bash

# Adding repos and packages
add-apt-repository -y ppa:libretime/libretime
apt-get -q update
apt-get install -y gstreamer1.0-plugins-base \
  gstreamer1.0-plugins-good \
  gstreamer1.0-plugins-bad \
  gstreamer1.0-plugins-ugly \
  libgirepository1.0-dev \
  liquidsoap \
  liquidsoap-plugin-faad \
  liquidsoap-plugin-lame \
  liquidsoap-plugin-mad \
  liquidsoap-plugin-vorbis \
  python3-gst-1.0 \
  silan \
  gcc \
  gir1.2-gtk-3.0 \
  python3-setuptools \
  python3-gi \
  python3-gi-cairo \
  python-cairo \
  pkg-config \
  libcairo2-dev \
  php \
  php-curl \
  php-gd \
  php-pgsql \
  postgresql \
  postgresql-client

# Creating database for testing
systemctl restart postgres
sudo -u postgres psql -c 'CREATE DATABASE libretime;' 
sudo -u postgres psql -c "CREATE USER libretime WITH PASSWORD 'libretime';"
sudo -u postgres psql -c 'GRANT CONNECT ON DATABASE libretime TO libretime;'
sudo -u postgres psql -c 'ALTER USER libretime CREATEDB;'
mkdir -p /tmp/log/libretime