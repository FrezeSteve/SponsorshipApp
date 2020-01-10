# SponsorshipApp
A Simple Sponsorship Web Django Application

# SETUP
Clone the repository into your local machine.
Add a media directory for uploading media files.

make sure you have your postgresql installed and running.
create a database called testdjango.
add a user and grant all privilidges for testdjango to that user.
adjust the various settings of your database to settings.py in the project.

make sure your activate your virtual environment.
install all the requirements listed in the requirements.txt.

run python manage.py makemigrations.
then run python manage.py migrate. This will create all the tables necessary to run the application.
if an error is encountered make sure that settings for your database are set correctly.
