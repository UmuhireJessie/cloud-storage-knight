# FILE API


## Description

MNO Service API is the API that deals with uploading files on the AWS and getting them through two different endpoints.

## Technologies Used

The following are the technologies which have been used in this API with their URLs

- Postgres

To test the API, one should have the credentials for the above.

## Service local development
The service demonstrates different operation of Files (Create and Read operation) using FastAPI.

Feel free to modify config variables in `core/config.py` file to interact with the two endpoints.

* To set up the service

Create a virtual environment

```bash
virtualenv venv
```

Activate and Install requirements
```bash
. venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file with at least the following variables (See the `app/core/config` file for all variables):
* POSTGRES_SERVER
* POSTGRES_USER
* POSTGRES_PASSWORD
* POSTGRES_DB

Create the database with the above credentials

Start the service:
```bash
sh run.sh
```

OR
```bash
uvicorn app.app:app --port 5000
```

This script creates the database tables and then starts the application


* Now you can open your browser and interact with these URLs:

API JSON based web API based on OpenAPI: http://localhost:5000/docs/