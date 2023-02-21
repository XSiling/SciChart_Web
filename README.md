# SciChart_Web

This is a website based on django, which is able to help people paint charts more easily.

## Feature
- Login and Register
- Data Load and Charts Painting

## Configuration

You should own sql at your PC.

In settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '-----', # change to ur own database name
        'HOST': '127.0.0.1',
        'PORT': ----, # change to ur own sql port
        'USER': 'root',
        'PASSWORD': '-----', # change to ur own password of database
    }
}
```

## How To Run:

```
cd HelloWorld
python manage.py runserver 0.0.0.0:8000
```

Then visit 127.0.0.1:8000 at your own website.
