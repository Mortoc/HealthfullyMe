#! /bin/bash

python manage.py collectstatic --noinput &
python manage.py syncdb --noinput
python manage.py migrate --noinput
