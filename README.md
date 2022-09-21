# Techwondoe-Assignment

This project serves as a very slim backend API developed with the help of Django-REST-Framework and Docker.

You can read more on [DRF](https://www.django-rest-framework.org/) and [Docker](https://docs.docker.com/).

## Project Structure
```
Techwondoe-Assigment
|---companytech
|    |---__pycache__
|    |---__init__.py
|    |---asgi.py
|    |---settings.py
|    |---urls.py
|    |---wsgi.py
|---tech
|    |---__pycache__
|    |---migrations
|    |---__init__.py
|    |---admin.py
|    |---apps.py
|    |---models.py
|    |---serializers.py
|    |---tests.py
|    |---urls.py
|    |---views.py
|---Dockerfile
|---README.md
|---db.sqlite3
|---docker-compose.yml
|---manage.py
|---requirements.txt
```

Company tech will contain settings of project and tech includes the django app.

-- Models.py will contain the schema.

-- urls.py of companytech will contain urls mapped with urls of tech.

-- views.py contains all the API function which are further mapped with urls.py with some routing.

-- docker-compose will contain instructions needed to run and build a container.

-- Dockerfile contains docker settings and app directory which will contain instruction that will be executed each time we build the container.

## Installing dependencies
All the requiremets or dependencies are included in requirements.txt file with the help of which user to install all dependencies by using the following command. 
```
pip install -r requiements.txt
```

## Authentication
This Project uses pyjwt for user authentication. 

You can read more about the API [here](https://pyjwt.readthedocs.io/en/stable//).

To authenticate a user require username and password. whenever user submit these details, API will check first that the user exist is the schema or not with given username. If user doesn't exists, then it will throws an error, else again it will check for the password. If the password matches with the user password, then with the help of authenticate() user will be authenticated. Then a payload will be created which contains user ID, expiry time, creation time. After that a token will be generated with the help of JWT encode function and HS256 algorithm encoded that payload. The token is then stored in cookies which will further help in verification.

Now, whenever a user access an API that have login required then the token will be taken from cookies then verified with the help of jwt.decode function. If it successfully verified then it will access those API. If the token expires then user needs to be authenticate again in order to access those routes.

## SuperUser Auth
All the CRUD operations are only accessed by superuser only or admin only. So, the user once verified need to be checked for the role whether it is a super user or not, if it is then they will access the API, else "Access Denied" will be returned as response.

## Creating SuperUser
One can use following command to create an super user.
```
python manage.py createsuperuser
```

## Running the server
If you wish to run the server, the first step is installing dependencies.

The second step includes installing Docker. If you have alraedy install this, then ignore this step.

Docker Desktop can be installed from [Docker Desktop](https://www.docker.com/products/docker-desktop/) for both windows and linux.

Once that's out of the way, then run the following command:

```
docker-compose build
docker-compose up
```

which should result in output such as:

```
[+] Running 1/0
 - Container techwondoe-assignment-web-1  Created                                                                                                                        0.0s
Attaching to techwondoe-assignment-web-1
techwondoe-assignment-web-1  | Watching for file changes with StatReloader
techwondoe-assignment-web-1  | Performing system checks...
techwondoe-assignment-web-1  | 
techwondoe-assignment-web-1  | System check identified some issues:
techwondoe-assignment-web-1  |
techwondoe-assignment-web-1  | WARNINGS:
techwondoe-assignment-web-1  | tech.Company.InceptionDate: (fields.W161) Fixed default value provided.
techwondoe-assignment-web-1  |  HINT: It seems you set a fixed date / time / datetime value as default for this field. This may not be what you want. If you want to have the current date as default, use `django.utils.timezone.now`
techwondoe-assignment-web-1  |
techwondoe-assignment-web-1  | System check identified 1 issue (0 silenced).
techwondoe-assignment-web-1  | September 21, 2022 - 11:34:53
techwondoe-assignment-web-1  | Django version 3.2.15, using settings 'companytech.settings'
techwondoe-assignment-web-1  | Starting development server at http://0.0.0.0:8000/
techwondoe-assignment-web-1  | Quit the server with CONTROL-C.

```

indicating the server is now listening at port 8000.

The server is now ready to run at [URL](http://127.0.0.1:8000/api/).

## Models(Schema)
This project will contain two models company and team.

### Company
It will contain fields which are given below:

-- UUID (primary Key)

-- Company name

-- Company CEO

-- Company address

-- Inception date

### Teams
It will contain fields which are given below:

-- UUID (primary Key)

-- CompanyID (Foreign Key)

-- Team Lead Name

## Serializers
Serializers helps to convert complex data type such as object to data types understandable by javascript and front-end frameworks.
They also provides deserialization which allows parsed data to be converted back into complex types, after first validating the incoming data.

You can read more about it on [Serializers](https://www.django-rest-framework.org/api-guide/serializers/).

## Routes
The project contain some API that are mapped to some URL which are given below.

### LOGIN
User can login via [URL](http://127.0.0.1:8000/api/login)

In order to access the Routes, User needs to be authenticated and only superuser has the access to perform CRUD operations.
This require two parameters - username, password as JSON Object.
On successful signIn a JWT token will be generated and stored in cookie which will further used for verifying the logged in user.
The API will return the JWT Token as response.

### Create a Company
User can create a company using [URL](http://127.0.0.1:8000/api/)

In order to create a company, user need to enter data in the form of JSON object in the APIview provided by Django-REST-Framework.
JSON object will contain all details provided in the above model except UUID. UUID will be created automatically once a company will be created.
On entering the data, it will first check whether any Company exists with the same name. If it exits, then it will return a response that "Company Already Exists", else it will create a company after verifying the data through serializer.

### Create a Team
User can create a team using http://127.0.0.1:8000/api/team/create/companyid 

In this user need to enter companyid in the url path in place of companyid
In order to create a team, user need to enter data in the form of JSON object in the APIview provided by Django-REST-Framework.
JSON object will contain all details provided in the above model except UUID. UUID will be created automatically once a company will be created.
It will create a team after verifying the data through serializer.

### Get Company object from ID
User can get company details from company ID using two routes, one needs ID in path, second needs ID as an JSON object.

#### ID in path
User can get a company details using http://127.0.0.1:8000/api/company/id/CompanyID.

user need to enter companyid in the url path in place of CompanyID.

#### ID as JSON
User can get company details using http://127.0.0.1:8000/api/company/id

User need to enter data companyid as JSON object.
It will return company details after passing through serializer.

### Search company by name
User can get a company details using http://127.0.0.1:8000/api/company/name

User need to enter data companyName as JSON object.
It will return company details after passing through serializer.

### Get All Teams
To get all teams as an array grouped within company object using http://127.0.0.1:8000/api/team/group


