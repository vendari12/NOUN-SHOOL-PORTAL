# django-school-management

A school management software for correlating and administrating school processes.
Features include

1. Teacher / Lecturers Login Panel
2. Student Login Panel
3. Result management console 
4. Admin console

# TODO
1. Research facilities
2. Support for Oauth authentication
3. API (Application profiling interface with prometheus, opentelemetry and signox) integration
4. Container support (Docker, Docker-compose)
5. Real time logging
6. Redis Integration for heavy lifting 


## SETUP

# Requirements

1. Python 3.7 +
2. pip3 
3. Virtualenv (Virtual environement for dependency isolation)
3. Browser support modern scripting


# Running the project

1. create a virtual environment using virtualenv
`` pip install virtualenv``
``pip install -r requirements.txt``

2. Make project migrations to initialize in memory database (db.sqlite3)
``python manage.py migrate``

3. Create a superuser using 
``python manage.py createsuperuser``

4. Run project
``python manage.py runserver``

5. Visit [http://127.0.0.1:8000] on your browser to view project.




NOUN RESULT PORTAL SYSTEM DESIGN

Project Main Dependencies:

. Python 3.7 +
2. pip3
3. Virtualenv (Virtual environment for dependency isolation)
3. Browser support modern scripting
 

This project is intended to run on all operating systems, from windows Os to linux and Unix systems.

System Requirements:
Operating system ( windows, Linux, Unix) s
Minimum 512mb of RAM space, this project scripts can be loaded onto a 512mb ram memory as it is designed and optimized for memory management efficiency consuming less resources while delivering optimal performance.
Minimum of 1gb storage space, a minimum of 1GB(1024 megabytes) of secondary storage space is required as files require this to effectively carry out manipulations without worrying about the amount of available address on the system.


PROCESS / PACKAGE FLOW



