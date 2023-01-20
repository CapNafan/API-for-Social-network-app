# TASK

**Description**  
Create a simple RESTful API using FastAPI for a social networking application

**Functional requirements:**\
There should be some form of authentication and registration (JWT, Oauth, Oauth 2.0, etc.)\
As a user I need to be able to sign up and login\
As a user I need to be able to create, edit, delete and view posts\
As a user I can like or dislike other users’ posts but not my own  
The API needs a UI Documentation (Swagger/ReDoc)

# How to run
 - In order for an API to work, PostgreSQL needs to be whether installed on your local machine
or run on remote server. User and password to PostgreSQL have to be created
 - Pull the repository to your environment

 - Create and activate virtualenv:
 >**python -m pip install --upgrade pip**  
 **python -m pip install --user virtualenv**  
 **python -m venv venv**  
 **source venv/bin/activate** For Linux  
 **venv\Scripts\activate.bat** For Windows
> 
 - Install all requirements using  
>**python -m pip install -r requirements.txt**  
> 
 - Create ".env" file in the same directory with app, gitignore and requirements.txt file
 - Populate ".env" file with your user credentials for PostgreSQL and JWT settings:
```
DATABASE_HOSTNAME=<host_name>
DATABASE_PORT=<port>
DATABASE_PASSWORD=<password_to_database>  
DATABASE_NAME=<db_Name>
DATABASE_USERNAME=<username>  
SECRET_KEY=<secret_key_for_jwt_signature>
ALGORITHM=<Algorithm>
ACCESS_TOKEN_EXPIRE_MINUTES=<time_in_minutes>
```

 - Located in the same directory with app, run
>**uvicorn app.main:app --host host_name --port port**