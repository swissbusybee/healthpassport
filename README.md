# healthpassport

Install Chart.js - pip install django-chartjs

Clear Existing Data from database - python manage.py flush
Recreate Superuser - python manage.py createsuperuser

Load Seed Data: 
python manage.py loaddata blog/fixtures/familygroup-data.json
python manage.py loaddata blog/fixtures/profile-data.json
python manage.py loaddata blog/fixtures/vaccine-data.json
python manage.py loaddata blog/fixtures/immunization-data.json
python manage.py runserver
