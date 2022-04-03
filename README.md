# Booking

This is a simple application written in Django for Global Talents Hub.
The application has two models. Rental and Reservation which are belong to a hotel.
The main goal is to show the previous reservation dates of a Rental instance.

## How to use

You may Install Python, create a Virtualenv after cloning the project and change the source to it:
brew install python3 python3-pip
pip3 install virtualenv
virtualenv venv
source venv/bin/activate

Install the required packages:
pip install -r requirements.txt

Create the dataase, run test and run server
pyhton manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py runserver 0.0.0.0:8000

Call the get method of http://127.0.0.1:8000/api/v1/reservation to see the result
