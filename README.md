# GeoTest
# What we need
-Python https://www.python.org/

-Django https://www.djangoproject.com/

-geoDjango https://docs.djangoproject.com/pl/2.2/ref/contrib/gis/

-postgres https://www.postgresql.org/

-Postgis https://postgis.net/

-requests  http://docs.python-requests.org/en/master/

# How to run app locally

Install and configure package from above. 

Then use git clone command to download source code

git clone https://github.com/Tomel23/GeoTest.git
then use folowing commands:

$cd ./GeoTest
$virtualenv untitled5
$source ./untitled5/bin/activate
$pip install -r requirements.txt

Then modify untitled5/settings.py file to set db name, pass etc.

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geo_test_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5454'}
}

runn server app 

python manage.py runserver

Then in new terminal run client script

python ./Client client.py

# Other info

sample user:

Login: tomek

Pass: tomek



