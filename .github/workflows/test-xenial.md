name: test-xenial
on:
  push:
    paths-ignore:
    - 'docs/**'
jobs:
  test-xenial:
    runs-on: ubuntu-16.04
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.5'
      - uses: harmon758/postgresql-action@v1
        with:
          postgresql version: '11'
          postgresql db: 'libretime'
          postgresql user: 'libretime'
          postgresql password: 'libretime'
      - run: ENVIRONMENT=testing && LIBRETIME_LOG_DIR=/tmp/log/libretime
      - run: psql -c 'ALTER USER libretime CREATEDB;' -U postgres
      - run: sudo bash dev_tools/ci/install.sh
      - run: sudo composer install
      - run: sudo pip3 install -e python_apps/airtime_analyzer/.
      - run: sudo pip3 install -e python_apps/airtime-celery/.
      - run: sudo pip3 install -e python_apps/api_clients/.
      - run: sudo pip3 install -e python_apps/pypo/.
      - run: nosetests python_apps/airtime_analyzer/.
      - run: nosetests python_apps/api_clients/.
