# SponsorshipApp
A Simple Sponsorship Web Django Application

# SETUP
Clone the repository into your local machine.
Add a media directory for uploading media files.

make sure you have your postgresql installed and running.
create a database called testdjango.
add a user and grant all privilidges for testdjango to that user.
adjust the various settings of your database to settings.py in the project.

open a terminal from your project folder
make sure your activate your virtual environment.
install all the requirements listed in the requirements.txt.

run "python manage.py makemigrations".
then run "python manage.py migrate". This will create all the tables necessary to run the application.
if an error is encountered make sure that settings for your database are set correctly.

run "python manage.py runserver" command to run the django server

copy the url to your browser

# About
The application has three user: users applying for sponsorship, sponsors and staff.

The staff are automatically registered by running the command "python manage.py createsuperuser".
The staff register the sponsors by creating a user then assigning the role of sponsor in the admin panel
through the sponsor model. The staff can also view the various sponsorship application through navigating to staff on the navbar. The staff can approve the applications.

The sponsor can login only after they have been registered by staff. Sponsors after login can view appproved applications and decide which one to sponsor.

The user seeking sponsorship has it very easy because the first view is a step by step wizard application for 
sponsorship. After submission they will automatically be redirected to a success page otherwise they will get an error 
and will have to redo the wizard again from the beginning.

Obviously there are many improvements to be made from this project such as using forms in the wizard instead of html5 elements. I believe it was a great learning experience. 
