# LibreTime API

This API provides access to LibreTime's database via a Django application. This
API supersedes the [PHP API](../airtime_mvc/application/controllers/ApiController.php).

## Deploying

Deploying in a production environment is done in the [`install`](../install)
script which installs LibreTime. This is how the API is installed in the Vagrant
development images too. This method does not automatically reflect changes to
this API. After any changes, the `libretime-api` systemd service needs
restarting:

    sudo systemctl restart libretime-api

### Development
For a live reloading version within Vagrant:

```
vagrant up debian-buster
vagrant ssh debian-buster
cd /vagrant/api
sudo systemctl stop libretime-api
sudo -u www-data LIBRETIME_DEBUG=True python3 manage.py runserver 0.0.0.0:8081
```
