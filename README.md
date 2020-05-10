# Trello Board Application

### Built a "headless" simple Trello board application to manage users and their tasks.	

#### Assumptions (Developed somewhat similar to real Trello/JIRA Application)
 - Application admin and Project admin are two different terms. Application admin is the one who is owner/developer/CTO of the whole application/company. Project admin is any authorized user who has created the project board.
 - Application admin has all the permissions to all the API endpoints.
 - User can be uniquely identified by username or email id.
 - All requests must be authorised via token except login/signup requests. This token can be retrieved by requesting on login API endpoint by sending credentials in the request.
 - Project admin can deactivate any user(project admin/non-admin users) from the project except himself/herself.
 - Only project admin can update the project board's details. 

 #### Features (Implemented via API endpoints)
  - There can be mulitple project admins. Only admin can make other user as an admin of that project.
  - Once an user is deactivated it will automatically become a non-admin as well (if user was admin earlier).
  - At any time there will always be atleat one admin of a project board.
  - Any number of statuses can be added for a particular project board.
  - User(admin/non-admin) associated to n projects can view all users of those n projects. Can also view users of a specific project.
  - Application Admin can view all users of all projects whether associated with project or not. Can also view it from Admin Panel.
  - To add/retrieve/edit/remove a task, one must be associated to the task's project board.

#### Other Implementations
 - Generated [API documentation](https://documenter.getpostman.com/view/5222257/SzmfXxAa) via Postman Collection
 - Done with API testing.
 - Tried dockerizing the code. Made Docker Files but the code is not dockerized due to few issues.
 - Built admin panel using Django admin panel. Checked all the functionalities via admin panel.
 - How to build and run the code is mentioned below.


#### This Application has three entities:

  - **Users**: Users of the application. 
    - [x] Each user is uniquely identified by his/her email address.
    - [x] There will be two roles: Admin and User. 
      - [x] Admin will be able to create/archive/unarchive Project Boards
      - [x] Admin will be able to view all users of all project boards
      - [x] Admin will be able to add new user or deactivate existing user from Project Board
      - [x] Non-Admin users will be able to view all the users of Project Boards that they're assigned to.
				
  - **Project Boards**: 
   - [x] Represents a Project which will have tasks defined under it. A non-admin user needs to be assigned to a particular Project Board in order to view it. 
		
  - **Tasks**: An atomic entity that defines the objective. 
    - [x] A Task is assignable to/by a user of the system. 
    - [x] A Task belongs to a particular Project Board.
    - [x] A Task should have minimum of the following properties: Title, Description, Assignee, Assigner, Due Date, Status.
    - [x] A Task can be added/removed/edited
    - [x] A Task can be in a particular Status. For ex: "Backlog", "InProgress", "Done".
    - [x] User can create any number of new statuses or remove existing Status in a Project Board and once defined, A Task can be assigned to one of these statuses.


# How to Build and Run the Code

### Installation Requirements
- Python 3.6
- Pip 20.1
- Virtualenv
- Postgres 10.6

### Postgres Setup
- Install postgreSQL
```
$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```
- Run the following commands
```
$ sudo -u postgres psql
$ CREATE DATABASE trello_dev;
$ CREATE USER jatin WITH PASSWORD ' ';
$ ALTER ROLE jatin SET client_encoding TO 'utf8';
$ ALTER ROLE jatin SET default_transaction_isolation TO 'read committed';
$ ALTER ROLE jatin SET timezone TO 'Asia/Kolkata';
```

### Installation Guide
- Switch on your Virtualenv `source bin/activate`
- git clone the repository. `git@github.com:jatin759/trello.git`
- `$ cd trello/`.
- Install all dependencies `$ pip install -r requirements.txt`

### Migrations, SuperUser, Local Server and Admin Panel
- Run migrations
```
$ python manage.py makemigrations
$ python manage.py migrate
```

- Create SuperUser
```
$ python manage.py createsuperuser
```

- Run Server
```
$ python manage.py runserver
```
- The server is running at [127.0.0.1:8000](http://127.0.0.1:8000/)

- Visit [Admin Panel](http://127.0.0.1:8000/admin) and log in with superuser credentials.

### Setting Up Environment Variables
- For development purpose .env file is uploaded to git.