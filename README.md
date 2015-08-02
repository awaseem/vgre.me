# vgre.me

My personal video game review website made with django. 

These are instructions for just a local dev setup. For production you will need to create a settings.cfg file in `django_project/django_project` and add the following:

```
[KEYS]
SECRET_KEY = YOUR SECRET KEY

[database]
name = DATABASE NAME
user = DATABASE USER
password = DATABASE PASSWORD

[email]
host = EMAIL HOST
user = EMAIL ADDRESS
password = EMAIL PASSWORD
port = EMAIL PORT
```

You might also want to change your database engine: 

```
    DATABASES = {
        'default': {
            'ENGINE': DATABASE ENGINE,
            'NAME': production_settings.get("database", "name"),
            'USER': production_settings.get("database", "user"),
            'PASSWORD': production_settings.get("database", "password"),
            'HOST': 'localhost',
            'PORT': '',
        }
    }
```

## Setup 

Start by installing all the projects dependencies:

`pip install -r requirements.txt`

Then migrate all migrations to your dev database:

`python manage.py migrate`

You'll need to create a superuser to get access to the admin page:

`python manage.py createsuperuser`

After that you'll need to login as admin, create a theme and one article (make sure you publish the article, its one of the admin actions in the article section). Then you should be good to go :)

