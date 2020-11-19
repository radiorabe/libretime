# LibreTime API

This API provides access to LibreTime's database via a Django application. This
API supersedes the [PHP API](../airtime_mvc/application/controllers/ApiController.php).

## Deploying

The quoted documentation will not work currently. It depends on a systemd unit that
has not yet been written. The only supported method of running currently is the
development install instructions.

> Deploying in a production environment is done in the [`install`](../install)
> script which installs LibreTime. This is how the API is installed in the Vagrant
> development images too. This method does not automatically reflect changes to
> this API. After any changes, the `libretime-api` systemd service needs
> restarting:
>
>     sudo systemctl restart libretime-api

### Development
For a live reloading version within Vagrant:

```
vagrant up debian-buster
# Run through the web setup http://localhost:8080
vagrant ssh debian-buster
sudo systemctl restart libretime-analyzer libretime-celery libretime-liquidsoap libretime-playout
cd /vagrant/api
sudo -u www-data LIBRETIME_DEBUG=True python3 manage.py runserver 0.0.0.0:8081
```
