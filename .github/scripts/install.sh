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
    setupAirtimePostgresUser() {
        # here-doc to execute this block as postgres user
        su postgres <<'EOF'
        set +e
        count=$(psql -d postgres -tAc "SELECT count(*) FROM pg_roles WHERE rolname='airtime';")
        if [[ $count -eq 0 ]]; then
            psql -d postgres -tAc "CREATE USER airtime WITH ENCRYPTED PASSWORD 'airtime'; ALTER USER airtime CREATEDB; CREATE DATABASE libretime; GRANT CONNECT ON DATABASE libretime TO libretime;"
            [[ $? -eq 0 ]] && 
                  echo "Created airtime user in PostgreSQL" || 
                  echo "$0:${FUNCNAME}(): ERROR: Can't create airtime user in PostgreSQL!"
        else
            echo "airtime user already exists in PostgreSQL"
        fi
        set -e
# don't indent this!
EOF
    }

setupAirtimePostgresUser