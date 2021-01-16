## Is it Valentine's day?
This is a simple Django app that checks if current day is Valentine's day

### Create Django project
Run : django-admin startproject PROJECT_NAME

### Create new app from newly created django project directory
Run: python manage.py startapp APP_NAME

### Edit settings.py file of django project to include newly created app
INSTALLED_APPS = [
    'APP_NAME',
    ...
]

### Register the url path of the newly created app in the urls.py file of the django project
urlpatterns = [
    ...
    path('URL_PATH/', include('APP_NAME.urls'))
]

If you created a new app via the startapp command above, create your styles.css, urls.py, and index.html files accordingly, as seen in my checkvalentine folder

### Run app via the console on localhost by the command
python manage.py runserver

### You can view app in action at url:

http://emman77240.pythonanywhere.com/isvalentines/
