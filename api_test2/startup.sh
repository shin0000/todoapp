cd api_test2
# django-admin startproject api_test1 .
# python3 manage.py startapp api1
python3 manage.py makemigrations
python3 manage.py migrate
# python3 manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8000