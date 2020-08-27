# Health Passport
## Digital Health & Vaccination Tracker
### Health Passport was developed to solve a real world problem of not having vaccination & critical health data in a central location.

![alt text](https://images.unsplash.com/photo-1581553673739-c4906b5d0de8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1650&q=80)

#### Language Used: Python
#### Framework Used: Django
#### Additional Plugins: 
* Cloudinary
* Twilio
* Chart.js

Developer Notes:
Clear Existing Data from database - python manage.py flush
Recreate Superuser - python manage.py createsuperuser

Load Seed Data: 
python manage.py loaddata app/fixtures/familygroup-data.json
python manage.py loaddata app/fixtures/profile-data.json
python manage.py loaddata app/fixtures/vaccine-data.json
python manage.py loaddata app/fixtures/immunization-data.json
python manage.py runserver
