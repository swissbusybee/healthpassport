# healthpassport

Install Chart.js - pip install django-chartjs

Clear Existing Data from database - python manage.py flush
Recreate Superuser - python manage.py createsuperuser

Load Seed Data: 
python manage.py loaddata app/fixtures/familygroup-data.json
python manage.py loaddata app/fixtures/profile-data.json
python manage.py loaddata app/fixtures/vaccine-data.json
python manage.py loaddata app/fixtures/immunization-data.json
python manage.py runserver
