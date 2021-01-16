# isItValentine
A simple Django app that checks if current day is Valentine's day

## To create app
Run : django-admin startproject PROJECT_NAME

## To create new app from newly created django project directory
Run: python manage.py startapp APP_NAME

## Edit settings.py file of django project to include newly created app
INSTALLED_APPS = [
    'checkvalentine',
    ...
]

## Register the url path of the newly created app in the urls.py file of the django project
urlpatterns = [
    ...
    path('isitvalentine/', include('checkvalentine.urls'))
]

If you created a new app via the startapp command above, create your styles.css, urls.py, and index.html files accordingly

## Run app via the console on localhost by the command
python manage.py runserver
